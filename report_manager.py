def total_expenses(expenses):
    """Calculate and display total expenses."""

    print("\n--- Total Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(f"Total spent: ₹{total:.2f}")


def category_summary(expenses):
    """Display expenses category-wise."""

    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:

        category = expense["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += expense["amount"]

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")


def highest_expense(expenses):
    """Find and display the highest expense."""

    print("\n--- Highest Expense ---")

    if not expenses:
        print("No expenses found.")
        return

    highest = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print(f"Category    : {highest['category']}")
    print(f"Description : {highest['description']}")
    print(f"Amount      : ₹{highest['amount']:.2f}")


def monthly_summary(expenses):
    """Display monthly expense summary."""

    print("\n--- Monthly Summary ---")

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:

        # Extract month and year from DD-MM-YYYY
        month = expense["date"][3:]

        if month not in summary:
            summary[month] = 0

        summary[month] += expense["amount"]

    for month, amount in summary.items():
        print(f"{month} : ₹{amount:.2f}")