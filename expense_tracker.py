expenses = []

def add_expense():
    description = ""
    category = ""
    amount = -1
    while True:
        try:
            if description == "":
                description = input("Give a description to your expense: \t").strip()

            if category == "":
                category = input("What is the category of the expense?").strip()

            if amount <= 0:
                amount = float(input("Give an amount"))

            if description == "" or category == "" or amount <= 0:
                print("Description and category must be given and amount must be bigger than zero")
                continue
            else:
                break

        except ValueError:
            amount = -1
            print("Give a valid amount")
    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }
    expenses.append(expense)

    print("Expense added successfully")

def show_expenses():
    if not expenses:
        print("There are no expenses")
    else:
        for expense in expenses:
            print(f'{expense["description"]} | {expense["category"]} | {expense["amount"]:.2f}€')

def show_total():
    if not expenses:
        print("There are no expenses")
    else:
        total_amount = 0
        for expense in expenses:
            total_amount += expense["amount"]

        print(f"Total spending: {total_amount:.2f}€")

def show_category_total():
    found = False
    wished_category = input("Enter a category").strip().lower()
    total = 0.0
    for expense in expenses:
        if wished_category == expense["category"].lower():
            total += expense["amount"]
            found = True
    if found:
        print(f"Your total amount in this category {total:.2f}€")
    else:
        print("No expenses found in this category")

def delete_expense():
    if not expenses:
        print("There are no expenses to delete")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f'{number}) {expense["description"]} | {expense["category"]} | {expense["amount"]:.2f}€')

    while True:
        try:
            selected_expense = int(input("Please give the number of the expense that you want to delete."))
            if selected_expense <= 0 or selected_expense > len(expenses):
                print("Please give a valid number")
            else:
                expenses.pop(selected_expense - 1)
                print(f"Selected expense removed successfully")
                break
        except ValueError:
            print("Please give a valid number")


while True:

    print("1. Add an expense\n2. Show all expenses\n3. Show total spending\n4. Show spending by category"
            "\n5. Delete an expense\n6. Exit")

    instruction = input().strip()

    if instruction == "1":
        add_expense()

    elif instruction == "2":
        show_expenses()

    elif instruction == "3":
        show_total()

    elif instruction == "4":
        show_category_total()

    elif instruction =="5":
        delete_expense()

    elif instruction == "6":
        print(f"Exiting")
        break

    else:
        print("Please give a valid number")

