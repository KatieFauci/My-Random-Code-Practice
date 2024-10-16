import json

def make_change(amount_owed):
    if (amount_owed < 0):
        message = {"Message": "Customer Still Owes Money, No Change Made"}
        return json.dumps(message)    
    else:
        change = {
            "Dollars":0,
            "Quarters":0,
            "Dimes":0,
            "Nickels":0,
            "Pennies":0
        }

        while amount_owed >= 1:
            amount_owed = round(amount_owed - 1,2)
            change['Dollars'] += 1

        while amount_owed >= .25:
            amount_owed = round(amount_owed - .25,2)
            change['Quarters'] += 1

        while amount_owed >= .10:
            amount_owed = round(amount_owed - .10,2)
            change["Dimes"] += 1

        while amount_owed >= .05:
            amount_owed = round(amount_owed - .05,2)
            change['Nickels'] += 1

        while amount_owed >= .01:
            amount_owed = round(amount_owed - .01,2)
            change["Pennies"] += 1

        return json.dumps(change, indent=4)
    


def calculate_cost(values):
    cost = {
        "Total":0
    }
    for v in values:
        cost["Total"] += v
    
    cost["Total"] = round(cost["Total"],2)

    return json.dumps(cost, indent=4)



def calculate_change(cost, amount_paid):
    change = {
        "Change": round(amount_paid - cost, 2)
    }

    if change["Change"] < 0:
        message = {"Message": "Customer Still Owes Money, No Change Given"}
        return json.dumps(message)
    else: 
        return json.dumps(change, indent=4)



def calculate_ammount_owed(cost, amount_paid):
    owed = {
        "Amount_Owed": round(cost - amount_paid,2)
    }

    if owed["Amount_Owed"] < 0:
        message = {"Message":"Amount Paid In Full"}
        return json.dumps(message)
    else:
        return json.dumps(owed, indent=4)
             
    




#result = calculate_cost([])

#result = calculate_ammount_owed(cost=25.7, amount_paid=12)

result = calculate_change(cost=13.7, amount_paid=15)

result = make_change(round(1.3,2))



print(result)
