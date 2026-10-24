"""InternCircle Project 03: a command-line expense tracker backed by CSV."""
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

FILE = Path(__file__).with_name("expenses.csv")
FIELDS = ["date", "category", "description", "amount"]
CATEGORIES = ["Food", "Travel", "Study", "Bills", "Fun"]


def ensure_file():
    """Create the CSV file and column headers the first time it is needed."""
    if not FILE.exists() or FILE.stat().st_size == 0:
        with FILE.open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=FIELDS).writeheader()


def load_expenses():
    ensure_file()
    with FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expense(expense):
    ensure_file()
    with FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(expense)


def read_date():
    while True:
        value = input("Date (YYYY-MM-DD): ").strip()
        try:
            date = datetime.strptime(value, "%Y-%m-%d")
            if date.strftime("%Y-%m-%d") != value:
                raise ValueError
            return value
        except ValueError:
            print("Invalid date. Example: 2026-10-24")


def read_category():
    while True:
        print("Categories: " + ", ".join(CATEGORIES))
        value = input("Category: ").strip().title()
        if value in CATEGORIES:
            return value
        print("Please choose a listed category.")


def read_amount():
    while True:
        try:
            amount = float(input("Amount (INR): ").strip())
            if not (0 < amount < float("inf")):
                raise ValueError
            return amount
        except ValueError:
            print("Enter a valid positive amount.")


def add_expense():
    date = read_date()
    category = read_category()
    while True:
        description = input("Description: ").strip()
        if description:
            break
        print("Description cannot be empty.")
    amount = read_amount()
    save_expense({"date": date, "category": category,
                  "description": description, "amount": f"{amount:.2f}"})
    print("Expense saved successfully!\n")


def show_expenses(rows):
    if not rows:
        print("No matching expenses.\n")
        return
    print(f"{'Date':<12} {'Category':<10} {'Description':<25} {'Amount (INR)':>14}")
    print("-" * 65)
    for item in rows:
        print(f"{item['date']:<12} {item['category']:<10} "
              f"{item['description'][:25]:<25} {float(item['amount']):>14.2f}")
    print(f"{'TOTAL':>52} {sum(float(x['amount']) for x in rows):>12.2f}\n")


def filter_expenses():
    print("1. By category\n2. By month")
    mode = input("Choose filter: ").strip()
    rows = load_expenses()
    if mode == "1":
        category = read_category()
        show_expenses([x for x in rows if x["category"].lower() == category.lower()])
    elif mode == "2":
        while True:
            month = input("Month (YYYY-MM): ").strip()
            try:
                datetime.strptime(month, "%Y-%m")
                if len(month) == 7:
                    break
            except ValueError:
                pass
            print("Invalid month. Example: 2026-10")
        show_expenses([x for x in rows if x["date"][:7] == month])
    else:
        print("Invalid filter choice.\n")


def show_summary():
    rows = load_expenses()
    if not rows:
        print("No expenses recorded yet.\n")
        return
    totals = defaultdict(float)
    for item in rows:
        totals[item["category"]] += float(item["amount"])
    print("\nSPENDING BY CATEGORY (INR)")
    print("-" * 33)
    for category, total in sorted(totals.items()):
        print(f"{category:<18} {total:>12.2f}")
    print("-" * 33)
    print(f"{'GRAND TOTAL':<18} {sum(totals.values()):>12.2f}")
    biggest = max(rows, key=lambda x: float(x["amount"]))
    print(f"Largest expense: {biggest['description']} "
          f"({biggest['category']}) - INR {float(biggest['amount']):.2f}\n")


def main():
    ensure_file()
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add expense\n2. View all expenses\n3. Filter expenses")
        print("4. Category summary\n5. Quit")
        choice = input("Choose 1-5: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses(load_expenses())
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
