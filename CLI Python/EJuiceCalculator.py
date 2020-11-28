#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this, hopefully

import os
import sys
import json
import pathlib

path = os.path.join(sys.path[0])

def load_saved_recipe():
    current_dir = pathlib.Path(f"{path}/saved_recipes")
    for current_file in current_dir.iterdir():
        print(current_file)
    
    print(f"Just enter the recipe name, not the full path, and you don't need to include the .json extension")
    recipe_name = input("Which recipe do you want to load?: ")
    recipe_path = f"{current_dir}/{recipe_name.title()}.json"

    with open(recipe_path, "r+") as json_file:
        recipe = json.load(json_file)

        return recipe
    

def start_new_recipe():
    number_of_flavorings = input("Enter the number of different flavorings you will be using: ")

    flavor_dictionary = dict()
    count = 0
    while count < int(number_of_flavorings):
        count += 1
        flavoring_name = input("Enter flavoring name: ")
        flavoring_percentage = input(f"What percentage of {flavoring_name} do you want recpie to have? : ")
        data = f"{flavoring_name}:{flavoring_percentage}"
        temp = data.split(":")
        flavor_dictionary[temp[0]] = int(temp[1])
    
    return flavor_dictionary

def save_recipe():
    flavor_name = input("What do you want to save this flavor as? ")
    filename = f"{path}/saved_recipes/{flavor_name.title()}.json"
    with open(filename, "w+") as f:
        json.dump(recipe, f)
    print(f"Recipe Saved to {filename}.")
    input("Press any key to exit...")

load_recipe = input("Do you want to open a saved recipe? (y/N): ")
if load_recipe.lower() == "y":
    recipe = load_saved_recipe()
else:
    recipe = start_new_recipe()

# Get batch amount
batch_amount = int(input("\nInput the total amount of E-Juice you wish to make (ML): "))

# Get desired nic level
nic_level = int(input("Input desired nicotine strength of the E-Juice: "))

# If nic level is 0 don't ask for nic solution level
if nic_level > 0:
    nic_base = int(input("Input nicotine solution strength: "))
    nic_result = round(((nic_level / nic_base) * batch_amount), 2)
    #print(nicResult)
else:
    nic_result = 0

# Initiate  list that will hold ML values of flavors
flavor_ml_amount = []

for key in recipe:
    flv_percent = batch_amount * (recipe[key] / 100)
    flavor_ml_amount.append(flv_percent)

base_total = batch_amount - (sum(flavor_ml_amount) + nic_result)

flav_name_list = list(recipe.keys())

print(f"\nBatch Size {batch_amount}ML")
for i in range(len(flavor_ml_amount)):
    print(f"{flav_name_list[i]}: {round(flavor_ml_amount[i], 2)}ML")
print(f"Nicotine solution: {nic_result}ML")
print(f"VG {base_total}ML")

print("\nFlavoring percentages: ")
for key, value in recipe.items():
    print(f"Flavoring {key}: {value}%")

if load_recipe.lower() == "y":
    input("Press any key to exit...")
    exit()

save = input("\nDo you want to save this recipe? (y/N): ")
if save.lower() == "y":
    save_recipe()
else:
    input("Press any key to exit...")
    exit()
    
