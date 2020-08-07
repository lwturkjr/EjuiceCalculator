#! /usr/bin/env python3
# Basic Command Line Python E-Juice Calculator
# I will eventually make a GUI for this with QT or something more "modern" looking, hopefully

import tkinter as tk

root = tk.Tk()
root.title("Ejuice Calculator")
root.iconbitmap("./flask.ico")

button_quit = tk.Button(root, text="Exit Program", command=root.quit, padx=30, pady=5)


batch_ammount_label = tk.Label(root, text="Input the total amount of E-Juice you wish to make (ML): ")
batch_entry = tk.Entry(root)

nic_level_label = tk.Label(root, text="Input desired nicotine strength of the E-Juice: ")
nic_level_entry = tk.Entry(root)

flavor_amount_label = tk.Label(root, text="Enter the number of different flavorings you will be using: ")
flavor_amount_entry = tk.Entry(root)

button_calculate = tk.Button(root, text="Calculate", padx=100, pady=5)

batch_ammount_label.grid(row=0, column=0, padx=10, pady=1, sticky=tk.W)
batch_entry.grid(row=0, column=1)

nic_level_label.grid(row=1, column=0, padx=10, pady=1, sticky=tk.W)
nic_level_entry.grid(row=1, column=1)

flavor_amount_label.grid(row=2, column=0, padx=10, pady=1, sticky=tk.W)
flavor_amount_entry.grid(row=2, column=1)

button_calculate.grid(row=100, column=0, padx=10, pady=1)
button_quit.grid(row=100, column=1, padx=10, pady=1)

root.mainloop()

