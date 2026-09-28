from datetime import datetime


def validate_date(date):
    """Check whether the date is in DD-MM-YYYY format."""

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False


def validate_amount(amount):
    """Check whether the amount is a positive number."""

    try:
        value = float(amount)

        if value <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_category(category):
    """Check whether the category is not empty."""

    return bool(category.strip())


def validate_description(description):
    """Check whether the description is not empty."""

    return bool(description.strip())