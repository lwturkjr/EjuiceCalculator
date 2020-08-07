#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this with tkinter, hopefully

import os
import sys

path = os.path.join(sys.path[0])

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

for i in range(int(number_of_flavors)):
    num_flav_list.append(i+1)

#print(num_flav_list)

print ("Enter flavoring names:")
# Get the flavorings names
for i in range(len(num_flav_list)):
    n = input(f"Flavoring {num_flav_list[i]} Name: ")
    flavor_name_list.append(str(n))

# Initiate flavor percentage list
flavor_percentage_list = []

print ("Enter flavoring percentage:")
# Add flavor percentages to flavor list
for i in range(len(flavor_name_list)):
    n = input("Percentage of " + flavor_name_list[i] + ": ")
    flavor_percentage_list.append(int(n))
    #print ('ARRAY: ',flavor_percentage_list)
#print(flavor_name_list)
#print(flavor_percentage_list)

# Initiate  list that will hold ML values offlavors
flavor_ml_amount = []

# Calculate ML value to add to batch and add to list
for i in range(len(flavor_percentage_list)):
    x = batch_amount * (flavor_percentage_list[i] / 100)
    flavor_ml_amount.append(int(x))
    #print('ARRAY: ', flavorAmount)

flavor_total = sum(flavor_ml_amount)

base_total = batch_amount - (flavor_total + nic_result)

print("Start with ", base_total, "ML of VG")
for i in range(len(flavor_ml_amount)):
    print("Add " + str(flavor_ml_amount[i]) + " ML of " + str(flavor_name_list[i]) )
print("Add " + str(nic_result) + " ML of nicotine solution.")
