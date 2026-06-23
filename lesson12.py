# Usage of libraries in python. There are 3 types of libraries in python: built-in libraries, external libraries, and custom libraries.

# Built-in libraries are those that come pre-installed with Python.

import math  # This is a built-in library for mathematical functions

print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793
print(math.floor(3.7))  # Output: 3
print(math.ceil(3.2))  # Output: 4
print(math.pow(2, 3))  # Output: 8.0

import random

print(random.randint(1, 10))  # Output: Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Output: Randomly selected item from the list
print(random.shuffle(['apple', 'banana', 'cherry']))  # Output: Shuffles the list in place
print(random.sample(['apple', 'banana', 'cherry'], 2))  # Output: Randomly selected 2 items from the list
print(random.random())  # Output: Random float between 0.0 and 1.0

from datetime import datetime

now = datetime.now()
print(now)  # Output: Current date and time
print(now.year)  # Output: Current year
print(now.month)  # Output: Current month
print(now.day)  # Output: Current day
print(now.hour)  # Output: Current hour
print(now.minute)  # Output: Current minute
print(now.second)  # Output: Current second
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: Current date and time in specified format

import os

print(os.getcwd())  # Output: Current working directory
print(os.listdir())  # Output: List of files and directories in the current working directory
os.makedirs("my_folder", exist_ok=True)  # Creates a new directory named "my_folder" if it doesn't exist

# External libraries are those that need to be installed separately using package managers like pip.

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200 means success

# Custom libraries are those that are created by the user for specific purposes.

# import my_custom_library  # Assuming you have a custom library named my_custom_library.py

# my_custom_library would contain user-defined functions and classes that can be imported and used in this script.
# like def greet(name): return f"Hello, {name}!"
# print(my_custom_library.greet("Alice"))  # Output: Hello, Alice!
