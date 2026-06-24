# Usage of file handling in python

with open("contacts.txt", "a") as file:
    input_name = input("Enter name: ")
    input_number = input("Enter number: ")
    file.write(f"{input_name}: {input_number}\n")
