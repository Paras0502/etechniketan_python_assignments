import csv
import datetime
import os

class Expense:
    def __init__(self, expense_id, title, amount, category, date):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()
        self.next_id = self.get_next_id()

    def get_next_id(self):
        if not self.expenses:
            return 101
        return max(exp.expense_id for exp in self.expenses) + 1

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.expenses.append(
                        Expense(int(row["ID"]), row["Title"], float(row["Amount"]), row["Category"], row["Date"])
                    )

    def save_expenses(self):
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ["ID", "Title", "Amount", "Category", "Date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow({
                    "ID": exp.expense_id,
                    "Title": exp.title,
                    "Amount": exp.amount,
                    "Category": exp.category,
                    "Date": exp.date
                })

    def add_expense(self, title, amount, category, date=None):
        # Internal validation to ensure class integrity
        if not title or not title.strip():
            print("[ERROR]: Title cannot be empty.")
            return
        if not category or not category.strip():
            print("[ERROR]: Category cannot be empty.")
            return
        if amount < 0:
            print("[ERROR]: Amount cannot be negative.")
            return
        if date:
            try:
                datetime.datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                print("[ERROR]: Invalid date format. Use DD-MM-YYYY.")
                return

        if not date:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"--> [SYSTEM]: Blank detected. Auto-assigned current timestamp date: {current_date}")
            date = current_date
        expense = Expense(self.next_id, title, amount, category, date)
        self.expenses.append(expense)
        print(f"Expense Added Successfully! (ID: {self.next_id})")
        self.next_id += 1
        self.save_expenses()

    def view_expenses(self):
        print("\n=== ALL EXPENSES ===")
        if not self.expenses:
            print("No expenses available.")
            return

        print("{:<5} {:<20} {:<10} {:<15} {:<12}".format("ID", "Title", "Amount", "Category", "Date"))
        for exp in self.expenses:
            print("{:<5} {:<20} {:<10.2f} {:<15} {:<12}".format(exp.expense_id, exp.title, exp.amount, exp.category, exp.date))

    def find_expense_by_id(self, expense_id):
        for exp in self.expenses:
            if exp.expense_id == expense_id:
                return exp
        return None

    def search_expense(self, expense_id):
        exp = self.find_expense_by_id(expense_id)
        if exp:
            print("\n--- SEARCH RESULT ---")
            print("{:<5} {:<20} {:<10} {:<15} {:<12}".format("ID", "Title", "Amount", "Category", "Date"))
            print("{:<5} {:<20} {:<10.2f} {:<15} {:<12}".format(exp.expense_id, exp.title, exp.amount, exp.category, exp.date))
        else:
            print("[ERROR]: Expense not found.")

    def update_expense(self, expense_id, title=None, amount=None, category=None, date=None):
        exp = self.find_expense_by_id(expense_id)
        if not exp:
            # This check is a safeguard. The main loop should prevent this.
            print("[ERROR]: Expense with that ID not found.")
            return

        # Internal validation for provided fields
        if title is not None and not title.strip():
            print("[ERROR]: Title cannot be empty.")
            return
        if category is not None and not category.strip():
            print("[ERROR]: Category cannot be empty.")
            return
        if amount is not None and amount < 0:
            print("[ERROR]: Amount cannot be negative.")
            return
        if date is not None:
            try:
                datetime.datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                print("[ERROR]: Invalid date format. Use DD-MM-YYYY.")
                return

        if title:
            exp.title = title
        if amount is not None:
            exp.amount = amount
        if category:
            exp.category = category
        if date:
            exp.date = date

        print("Expense updated successfully!")
        self.save_expenses()

    def delete_expense(self, expense_id):
        exp = self.find_expense_by_id(expense_id)
        if exp:
            self.expenses.remove(exp)
            print("Expense deleted successfully!")
            self.save_expenses()
        else:
            print("[ERROR]: Expense with that ID not found.")

    def summary(self):
        print("\n========== Expense Summary ==========")
        total = sum(exp.amount for exp in self.expenses)
        print(f"Total Expense : ₹{total:.2f}")
        print(f"Total Expenses : {len(self.expenses)}")

        categories = {}
        for exp in self.expenses:
            categories[exp.category] = categories.get(exp.category, 0) + exp.amount

        print("\nCategory-wise Expense:")
        for cat, amt in categories.items():
            print(f"{cat:<15}: ₹{amt:.2f}")
        print("\n==============================")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. View Summary Metrics")
        print("7. Exit & Save Data")
        choice = input("Choose option (1-7): ")
        if choice == "1":
            while True:
                title = input("Enter Expense Title: ").strip()
                if title:
                    break
                print("[ERROR]: Title cannot be empty.")

            while True:
                amount_str = input("Enter Expense Amount: ")
                try:
                    amount = float(amount_str)
                    if amount < 0:
                        print("[ERROR]: Amount cannot be negative.")
                    else:
                        break
                except ValueError:
                    print("[ERROR]: Invalid monetary value. Please enter a valid numerical decimal amount.")

            while True:
                category = input("Enter Expense Category: ").strip()
                if category:
                    break
                print("[ERROR]: Category cannot be empty.")

            while True:
                date_str = input("Enter Expense Date (DD-MM-YYYY) or leave blank for today: ")
                if not date_str:
                    date = None
                    break
                try:
                    datetime.datetime.strptime(date_str, "%d-%m-%Y")
                    date = date_str
                    break
                except ValueError:
                    print("[ERROR]: Invalid date format. Use DD-MM-YYYY.")
            tracker.add_expense(title, amount, category, date)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            try:
                expense_id = int(input("Enter Expense ID: "))
                tracker.search_expense(expense_id)
            except ValueError:
                print("[ERROR]: Invalid ID.")
        elif choice == "4":
            try:
                expense_id = int(input("Enter Expense ID to update: "))
                if not tracker.find_expense_by_id(expense_id):
                    print("[ERROR]: Expense with that ID not found.")
                    continue

                title = input("New Title (leave blank to skip): ").strip()

                amount = None
                while True:
                    amount_str = input("New Amount (leave blank to skip): ")
                    if not amount_str:
                        break
                    try:
                        amount = float(amount_str)
                        if amount < 0:
                            print("[ERROR]: Amount cannot be negative.")
                            amount = None
                        else:
                            break
                    except ValueError:
                        print("[ERROR]: Invalid monetary value. Please enter a valid numerical decimal amount.")

                category = input("New Category (leave blank to skip): ").strip()

                date = None
                while True:
                    date_str = input("New Date (DD-MM-YYYY, leave blank to skip): ")
                    if not date_str:
                        break
                    try:
                        datetime.datetime.strptime(date_str, "%d-%m-%Y")
                        date = date_str
                        break
                    except ValueError:
                        print("[ERROR]: Invalid date format. Use DD-MM-YYYY.")

                tracker.update_expense(expense_id, title or None, amount, category or None, date or None)
            except ValueError:
                print("[ERROR]: Invalid ID.")
        elif choice == "5":
            try:
                expense_id = int(input("Enter Expense ID to delete: "))
                expense = tracker.find_expense_by_id(expense_id)

                if not expense:
                    print("[ERROR]: Expense with that ID not found.")
                    continue

                print("\n--- Expense to be Deleted ---")
                print("{:<5} {:<20} {:<10} {:<15} {:<12}".format("ID", "Title", "Amount", "Category", "Date"))
                print("{:<5} {:<20} {:<10.2f} {:<15} {:<12}".format(expense.expense_id, expense.title, expense.amount, expense.category, expense.date))

                confirm = input("\nAre you sure you want to delete this expense? (Y/N): ").strip().lower()
                if confirm == 'y':
                    tracker.delete_expense(expense_id)
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("[ERROR]: Invalid ID.")
        elif choice == "6":
            tracker.summary()
        elif choice == "7":
            tracker.save_expenses()
            print("Thank You!")
            break
        else:
            print("[ERROR]: Invalid option.")

if __name__ == "__main__":
    main()
