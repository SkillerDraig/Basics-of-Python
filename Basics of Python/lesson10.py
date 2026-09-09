# Usage of file handling in python

# create contacts.txt file if it doesn't exist

import os

if not os.path.exists("contacts.txt"):
    with open("contacts.txt", "w") as file:
        file.write("Contacts List\n")
        file.write("--------------\n")

with open("contacts.txt", "a") as file:
    input_name = input("Enter name: ")
    try:
        input_number = int(input("Enter number: "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        file.write(f"{input_name}: {input_number}\n")