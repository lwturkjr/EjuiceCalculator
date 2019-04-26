#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this with tkinter, hopefully

# Get batch amount
batchAmount = int(input("Input the total amount of E-Juice you wish to make (ML): "))

# Get desired nic level
nicLevel = int(input("Input desired nicotine strength of the E-Juice: "))

# If nic level is 0 don't ask for nic solution level
if nicLevel > 0:
    nicBase = int(input("Input nicotine solution strength: "))
    nicResult = round(((nicLevel / nicBase) * batchAmount), 2)
    #print(nicResult)

# Initiate flavor list
flavorList = list()

# Ask how many flavors are going to be in this batch
numberOfFlavors = input("Enter the number of different flavorings you will be using: ")
print ('Enter flavor percentages:')

# Add flavor percentages to flavor list
for i in range(int(numberOfFlavors)):
    n = input("Flavor Percentage: ")
    flavorList.append(int(n))
    #print ('ARRAY: ',flavorList)

# Initiate  list that will hold ML values offlavors
flavorAmount = list()

# Calculate ML value to add to batch and add to list
for i in range(len(flavorList)):
    x = batchAmount * (flavorList[i] / 100)
    flavorAmount.append(int(x))
    #print('ARRAY: ', flavorAmount)

flavorTotal = sum(flavorAmount)

baseTotal = batchAmount - (flavorTotal + nicResult)

print("Start with ", baseTotal, "ML of VG")
for i in range(len(flavorAmount)):
    print("Add ", flavorAmount[i], "ML of flavor ", i+1)
print("Add ", nicResult, "ML of nicotine solution.")
