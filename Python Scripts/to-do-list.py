import json
import os

list_file = "my-to-do-lists.json"

def create_new_list(list_name):
    '''
    Description: Create a new to-do list

    Args:
      list_name (string): the name of the new list
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
        "To_Do_Items": []
    }

    lists.append(new_list)

    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {"Message": "List Created Successfully"}
    return json.dumps(message, indent=4)
        



def add_item_to_list(list_name, item, priority="Low"):
    '''
    Description: Add an item to the to-do-list

    Args:
      list_name (string): The list to add the item to
      item (string): content of the to-do item
      priotity (string): the priority of the item. Options: Low, Medium, High, Urgent
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)

    list_found = False    
    for todo_list in lists: 
        if todo_list["List_Name"] == list_name:
            list_found = True
            item_num = len(todo_list["To_Do_Items"]) + 1
            new_item = {
                "Item_Number": item_num, 
                "Item": item,
                "Priority": priority
            }

            todo_list["To_Do_Items"].append(new_item)
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
            "Item_Number": item_num, 
            "Item": item,
            "Priority": priority
        }
    }
    return json.dumps(message, indent=4)



def remove_item_from_list(list_name, item_number):
    '''
    Description: Removes an item from the list based on the provided item number
    
    Args:
      list_name (string): the list to remove the item from
      item_number (number): The list number of the item to be removed
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)
    
    for todo_list in lists: 
        if todo_list["List_Name"] == list_name:
            todo_list["To_Do_Items"] = [item for item in todo_list["To_Do_Items"] if item["Item_Number"] != item_number]

        # Update list file
    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    message = {
        "Message": "Successfully Removed Item",
        "Item": {
            "Item_Number": item_number, 
        }
    }
    return json.dumps(message, indent=4)


def change_priority(list_name, item_number, priority):
    '''
    Description: changes the priority of an item in the list
    
    Args:
      list_name (string): the list to modify
      item_number (number): the list number of the item to be updated
      priority (string): the new priority of the item, Options: Low, Medium, High, Urgent
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)
    
    for todo_list in lists: 
        if todo_list["List_Name"] == list_name:
            for item in todo_list["To_Do_Items"]:
                if item["Item_Number"] == item_number:
                    item["Priority"] = priority
                    message = {
                        "Message": "Priority Updated Successfully",
                        "Item": {
                            "Item_Number": item['Item_Number'], 
                            "Item": item["Item"],
                            "Priority": item["Priority"]
                        }
                    }
                    break
            
    # Update list file
    with open(list_file, 'w') as lf:
        json.dump(lists, lf, indent=4)

    return json.dumps(message, indent=4)

def get_full_list(list_name, sort_by="Item Number"):
    '''
    Description: Provides the full to-do list

    Args:
      list_name (string): The list to pull from
      sort_by (string): the value to sort the list by, Options: Priority High To Low, Priority Low To High, Item Number
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)
    
    priorities = ["Urgent", "High", "Medium", "Low"]
    
    output = []
    for todo_list in lists: 
        if todo_list["List_Name"] == list_name:
            if sort_by == "Item Number":
                output = todo_list["To_Do_Items"]
            else:
                for p in priorities:
                    for item in todo_list["To_Do_Items"]:
                        if item["Priority"] == p:
                            output.append(item)

        if sort_by == "Priority Low To High":
            output = output[::-1]


    return json.dumps(output, indent=4)


def get_by_priority(list_name, priority):
    '''
    Description: Provided a list of the two do items labeled as a specific priority

    Args:
      list_name (string): the list to pull from
      priority (string): the priority to get, Options: Low, Medium, High, Urgent
    '''
    with open(list_file, 'r') as lf:
        lists = json.load(lf)
        
    output = []
    for todo_list in lists: 
        if todo_list["List_Name"] == list_name:
            for item in todo_list["To_Do_Items"]:
                if item["Priority"] == priority:
                    output.append(item)
    
    return json.dumps(output, indent=4)



#print(create_new_list(list_name="Chores"))

#print(add_item_to_list(list_name="Chores", item="Clean kitchen", priority="Low"))

#print(remove_item_from_list(list_name="Chores", item_number=4))

#print(change_priority(list_name="Weekend Chores", item_number=4, priority="Urgent"))

print(get_full_list(list_name="Chores", sort_by="Priority High To Low"))

#print(get_by_priority(list_name="List_2", priority="Low"))