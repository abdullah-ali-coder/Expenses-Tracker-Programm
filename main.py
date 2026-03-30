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
    
    
