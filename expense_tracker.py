import os
import csv
from datetime import datetime
import pandas as pd
import argparse

# Path to the CSV file
file_path = 'data/expenses.csv'

# Check if the CSV file exists and create it if not
if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Description", "Amount"])  # Headers for the CSV file
    print(f"Created {file_path} with headers.")

def load_expenses():
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        # Return an empty DataFrame if the file does not exist
        return pd.DataFrame(columns=['ID', 'Date', 'Description', 'Amount', 'Category'])


def save_expenses(expenses):
    expenses.to_csv(file_path, index=False)

def add_expense(description, amount, category=None):
    expenses = load_expenses()
    new_id = 1 if expenses.empty else expenses['ID'].max() + 1
    new_expense = {
        "ID": new_id,
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Description": description,
        "Amount": amount,
        "Category": category if category else "Uncategorized"
    }
    expenses = expenses.append(new_expense, ignore_index=True)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {new_id})")

def list_expenses():
    expenses = load_expenses()
    if expenses.empty:
        print("No expenses found.")
    else:
        print(expenses.to_string(index=False))

def delete_expense(expense_id):
    expenses = load_expenses()
    if expense_id in expenses['ID'].values:
        expenses = expenses[expenses['ID'] != expense_id]
        save_expenses(expenses)
        print(f"Expense with ID {expense_id} deleted successfully.")
    else:
        print(f"No expense found with ID {expense_id}.")

def update_expense(expense_id, description=None, amount=None, category=None):
    expenses = load_expenses()
    if expense_id in expenses['ID'].values:
        if description:
            expenses.loc[expenses['ID'] == expense_id, 'Description'] = description
        if amount:
            expenses.loc[expenses['ID'] == expense_id, 'Amount'] = amount
        if category:
            expenses.loc[expenses['ID'] == expense_id, 'Category'] = category
        save_expenses(expenses)
        print(f"Expense with ID {expense_id} updated successfully.")
    else:
        print(f"No expense found with ID {expense_id}.")

def summary():
    expenses = load_expenses()
    total = expenses['Amount'].sum()
    print(f"Total expenses: ${total:.2f}")

def summary_by_month(month):
    expenses = load_expenses()
    expenses['Date'] = pd.to_datetime(expenses['Date'])
    filtered = expenses[expenses['Date'].dt.month == month]
    total = filtered['Amount'].sum()
    print(f"Total expenses for month {month}: ${total:.2f}")

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Add expense command
    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('--description', required=True)
    parser_add.add_argument('--amount', type=float, required=True)
    parser_add.add_argument('--category', required=False)

    # List expenses command
    parser_list = subparsers.add_parser('list')

    # Delete expense command
    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('--id', type=int, required=True)

    # Update expense command
    parser_update = subparsers.add_parser('update')
    parser_update.add_argument('--id', type=int, required=True)
    parser_update.add_argument('--description', required=False)
    parser_update.add_argument('--amount', type=float, required=False)
    parser_update.add_argument('--category', required=False)

    # Summary command
    parser_summary = subparsers.add_parser('summary')
    parser_summary.add_argument('--month', type=int, required=False)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.category)
    elif args.command == "summary":
        if args.month:
            summary_by_month(args.month)
        else:
            summary()

if __name__ == "__main__":
    main()