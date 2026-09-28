import csv
import os

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file if it does not exist."""

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount"
            ])


def load_expenses():
    """Load saved expenses from the CSV file."""

    initialize_file()

    expenses = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "id": int(row["ID"]),
                "date": row["Date"],
                "category": row["Category"],
                "description": row["Description"],
                "amount": float(row["Amount"])
            })

    return expenses


def save_expenses(expenses):
    """Save expenses to the CSV file."""

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Date",
            "Category",
            "Description",
            "Amount"
        ])

        for expense in expenses:
            writer.writerow([
                expense["id"],
                expense["date"],
                expense["category"],
                expense["description"],
                expense["amount"]
            ])