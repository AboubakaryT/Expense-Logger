def expenseLogger():
    #Loops until user outouput n
    expenses = 0
    while True:
        #Ask for user item
        expenseDesc = input("Enter expense description: ")
        #Ask for price
        expense = float(input("Enter amount: "))
        addOn = input("Add another? (y/n): ")
        expenses += expense
        if addOn == 'n':
            print(expenses)
            break

            

expenseLogger()
            



