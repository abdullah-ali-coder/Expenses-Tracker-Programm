expenses =[]

def add_expenses():
    description = input("Enter expenses description: ")
    date = input("Enter expenses date (YYYY-MM-DD): ")
    amount = float(input("Enter expenses amount: "))


    expense={
        "description": description,
        "date": date,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet. \n")
        return
    
    print("\nList of Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['description']} : {expense['amount']}")
        print("")



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