from storage import load_expenses
from expense_manager import (
    add_expense,
    view_expenses,
    update_expense,
    delete_expense
)
from budget_manager import (
    set_budget,
    check_budget
)
from report_manager import (
    total_expenses,
    category_summary,
    highest_expense,
    monthly_summary
)


def display_menu():
    """Display the main menu."""

    print("\n")
    print("=" * 45)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 45)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Set Monthly Budget")
    print("6. Check Budget")
    print("7. Total Expenses")
    print("8. Category Summary")
    print("9. Monthly Summary")
    print("10. Highest Expense")
    print("11. Exit")

    print("=" * 45)


def main():

    # Load previously saved expenses
    expenses = load_expenses()

    # Store monthly budget
    budget = None

    print("\nWelcome to Personal Expense Tracker!")

    while True:

        display_menu()

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            update_expense(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            budget = set_budget()

        elif choice == "6":
            check_budget(expenses, budget)

        elif choice == "7":
            total_expenses(expenses)

        elif choice == "8":
            category_summary(expenses)

        elif choice == "9":
            monthly_summary(expenses)

        elif choice == "10":
            highest_expense(expenses)

        elif choice == "11":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("\nInvalid choice!")
            print("Please enter a number from 1 to 11.")


# Start the program
if __name__ == "__main__":
    main()