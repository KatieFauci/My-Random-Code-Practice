import json
import os


cookbook_file = "my_cookbook.json"

def create_new_recipe(recipe_title, prep_time=0, cook_time=0, servings=0, instructions=[], ingredients=[]):
    '''
    Description: creates a new recipie with the base information, and instructions and ingredients

    Arg:
        recipe_title (string): the title of the recipe
        prep_time (string): the time it takes to prep the recipe
        cook_time (string): the time it takes to cook the recipe
        servings (number): the number of servings the recipe makes, defaults to 0 if not provided
        ingredients (array): list of lists containg the ingredient and the quantity needed, ingredients not added if not provided, must be formated [ingredient,quantity]
        instructions (array): list of lists containting the step number and the corresponding instruciton, instructions not added if not provided, must be formated [step_number,step]
    '''
    # Check that cook book exists
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # Check if recipe already exists
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            message = {
                "Message": "A Recipe With That Name Already Exists",
                "Recipe": recipe
            }
            return json.dumps(message, indent=4)
        
    this_recipe = {
        "Title": recipe_title,
        "Prep_Time": prep_time,
        "Cook_Time": cook_time,
        "Servings": servings,
        "Ingredients": [],
        "Instructions": []
    }

    if ingredients:
        for i in ingredients:
            this_i = {
                "Ingredient": i[0],
                "Quantity": i[1]
            }
            this_recipe["Ingredients"].append(this_i)

    if instructions:
        for i in instructions:
            this_i = {
                "Step_Number": i[0],
                "Instruction": i[1]
            }
            this_recipe["Instructions"].append(this_i)

    cookbook.append(this_recipe)

    with open(cookbook_file, 'w') as lf:
        json.dump(cookbook, lf, indent=4)

    message = {
        "Message": "Recipe Created Successfully",
        "Recipe": this_recipe
        }
    return json.dumps(message, indent=4)


def delete_recipe(recipe_title):
    '''
    Description: Deletes a recipe from the cookbook

    Args: 
      recipe_title (string): The name of the recipe to be deleted
    '''
    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    updated_cookbook = []
    recipe_found = False
    for recipe in cookbook:
        if not recipe["Title"] == recipe_title:
            updated_cookbook.append(recipe)
        else:
            recipe_found = True

    if recipe_found == True:
        with open(cookbook_file, 'w') as lf:
            json.dump(updated_cookbook, lf, indent=4)

        message = {"Message": "Recipe Deleted Successfully"}
        return json.dumps(message, indent=4)
    
    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)

    

def add_ingredient_to_recipe(recipe_title, ingredient_name, ingredient_quantity):
    '''
    Description: adds an ingridient to an existing recipe

    Args:
      recipe_title (string): The title of the recipe being updated
      ingredient_name (string): The name of the ingredient being added
      ingredient_quantity (string): The quantity of the ingredient being added
    '''
    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            # Recipe Found
            recipe["Ingredients"].append({"Ingredient":ingredient_name, "Quantity":ingredient_quantity})

            with open(cookbook_file, 'w') as lf:
                json.dump(cookbook, lf, indent=4)

            message = {
                "Message": "Recipe Updated Successfully",
                "Recipe": recipe
            }

            return json.dumps(message, indent=4)

    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)


def delete_ingredient(recipe_title, ingredient_name):
    '''
    Description: Deletes and ingredient in a recipe

    Args:
      recipe_title (string): the name of the recipe being updated
      ingredient_name (string): The name of the ingredient being removed
    '''
    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            updated_ingredients = []
            for i in recipe["Ingredients"]:
                if not i["Ingredient"] == ingredient_name:
                    updated_ingredients.append(i)
            recipe["Ingredients"] = updated_ingredients
            
            with open(cookbook_file, 'w') as lf:
                json.dump(cookbook, lf, indent=4)

            message = {
                "Message": "Recipe Updated Successfully",
                "Recipe": recipe
            }

            return json.dumps(message, indent=4)
        
    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)


def add_instruction(recipe_title, step_number, instruction):
    '''
    Description: Add an instruction to a pre-existing recipe, it is inserted in the appropriate place according to the step number. All steps that are bellow it and the one matching the step number are pushed down by one. if the step number passses in is larger than highest step number, it is added to the end of the steps
    
    Args:
      recipe_title (string): The name of the recipe being updated
      step_number (number): The step number of the instruction being added
      instruction (string): The instruction being added
    '''
    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            # Recipe Found
            if step_number > len(recipe["Instructions"]):
                recipe["Instructions"].append({"Step_Number":len(recipe["Instructions"])+1, "Instruction":instruction})
            else:
                instrucitons = recipe["Instructions"]
                updated_instructions = []
                step_num = 1
                for i in instrucitons:
                    if step_num == step_number:
                        updated_instructions.append({"Step_Number":step_num, "Instruction":instruction})
                        step_num += 1
                    i["Step_Number"] = step_num
                    updated_instructions.append(i)
                    step_num += 1   

                recipe["Instructions"] = updated_instructions
    
            with open(cookbook_file, 'w') as lf:
                json.dump(cookbook, lf, indent=4)

            message = {
                "Message": "Recipe Updated Successfully",
                "Recipe": recipe
            }

            return json.dumps(message, indent=4)
        
    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)


def delete_instruction(recipe_title, step_number):
    '''
    Description: Removeses a instruction step and updates the remaining steps to remain in order

    Args:
      recipe_title (string): The name of the recipe being updated
      step_number (number): the step number that is being removed
    '''
    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            instrucitons = recipe["Instructions"]
            updated_instructions = []
            step_num = 1
            for i in instrucitons:
                if i["Step_Number"] != step_number:
                    i["Step_Number"] = step_num
                    updated_instructions.append(i)
                    step_num += 1   

            recipe["Instructions"] = updated_instructions
            
            with open(cookbook_file, 'w') as lf:
                json.dump(cookbook, lf, indent=4)

            message = {
                "Message": "Recipe Updated Successfully",
                "Recipe": recipe
            }

            return json.dumps(message, indent=4)    
        
    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)

def update_ingredient_quantity(recipe_title, ingredient, new_quantity):
    '''
    Description: Updated the quantity of an existing ingredient

    Arg:
      recipe_title (string): the name of the recipe to be updated
      ingredient (string): the name of the ingredient to be updated
      new_quantity (string): The new quanity of the ingredient
    '''
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    recipe_found = False
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            recipe_title = True
            ingredient_found = False
            for i in recipe["Ingredients"]:
                if i["Ingredient"] == ingredient:
                    i["Quantity"] = new_quantity
                    ingredient_found = True
                    with open(cookbook_file, 'w') as lf:
                        json.dump(cookbook, lf, indent=4)
                        message = {
                            "Message": "ingredient Updated Successfully",
                            "Recipe": recipe
                        }
                        return json.dumps(message, indent=4)    
                    
    if not recipe_found:
        message = {
            "Message": "A Recipe With That Title Was Not Found",
            "Recipe Title": recipe_title
        }
    if not ingredient_found:
        message = {
            "Message": "The ingredient could not be found",
        }
    return json.dumps(message, indent=4)

def update_instruction(recipe_title, step_number, new_instruction):
    '''
    Description: Updates an existing instruction

    Args:
      recipe_title (string): The recipe with the instruction to be updated
      step_number (number): The step number to be updated
      new_instruction (string): the new instruction value
    '''
    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    recipe_found = False
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            recipe_title = True
            step_found = False
            for i in recipe["Instructions"]:
                if i["Step_Number"] == step_number:
                    i["Instruction"] = new_instruction
                    step_found = True
                    with open(cookbook_file, 'w') as lf:
                        json.dump(cookbook, lf, indent=4)
                        message = {
                            "Message": "instruction Updated Successfully",
                            "Recipe": recipe
                        }
                        return json.dumps(message, indent=4)       
                    
    if not recipe_found:
        message = {
            "Message": "A Recipe With That Title Was Not Found",
            "Recipe Title": recipe_title
        }
        return json.dumps(message, indent=4)
    if not step_found:
        message = {
            "Message": "The step could not be found",
        }
        return json.dumps(message, indent=4)

def update_recipe_information(update_recipe, recipe_title=0, prep_time=0, cook_time=0, servings=0):
    '''
    Description: Updates recipie information, only updates fields that are passed in

    Args:
      updated_recipe (string): the name of the recipe being updated
      recipe_title (string): updates the recipe title if passed in
      prep_time (string): updates the prep time if passed in
      cook_time (string): updated the cook time if passed in
      servings (string): updates the number of servings
    '''

    # Get recipe
    if not os.path.exists(cookbook_file):
        # Create File
        new_file = []
        with open(cookbook_file, 'w') as f:
            json.dump(new_file, f, indent=4)

    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    for recipe in cookbook:
        if recipe["Title"] == update_recipe:
            # Recipe Found
            if recipe_title:
                recipe["Title"] = recipe_title
            if prep_time:
                recipe["Prep_Time"] = prep_time
            if cook_time:
                recipe["Cook_Time"] = cook_time
            if servings:
                recipe["Servings"] = servings
        
            with open(cookbook_file, 'w') as lf:
                json.dump(cookbook, lf, indent=4)

            message = {
                "Message": "Recipe Updated Successfully",
                "Recipe": recipe
            }

            return json.dumps(message, indent=4)

    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)

def get_recipe(recipe_title):
    '''
    Description: Gets a specified recipe

    Args:
      recipe_name (string): the name of the recipie to get
    '''
    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    # find recipe
    for recipe in cookbook:
        if recipe["Title"] == recipe_title:
            message = {
                "Message": "Recipe Found",
                "Recipe": recipe
            }
            return json.dumps(message, indent=4)

    message = {
        "Message": "A Recipe With That Title Was Not Found",
        "Recipe Title": recipe_title
    }
    return json.dumps(message, indent=4)

def get_recipe_titles():
    '''
    Description: Returns a list of all recipes in the 
    '''
    # Get recipies from cookbook
    with open(cookbook_file, 'r') as lf:
        cookbook = json.load(lf)

    recipe_names = []
    # find recipe
    for recipe in cookbook:
        recipe_names.append(recipe["Title"]);

    message = {
        "Recipe Names": recipe_names
    }
    return json.dumps(message, indent=4)

#response = create_new_recipe(recipe_title="New Recipe", prep_time=1, cook_time=1, servings=2, ingredients=[], instructions=[])#response = delete_recipe(recipe_title="New Recipe")

#response = create_new_recipe(recipe_title="Chicken Noodle Soup", servings=4)

#response = delete_recipe(recipe_title="New Recipe")

#response = delete_recipe(recipe_title="New Recipe")

#response = delete_recipe(recipe_title="New Recipe")

#response = get_recipe(recipe_title="Caprese Salad")

response = add_ingredient_to_recipe(recipe_title="Chicken Noodle Soup", ingredient_name="Fresh Dill", ingredient_quantity="1/4 Cup")

#response = delete_ingredient(recipe_title="BEST Deviled Eggs", ingredient_name="paprika, for garnish")

#response = update_ingredient_quantity(recipe_title="Caprese Salad", ingredient="balsamic glaze", new_quantity="4 tablespoons")

#response = add_instruction(recipe_title="Chicken Noodle Soup", step_number=5, instruction="Bring to a simmer, then remove from heat, and serve.")

#response = update_instruction(recipe_title="BEST Deviled Eggs", step_number=1, new_instruction="updated")

#response = delete_instruction(recipe_title="BEST Deviled Eggs", step_number=5)

#response = update_recipe_information(update_recipe="Caprese Salad", servings=12)

#response = get_recipe_titles()

print(response)