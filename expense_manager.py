from storage import save_expenses
from validation import (
    validate_date,
    validate_amount,
    validate_category,
    validate_description
)


def generate_id(expenses):
    """Generate a unique ID for a new expense."""

    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def add_expense(expenses):
    """Add a new expense."""

    print("\n--- Add New Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")

    if not validate_date(date):
        print("Invalid date format.")
        return

    category = input("Enter category: ")

    if not validate_category(category):
        print("Category cannot be empty.")
        return

    description = input("Enter description: ")

    if not validate_description(description):
        print("Description cannot be empty.")
        return

    amount = input("Enter amount: ₹")

    if not validate_amount(amount):
        print("Invalid amount.")
        return

    expense = {
        "id": generate_id(expenses),
        "date": date,
        "category": category.title(),
        "description": description,
        "amount": float(amount)
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    """Display all expenses."""

    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    print("-" * 80)

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<25}"
        f"{'Amount':>10}"
    )

    print("-" * 80)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"₹{expense['amount']:>9.2f}"
        )

    print("-" * 80)


def update_expense(expenses):
    """Update an existing expense."""

    print("\n--- Update Expense ---")

    if not expenses:
        print("No expenses available.")
        return

    try:
        expense_id = int(input("Enter expense ID to update: "))

    except ValueError:
        print("Invalid ID.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:

            print("\nLeave a field blank to keep the old value.")

            date = input(
                f"Date [{expense['date']}]: "
            )

            category = input(
                f"Category [{expense['category']}]: "
            )

            description = input(
                f"Description [{expense['description']}]: "
            )

            amount = input(
                f"Amount [{expense['amount']}]: "
            )

            if date:

                if validate_date(date):
                    expense["date"] = date

                else:
                    print("Invalid date.")
                    return

            if category:
                expense["category"] = category.title()

            if description:
                expense["description"] = description

            if amount:

                if validate_amount(amount):
                    expense["amount"] = float(amount)

                else:
                    print("Invalid amount.")
                    return

            save_expenses(expenses)

            print("Expense updated successfully!")
            return

    print("Expense ID not found.")


def delete_expense(expenses):
    """Delete an expense."""

    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses available.")
        return

    try:
        expense_id = int(input("Enter expense ID to delete: "))

    except ValueError:
        print("Invalid ID.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)
            save_expenses(expenses)

            print("Expense deleted successfully!")
            return

    print("Expense ID not found.")