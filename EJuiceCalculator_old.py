#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this with tkinter, hopefully

import os
import sys
import json
import pathlib

path = os.path.join(sys.path[0])
load_recipe = input("Do you want to open a saved recipe? (y/N)")

if load_recipe.lower() == "y":
    current_dir = pathlib.Path(f"{path}/saved_recipes")
    for current_file in current_dir.iterdir():
        print(current_file)
        

# Get batch amount
batch_amount = int(input("Input the total amount of E-Juice you wish to make (ML): "))

# Get desired nic level
nic_level = int(input("Input desired nicotine strength of the E-Juice: "))

# If nic level is 0 don't ask for nic solution level
if nic_level > 0:
    nic_base = int(input("Input nicotine solution strength: "))
    nic_result = round(((nic_level / nic_base) * batch_amount), 2)
    #print(nicResult)
else:
    nic_result = 0

# Initialize flavorings name list
flavor_name_list = []

# Ask how many flavors are going to be in this batch
num_flav_list = []

number_of_flavors = input("Enter the number of different flavorings you will be using: ")

flavor_dictionary = dict()
count = 0
while count < int(number_of_flavors):
    count += 1
    data = input ("Enter flavoring name and flavoring percentage seperated by \";\" : ")
    temp = data.split(";")
    flavor_dictionary[temp[0]] = int(temp[1])

#print(flavor_dictionary)
#for key, value in flavor_dictionary.items():
#    print("Flavoring Name: {}, Flavoring Percentage: {}%".format(key, value))

# Initiate  list that will hold ML values of flavors
flavor_ml_amount = []

for key in flavor_dictionary:
    flv_percent = batch_amount * (flavor_dictionary[key] / 100)
    flavor_ml_amount.append(flv_percent)

flavor_total = sum(flavor_ml_amount)

base_total = batch_amount - (flavor_total + nic_result)

flav_name_list = list(flavor_dictionary.keys())

#print(flav_name_list)

print(f"Start with {base_total} ML of VG")
for i in range(len(flavor_ml_amount)):
    print(f"Add {int(flavor_ml_amount[i])} ML of  {flav_name_list[i]}")
print("Add " + str(nic_result) + " ML of nicotine solution.")

save = input("Do you want to save this flavor? (y/N): ")
if save.lower() == "y":
    flavor_name = input("What do you want to save this flavor as? ")
else:
    exit()

filename = f"{path}/saved_recipes/{flavor_name}.json"
with open(filename, "w+") as f:
    json.dump(flavor_dictionary, f)

