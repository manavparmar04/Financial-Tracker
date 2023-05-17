""" Problem: Ever since university began, I've been having a hard time keep track of my money because there are
purchases I make every day, some little and some big and I forget to budget myself. Every morning I'd buy Tim Hortons
because it is cheap BUT, overtime the amount starts to build up and on top of that more expenses I could/ make
throughout the day. To help me with this problem, I made a financial tracker. This will allow me to plug in all of my
expenses and being able to total and average my spending.



"""


def add_expense(expenses, costs):
    expense = ""    # Empty quotes
    while expense != "proceed":  # If inside the empty quotes is the typed "proceed", the while loop ends and will be
        # brought to the menu
        expense = input("What was the purchase that was made? ")
        expenses.append(expense)
        # The expense inputted by the user will be appended to the empty expenses list
        cost = float(input("What was the cost of the purchase that was made? "))
        costs.append(cost)
        # The cost inputted by the user will be appended to the empty costs list
        print("Your expense and cost have been added to final tally")
        # Basic message to confirm that the expense and cost have been added to lists
        proceed = input("Type 'proceed' when you'd like to continue ")
        # As said if expense = "proceed", the while loop ends and therefore will bring you to the main menu again
        if proceed == "proceed":
            break
        else:
            continue

        pass


def remove_expense(expenses, costs):
    expense = "" # Empty quote
    while expense != "proceed":  # Whilo loop ends if the user inputs proceed
        remove_e = input("What is the expense you want to remove from your expenses? ")
        for i in range(len(expenses)):
            if remove_e == expenses[i]: # Checks to see what the cost of the expense the user wants to be removed
                costs.pop(i) # Pop takes the index value of the parameter
        expenses.remove(remove_e) # Once the expense has been removed, the cost of the same index will also be removed

        print("Your expense and cost have been removed from final tally ")
        proceed = input("Type 'proceed to continue ")
        if proceed == "proceed":
            break
        else:
            continue
    # While loop ends when the user types "proceed" as said above
    pass


def total(costs):
    sumOfCosts = sum(costs) # Using the sum function to calulate the sum
    print("The total costs for all of your expenses ", sumOfCosts)
    # Takes the values from the costs and add them all together
    pass


def list_expenses(expenses):
    print("These are the list of your expenses:", expenses) # message out putting the list of your expenses
    # Simply just being able to go over your list of expenses by printing the list of expenses
    pass


def average(expenses, costs):
    avg = sum(costs) / len(expenses)
    print("The average you have spent is: ", avg)  # Mesage outputting the average of the user spending
    # Taking the sum of the costs and divided it by the length of the expenses give you the average sum


def exit_program():
    print("Thank you for using financial tracker!")
    return False
# Once returned false, the main while loop ends and therefore exits you out of the program as intended
    pass


def menu():  # This is the main function of the program
    # These are empty lists and will be used based off the users inputs.
    expenses = []
    # Expenses will be the name of what the user has paid, this could be an item, food, mortgage etc#
    costs = []
    # Costs will be what the user has paid and inputted, and will give total
    menuRunning: bool = True  # Setting menuRunning to True
    while menuRunning:  # While loop will run until the program returns false, that's when the loop will end
        # Below are the different options in the menu
        print()
        print("[1] Add an expense")  # Gathering the expenses whill be  appended to the expenses list and will also
        # append cost
        print("[2] Remove an expense")  # Removing from your expenses which will pop from the expenses list
        print("[3] Total expense")  # Will calulate the sum from the costs list
        print("[4] List of your expenses")  # Giving an overview of the expenses the user has inputted
        print("[5] Average cost of your expenses")  # Averaging the costs
        print("[6] exit program")  # Stopping the loop of the program

        option = int(input("Please select the following number you would like to proceed with "))
        # Giving the user to decide which part of the program they want to use, and easy to follow as they are numbered
        if option == 6:
            exit_program()
            menuRunning = False
        # End of program, set at the top so that it will stop once after the user has typed 6
        elif option == 1:
            add_expense(expenses, costs)
            # If typed "1", user will be able to input there expenses
        elif option == 2:
            remove_expense(expenses, costs)
            # If typed "2, user will be given the chance to remove any of their expenses and cost of that expense
            # would be removed too
        elif option == 3:
            total(costs)
            # Overview of your total sum from the expenses inputted by the user
        elif option == 4:
            list_expenses(expenses)
            # An overview of your expenses
        elif option == 5:
            average(expenses, costs)
            # The average of how much the user has spent
        elif option == 6:
            menuRunning = exit_program()
            # program ends


        else:
            print("Input not valid, please try again")
            ''' If the user types anything else besides the numbers from the main menu, they will be redirected to 
            the menu screen
            '''


menu()  # Calling the main function
