# Personal Expense Tracker with CSV

InternCircle Python Programming — Project 03.

A beginner-friendly command-line expense tracker built using Python's standard `csv` and `datetime` modules. It saves data between runs in `expenses.csv`.

## Features
- Add an expense with a validated date, category, description, and positive amount
- View all expenses in a table
- Filter records by category or `YYYY-MM` month
- Show total expenses by category, a grand total, and the largest expense
- Automatically create an empty `expenses.csv` with the required headers if missing

## Run
1. Download `main.py` and `expenses.csv` into the same folder.
2. Run `python main.py` with Python 3.10 or newer.
3. Choose menu items 1–5. Try adding an expense, then exit and restart to verify persistence.

The included `expenses.csv` has **12 invented entries across September and October 2026**. These are demonstration values, not personal financial data. Replace or extend them with your own invented entries before submission.

## CSV example
```csv
date,category,description,amount
2026-09-04,Food,Lunch,120.00
2026-10-02,Travel,Bus fare,35.00
```

## Suggested tests
- Add an expense, quit, then reopen and check that it still exists.
- Try a bad date (`2026-02-30`), a negative amount, an unlisted category and an empty description.
- Filter by Food and by 2026-10.
- Check category totals against rows in the CSV.

## Implementation note
A common CSV issue on Windows is blank lines between rows. This implementation uses `newline=""` for both CSV reading and writing to avoid that issue.

## Project guide
The project guide also asks for a **short note on a problem you actually fixed**. Describe your own debugging experience in the InternCircle submission notes; don't claim a fix you haven't personally made.
