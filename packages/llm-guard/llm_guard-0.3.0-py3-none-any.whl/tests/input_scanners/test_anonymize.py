import re

import pytest

from llm_guard.input_scanners.anonymize import Anonymize, sensitive_patterns_path
from llm_guard.input_scanners.anonymize_helpers.analyzer import RECOGNIZER_SPACY_EN_PII_FAST
from llm_guard.util import read_json_file
from llm_guard.vault import Vault

_preamble = (
    "In the following prompt, I am going remove certain information and replace each instance with "
    "sequentially-numbered placeholders in ALL CAPS (e.g. [REDACTED_NAME_1]). Ignore these placeholders and "
    "respond as if you were receiving a normal prompt. Prompt: "
)


@pytest.mark.parametrize(
    "settings,prompt,expected_prompt,expected_valid,expected_score",
    [
        (
            {},
            "Just a simple prompt",
            "Just a simple prompt",
            True,
            0.0,
        ),  # Prompt without sensitive data
        (
            {"preamble": _preamble, "hidden_names": ["Test LLC"]},
            "Make an SQL insert statement to add a new user to our database. Name is John Doe. My email is test@test.com "
            "but also possible to contact him with hello@test.com email. Phone number is 555-123-4567 and "
            "the IP address is 192.168.1.100. And credit card number is 4567-8901-2345-6789. "
            "He works in Test LLC.",
            "In the following prompt, I am going remove certain information and replace each instance with "
            "sequentially-numbered placeholders in ALL CAPS (e.g. [REDACTED_NAME_1]). "
            "Ignore these placeholders and respond as if you were receiving a normal prompt. "
            "Prompt: Make an SQL insert statement to add a new user to our database. "
            "Name is [REDACTED_PERSON_1]. My email is [REDACTED_EMAIL_ADDRESS_1] but also possible to contact "
            "him with [REDACTED_EMAIL_ADDRESS_2] email. Phone number is [REDACTED_PHONE_NUMBER_1] "
            "and the IP address is [REDACTED_IP_ADDRESS_1]. And credit card number is "
            "[REDACTED_CREDIT_CARD_RE_1]. He works in [REDACTED_CUSTOM_1].",
            False,
            1.0,
        ),  # Exposed name, email, phone number, credit card number and IP
        (
            {"entity_types": ["PERSON"]},
            "Make an SQL insert statement to add a new user to our database. Name is John Doe. E-mail is test@test.com "
            "but also possible to contact him with hello@test.com email. Phone number is 555-123-4567 and "
            "the IP address is 192.168.1.100. And credit card number is 4567-8901-2345-6789. "
            "He works in Test LLC.",
            "Make an SQL insert statement to add a new user to our database. Name is [REDACTED_PERSON_1]. "
            "E-mail is test@test.com but also possible to contact him with hello@test.com email. "
            "Phone number is 555-123-4567 and the IP address is 192.168.1.100. "
            "And credit card number is 4567-8901-2345-6789. He works in Test LLC.",
            False,
            0.85,
        ),  # Exposed name, email, phone number, credit card number and IP but only with PERSON
        (
            {},
            """Given the personal profile of Johnathan Edward Doe:

Full Name: Johnathan Edward Doe.
Date of Birth: April 12, 1990.
Address: 123 Elm Street, Springfield, IL, 62701.
Email: john.doe@laiyer[DOT]ai.
Phone Number: (123) 456-7890.
Educational Background:
    Springfield High School, Graduated in 2008;
    Springfield University, B.Sc. Computer Science, Graduated in 2012.
Employment:
    ABC Tech Solutions, Software Engineer, 2012-2015;
    XYZ Global Systems, Senior Software Developer, 2015-2021.
Social Security Number (SSN): 123-45-6789.
Credit Card: 4111111111111111, Exp: 09/25, CVV: 123.

Please create a summarized version of his resume.""",
            """Given the personal profile of [REDACTED_PERSON_1]:

Full Name: [REDACTED_PERSON_1].
Date of Birth: April 12, 1990.
Address: 123 Elm Street, Springfield, IL, 62701.
Email: [REDACTED_EMAIL_ADDRESS_RE_1].
Phone Number: [REDACTED_PHONE_NUMBER_1].
Educational Background:
    Springfield High School, Graduated in 2008;
    Springfield University, B.Sc. Computer Science, Graduated in 2012.
Employment:
    ABC Tech Solutions, Software Engineer, 2012-2015;
    XYZ Global Systems, Senior Software Developer, 2015-2021.
Social Security Number (SSN): [REDACTED_US_SSN_RE_1].
Credit Card: [REDACTED_CREDIT_CARD_1], Exp: 09/25, CVV: 123.

Please create a summarized version of his resume.""",
            False,
            1.0,
        ),
        (
            {"recognizer": RECOGNIZER_SPACY_EN_PII_FAST},
            """Given the personal profile of Johnathan Edward Doe:

Full Name: Johnathan Edward Doe.
Date of Birth: April 12, 1990.
Address: 123 Elm Street, Springfield, IL, 62701.
Email: john.doe@laiyer[DOT]ai.
Phone Number: (123) 456-7890.
Educational Background:
    Springfield High School, Graduated in 2008;
    Springfield University, B.Sc. Computer Science, Graduated in 2012.
Employment:
    ABC Tech Solutions, Software Engineer, 2012-2015;
    XYZ Global Systems, Senior Software Developer, 2015-2021.
Social Security Number (SSN): 123-45-6789.
Credit Card: 4111111111111111, Exp: 09/25, CVV: 123.

Please create a summarized version of his resume.""",
            """Given the personal profile of [REDACTED_PERSON_1]:

Full Name: [REDACTED_PERSON_1].
Date of Birth: April 12, 1990.
Address: 123 Elm Street, Springfield, IL, 62701.
Email: [REDACTED_EMAIL_ADDRESS_RE_1].
Phone Number: [REDACTED_PHONE_NUMBER_1].
Educational Background:
    Springfield High School, Graduated in 2008;
    Springfield University, B.Sc. Computer Science, Graduated in 2012.
Employment:
    ABC Tech Solutions, Software Engineer, 2012-2015;
    XYZ Global Systems, Senior Software Developer, 2015-2021.
Social Security Number (SSN): [REDACTED_US_SSN_RE_1].
Credit Card: [REDACTED_CREDIT_CARD_1], Exp: 09/25, CVV: 123.

Please create a summarized version of his resume.""",
            False,
            1.0,
        ),  # Use different recognizer
        ({}, "", "", True, 0.0),  # Empty prompt
    ],
)
def test_scan(settings, prompt, expected_prompt, expected_valid, expected_score):
    scanner = Anonymize(Vault(), **settings)
    sanitized_prompt, valid, score = scanner.scan(prompt)
    assert sanitized_prompt == expected_prompt
    assert valid == expected_valid
    assert score == expected_score


def test_patterns():
    pattern_groups = read_json_file(sensitive_patterns_path)

    for group in pattern_groups:
        name = group["name"]

        for example in group["examples"]:
            for expression in group["expressions"]:
                compiled_expression = re.compile(expression)
                assert (
                    compiled_expression.search(example) is not None
                ), f"Test for {name} failed. No match found for example: {example}"
