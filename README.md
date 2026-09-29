# Personal Expense Tracker

## 1. Project Overview

Personal Expense Tracker is a Python-based application designed to help users
record, manage, and analyze their personal expenses.

The application provides a simple menu-driven interface through which users
can add, view, update, and delete expenses. It also provides budget management
and expense reporting features.

Expense data is stored in a CSV file so that records can be saved and loaded
when the application is used again.

## 2. Features

- Add a new expense
- View all expenses
- Update an existing expense
- Delete an expense
- Set a monthly budget
- Check budget status
- Calculate total expenses
- View category-wise expenses
- View monthly expense summary
- Find the highest expense
- Store expense data in a CSV file
- Validate user input
- Handle invalid input and errors

## 3. Functional Modules

### Expense Management

The Expense Management module handles:

- Adding expenses
- Viewing expenses
- Updating expenses
- Deleting expenses

### Budget Management

The Budget Management module handles:

- Setting a monthly budget
- Checking the budget
- Monitoring spending against the budget

### Reports and Analytics

The Report Management module provides:

- Total expense calculation
- Category-wise expense summary
- Monthly expense summary
- Highest expense identification

### Data Storage

The Storage module manages reading and writing expense records using a CSV
file.

### Validation

The Validation module checks user inputs such as dates, amounts, categories,
and descriptions.

## 4. Technologies Used

- Python
- CSV
- Visual Studio Code
- Git
- GitHub

## 5. Project Structure

```text
Personal-Expense-Tracker/
│
├── docs/
│   ├── flowchart.png
│   ├── architecture.png
│   ├── use_case.png
│   ├── sequence.png
│   ├── class_diagram.png
│   └── er_diagram.png
│
├── main.py
├── expense_manager.py
├── budget_manager.py
├── report_manager.py
├── storage.py
├── validation.py
├── test_expense_tracker.py
├── expenses.csv
├── README.md
└── statement.md
```

## 6. How to Run the Project

### Step 1: Open the Project

Open the `Personal-Expense-Tracker` folder in Visual Studio Code.

### Step 2: Open the Terminal

In Visual Studio Code, select:

```text
Terminal → New Terminal
```

### Step 3: Run the Application

Use the following command:

```bash
python main.py
```

The Personal Expense Tracker menu will then be displayed.

## 7. Testing

The project contains a test file named:

```text
test_expense_tracker.py
```

Run the tests using:

```bash
python test_expense_tracker.py
```

The testing and validation process checks important inputs and project
functionality.

## 8. Data Storage

Expense records are stored in:

```text
expenses.csv
```

The CSV file stores expense information used by the application.

## 9. Documentation and Design Diagrams

The `docs` folder contains the following design diagrams:

- Flowchart / Workflow Diagram
- System Architecture Diagram
- Use Case Diagram
- Sequence Diagram
- Class Diagram
- ER Diagram

## 10. Error Handling and Validation

The application validates user input and handles invalid entries such as:

- Invalid dates
- Invalid amounts
- Invalid expense IDs
- Empty categories
- Empty descriptions
- Invalid menu choices

## 11. Future Enhancements

Possible future improvements include:

- Graphical User Interface
- Expense charts and visualizations
- Database integration
- User authentication
- Exportable reports
- Automated monthly reports
