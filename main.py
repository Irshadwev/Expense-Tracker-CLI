# Here is Total Expense is Calculate
def TotalExpense():
    total_expense = 0
    expense = [
            int(input("Enter the Food Expense: ")),
            int(input("Enter the Transport Expense: ")),
            int(input("Enter the Internet Expense: ")),
            int(input("Enter the others Expense: "))
                   ]
    for i in expense:
        total_expense += i
    return total_expense

# Here Expense Category logic build
def ExpenseCatogory(total_expense):
    if(total_expense > 10000):
        return "High Spending"
    elif (total_expense > 5000):
        return "Moderate Spending"
    else:
        return "Low Spending"

total_expense = TotalExpense()
expensecatogory = ExpenseCatogory(total_expense)

print(f"Total Expense {total_expense}")
print(f"Your spending category is: {expensecatogory}")