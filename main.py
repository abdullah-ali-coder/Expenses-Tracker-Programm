from database import load_expenses, save_expenses

expenses = load_expenses()

def add_expenses():
    description = input("Enter expenses description: ")
    date = input("Enter expenses date (YYYY-MM-DD): ")
    try:
        amount = float(input("Enter expenses amount: "))
    except ValueError:
        print("Invalid amount!\n")
        return

    expense = {
        "description": description,
        "date": date,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.\n")
        return
    
    print("\nList of Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['description']} : {expense['amount']}")
    print("")

def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()