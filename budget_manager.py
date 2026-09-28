def set_budget():
    """Set the monthly budget."""

    print("\n--- Set Monthly Budget ---")

    try:
        budget = float(input("Enter monthly budget: ₹"))

        if budget <= 0:
            print("Budget must be greater than zero.")
            return None

        print(f"Monthly budget set to ₹{budget:.2f}")

        return budget

    except ValueError:
        print("Invalid budget amount.")


def check_budget(expenses, budget):
    """Check spending against the monthly budget."""

    print("\n--- Budget Status ---")

    if budget is None:
        print("Please set a budget first.")
        return

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    remaining = budget - total

    print(f"Budget      : ₹{budget:.2f}")
    print(f"Total Spent : ₹{total:.2f}")
    print(f"Remaining   : ₹{remaining:.2f}")

    if remaining < 0:
        print("Warning: You have exceeded your budget!")

    else:
        print("You are within your budget.")