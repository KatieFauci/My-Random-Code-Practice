import json

budget_file = "my_budget.json"

def setup_new_budget(income, rent, food, electric, internet, gas=0, misc=0):
    '''
    Description: setup a new budget with the base budget items, overwrites any budget that has already been setup

    Args:
      income (number): users monthly income
      rent (number): users monthly rent (could also be mortgage or whatever cost for living space)
      food (number): monthly cost of food
      electric (number): monthly cost of electric bill
      internet (number): monthly cost of internet bill
      gas (number): amount spent on gass per month (defaults to 0 if not specified)
      misc (number): amount spent on miscelanious things per month (defaults to 0 if not specified) 
    '''
    budget = {
        "Expenses":{
            "Rent": rent,
            "Food": food,
            "Electric": electric,
            "Internet": internet,
            "Gas": gas,
            "Misc": misc
        },
        "Total_Expenses":0,
        "Income": income,
        "Available_Funds":0
    }

    total_exp = 0
    for item in budget["Expenses"]:
        total_exp += budget["Expenses"][item]


    budget["Total_Expenses"] = total_exp
    budget["Available_Funds"] = budget["Income"] - budget["Total_Expenses"]

    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=4)

    return json.dumps(budget, indent=4)
    

def add_new_expense(expense_name, amount):
    '''
    Description: Adds a new expense to the budget, returns the updated budget

    Args:
      expense_name (number): The name of the new expense
      amount (number): the cost of the new expense
    '''
    with open(budget_file, 'r') as f:
        budget = json.load(f)


    budget["Expenses"][expense_name] = amount

    total_exp = 0
    for item in budget["Expenses"]:
        total_exp += budget["Expenses"][item]


    budget["Total_Expenses"] = total_exp
    budget["Available_Funds"] = budget["Income"] - budget["Total_Expenses"]

    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=4)

    return json.dumps(budget, indent=4)


def check_for_funds(amount):
    '''
    Description: Determines if the user can afford to spend a specified amount but does not add the item as an expense

    Args:
      amount (number): the amount they want to spend
    '''
    with open(budget_file, 'r') as f:
        budget = json.load(f)

    new_available_funds = budget["Available_Funds"] - amount

    if new_available_funds > 0:
        message = {"can_afford":True,
                   "projected_remaining_funds":new_available_funds}
    else:    
        message = {
            "can_afford":False,
            "projected_remaining_funds":new_available_funds
        }

    return message

    
def remove_expense(expense_name):
    '''
    Description: removes an expense from the budget, returns the updated budget

    Args:
      expense_name (number): The name of the expense being removed
    '''
    with open(budget_file, 'r') as f:
        budget = json.load(f)

    del budget["Expenses"][expense_name]

    total_exp = 0
    for item in budget["Expenses"]:
        total_exp += budget["Expenses"][item]

    budget["Total_Expenses"] = total_exp
    budget["Available_Funds"] = budget["Income"] - budget["Total_Expenses"]

    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=4)

    return json.dumps(budget, indent=4)


def get_my_budget():
    '''
    Description: Returns the current budget details
    '''
    with open(budget_file, 'r') as f:
        budget = json.load(f)

    return json.dumps(budget, indent=4)

def modify_expense(expense_name, amount):
    '''
    Description: modifies an existing expense. returns the updated budget

    Args:
      expense_name (string): The name of the expense being modified
      amount (number): The new amount for the expense
    '''

    with open(budget_file, 'r') as f:
        budget = json.load(f)

    budget["Expenses"][expense_name] = amount

    total_exp = 0
    for item in budget["Expenses"]:
        total_exp += budget["Expenses"][item]

    budget["Total_Expenses"] = total_exp
    budget["Available_Funds"] = budget["Income"] - budget["Total_Expenses"]

    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=4)

    return json.dumps(budget, indent=4)


def update_income(new_income):
    '''
    Description: updates the income in the budget, returns the updated budget

    Args:
      new_income (number): the value the income is being update to.
    '''
    with open(budget_file, 'r') as f:
        budget = json.load(f)

    budget["Income"] = new_income

    total_exp = 0
    for item in budget["Expenses"]:
        total_exp += budget["Expenses"][item]

    budget["Total_Expenses"] = total_exp
    budget["Available_Funds"] = budget["Income"] - budget["Total_Expenses"]

    with open(budget_file, 'w') as f:
        json.dump(budget, f, indent=4)

    return json.dumps(budget, indent=4)

#print(setup_new_budget(income=3200, rent=1500, food=200, electric=60, internet=80))

#print(add_new_expense(expense_name="car loan", amount=500))

#print(check_for_funds(amount=590))

#print(remove_expense(expense_name="Misc"))

#print(get_my_budget())

#print(modify_expense(expense_name="Gas", amount=190))

#print(update_income(3500))