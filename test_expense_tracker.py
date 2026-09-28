from validation import (
    validate_date,
    validate_amount,
    validate_category,
    validate_description
)


def test_valid_date():
    assert validate_date("29-09-2026") is True


def test_invalid_date():
    assert validate_date("2026-09-29") is False


def test_valid_amount():
    assert validate_amount("500") is True


def test_invalid_amount():
    assert validate_amount("-100") is False


def test_valid_category():
    assert validate_category("Food") is True


def test_empty_category():
    assert validate_category("") is False


def test_valid_description():
    assert validate_description("Lunch") is True


def test_empty_description():
    assert validate_description("") is False


print("All validation tests completed successfully!")