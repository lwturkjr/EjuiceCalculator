#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this, hopefully

import os
import sys
import json
import pathlib

path = os.path.join(sys.path[0])

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

recipe = start_new_recipe()

def save_recipe():
    saved_recipes = pathlib.Path(f"{path}/saved_recipes/recipes.json")
    flavor_name = input("What do you want to save this flavor as? ")
    entry = {flavor_name: recipe}

    with open(saved_recipes, "r+") as json_file:
        data = json.load(json_file)
        data.update(entry)
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
    print("Recipe Saved.")
    json_file.close()
    input("Press any key to exit...")

print(recipe)
save_recipe()