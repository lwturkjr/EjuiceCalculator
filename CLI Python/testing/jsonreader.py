#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this, hopefully

import os
import sys
import json
import pathlib

path = os.path.join(sys.path[0])

saved_recipes = pathlib.Path(f"{path}/saved_recipes/recipes.json")

with open(saved_recipes, "r+") as json_file:
    saved_recipes = json.load(json_file)
    print("Saved Recipes:")
    for entry in saved_recipes:
            print(entry)

recipe_name = input("Which recipe do you want to load?: ")

recipe_to_load = saved_recipes[recipe_name]

print(recipe_to_load)

json_file.close()