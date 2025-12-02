from storage import read_expenses, write_expenses, init_storage
from core import add_expense, delete_expense, edit_expense, summarize_by_category

DATA_PATH = "data/expenses.csv"

def main():
    init_storage(DATA_PATH)
    
    while True:
        rows = read_expenses(DATA_PATH)
        print("\n(1) Add  (2) List  (3) Summary  (4) Delete  (5) Edit  (0) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            amount = input("Amount: ")
            category = input("Category: ")
            desc = input("Description: ")
            add_expense(rows, date, amount, category, desc)
            write_expenses(DATA_PATH, rows)
            print("Expense added!")

        elif choice == "2":
            for r in rows:
                print(r)

        elif choice == "3":
            y = int(input("Year: "))
            m = int(input("Month (1-12): "))
            print(summarize_by_category(rows, y, m))

        elif choice == "4":
            id_ = int(input("ID to delete: "))
            if delete_expense(rows, id_):
                write_expenses(DATA_PATH, rows)
                print("Deleted!")
            else:
                print("Not found.")

        elif choice == "5":
            id_ = int(input("ID to edit: "))
            field = input("Field (date/amount/category/description): ")
            val = input("New value: ")
            if edit_expense(rows, id_, {field: val}):
                write_expenses(DATA_PATH, rows)
                print("Edited!")
            else:
                print("Not found.")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
