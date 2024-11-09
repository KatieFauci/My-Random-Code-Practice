import json
import os


list_file = 'My_Grocery_Lists.json'

def create_new_list(list_name):
    '''
    Description: Creates a new grocery list
    
    Args:
      list_name (string): The name of the list to be created
    '''
    if not os.path.exists(list_file):
        # Create File
        new_file = []
        with open(list_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Add List to File
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    # Check if list already exists
    for todo_list in lists:
        if todo_list["List_Name"] == list_name:
            message = {"Message": "A List With That Name Already Exists"}
            return json.dumps(message, indent=4)
    
    new_list = {
        "List_Name": list_name,
        "Items": []
    }

    lists.append(new_list)

    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {"Message": "List Created Successfully"}
    return json.dumps(message, indent=4)
        


def show_list(list_name):
    '''
    Description: gets all contents of a specified list

    Args:
      list_name (string): the name of the list to get the contents of
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    for grocery_list in lists: 
        if grocery_list["List_Name"] == list_name:
            return json.dumps(grocery_list, indent=4)

    message = {"Message": "List Not Found"}
    return json.dumps(message, indent=4)


def add_item_to_list(list_name, item_name, quantity, category="Other"):
    '''
    Description: adds an item to the specified grocery list

    Args:
      list_name (string): The name of the list that the item will be added to
      item_name (string): the name of item being added
      quantity (string): the amount of the item that needs to be purchased 
      category (string): The category of the grocery item. Options: Produce, Dry Goods, Snacks, Meats, Dairy, Frozen, Other. Defaults to other if not provided
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    list_found = False    
    for grocery_list in lists: 
        if grocery_list["List_Name"] == list_name:
            list_found = True
            if not grocery_list["Items"]:
                new_item = {
                    "Item_Name": item_name,
                    "Quantity": quantity,
                    "Category": category
                }
                grocery_list["Items"].append(new_item)
                break

            for item in grocery_list["Items"]:
                if item["Item_Name"] == item_name:
                        message = {
                            "Message": "Item Already In List",
                            "Item": {
                                "Item_Name": item["Item_Name"],
                                "Quantity": item["Quantity"],
                                "Category": item["Category"]
                            }
                        }
                        return json.dumps(message, indent=4)

            new_item = {
                "Item_Name": item_name,
                "Quantity": quantity,
                "Category": category
            }
            grocery_list["Items"].append(new_item)
            break

    if not list_found:
        message = {"Message": "List Not Found"}
        return json.dumps(message, indent=4)
        
    # Update list file
    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {
        "Message": "Item Successfully Added",
        "Item": {
            "Item_Name": item_name,
            "Quantity": quantity,
            "Category": category
        }
    }
    return json.dumps(message, indent=4)


def remove_item_from_list(list_name, item_name):
    '''
    Description: removed an item to the specified grocery list based on the item_name

    Args:
      list_name (string): The name of the list that the item will be removed from
      item_name (string): the name of item being removed
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    list_found = False
    item_found = False
    for grocery_list in lists: 
        if grocery_list["List_Name"] == list_name:
            list_found = True
            for item in grocery_list["Items"]:
                if item["Item_Name"] == item_name:
                    item_found = True
                    grocery_list["Items"] = [item for item in grocery_list["Items"] if item["Item_Name"] != item_name]
                    break

    if not list_found:
        message = {"Message": "List Not Found"}
        return json.dumps(message, indent=4)
    if not item_found:
        message = {"Message": "Item Not Found"}
        return json.dumps(message, indent=4)
    
    # Update list file
    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {
        "Message": "Item Successfully Removed",
    }
    return json.dumps(message, indent=4)



def edit_item(list_name, item_name, item_name_change=0, quantity=0, category=0):
    '''
    Description: Modifies quantity, item_category, or both of a specified item in a list

    Args:
      list_name (string): The name of the list that the item to modify is on
      item_name (string): the name of item being modified
      item_name_change (string): If this value is supplied the item name is updated to the value
      quantity (string): If this value is supplied the quantity is updated to the value
      item_category (string): If this value is supplied the category is updated to the value. 
        Options: 
          Produce, 
          Dry Goods, 
          Snacks, 
          Meats, 
          Dairy, 
          Frozen, 
          Other. 
          
        Defaults to other if not provided
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    list_found = False
    item_found = False
    for grocery_list in lists: 
        if grocery_list["List_Name"] == list_name:
            list_found = True
            for item in grocery_list["Items"]:
                if item["Item_Name"] == item_name:
                    item_found = True
                    if item_name_change:
                        item["Item_Name"] = item_name_change
                    if quantity:
                        item["Quantity"] = quantity
                    if category:
                        item["Category"] = category

    if not list_found:
        message = {"Message": "List Not Found"}
        return json.dumps(message, indent=4)
    if not item_found:
        message = {"Message": "Item Not Found"}
        return json.dumps(message, indent=4)

    # Update list file
    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {
        "Message": "Item Successfully Updated",
    }
    return json.dumps(message, indent=4)



def delete_list(list_name):
    '''
    Description: Deletes a specified list

    Args:
      list_name (string): The name of the list to delete
    '''

    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    list_found = False
    item_found = False
    for grocery_list in lists: 
        if grocery_list["List_Name"] == list_name:
            list_found = True
            lists = [grocery_list for grocery_list in lists if grocery_list["List_Name"] != list_name]
            break

    if not list_found:
        message = {"Message": "List Not Found"}
        return json.dumps(message, indent=4)

    # Update list file
    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {
        "Message": "List Successfully Removed",
    }
    return json.dumps(message, indent=4)

def show_list_by_category(list_name, category):
    '''
    Description: Returns the items from the list labeled as the specified category

    Args:
      list_name (string): The name of the list the items will be read from
      category (string): The category to find
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    list_found = False
    for grocery_list in lists: 
        if grocery_list["List_Name"] == list_name:
            list_found = True
            category_items = [item for item in grocery_list["Items"] if item["Category"] == category]
            break

    if not list_found:
        message = {"Message": "List Not Found"}
        return json.dumps(message, indent=4)
    
    return json.dumps(category_items, indent=4)

def get_list_names():
    '''
    Description: returns the names of all available lists
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)
    list_names = []
    for grocery_list in lists: 
        list_names.append(grocery_list["List_Name"])

    message = {"Available Lists": list_names}
    return json.dumps(message, indent=4)




#print(create_new_list(list_name="Recipe Shopping List"))

print(show_list(list_name="Recipe Shopping List"))

'''
Options: 
    Produce, 
    Dry Goods, 
    Canned Goods,
    Snacks, 
    Meats, 
    Dairy, 
    Frozen, 
    Other. 
'''
'''
print(add_item_to_list(
    list_name="Recipe Shopping List", 
    item_name="tomato paste", 
    quantity="1 tablespoon", 
    category="Canned Goods"))
'''

#print(remove_item_from_list(list_name="Pantry Replenishment", item_name="apple cider vinegar"))

#print(edit_item(list_name="Pasta Aglio e Olio", item_name="olive oil", quantity="3/4 cup"))

#print(delete_list(list_name="Cheesecake Shopping List"))

#print(show_list_by_category(list_name="Grocery List", category="Other"))

#print(get_list_names())
