# usage of functions in python

import time

time.sleep(1)

def greet():
    print("Hello, welcome to the Python lesson!")
    print("Let's learn about functions.")
greet()

time.sleep(1)


def hello(name):
    print(f"Hello, {name}! Nice to meet you.")

hello("Alice")
time.sleep(1)
hello("Bob")
time.sleep(1)
input_name = input("Enter your name: ")
hello(input_name)

time.sleep(1)

def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")

time.sleep(1)

def sub(a, b):
    return a - b

result = sub(10, 4)
print(f"The difference between 10 and 4 is: {result}")

time.sleep(1)

def mul(a, b):
    return a * b

result = mul(6, 7)
print(f"The product of 6 and 7 is: {result}")

time.sleep(1)

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

result = div(20, 5)
print(f"The quotient of 20 and 5 is: {result}")

result = div(10, 0)
print(f"Trying to divide 10 by 0: {result}")

time.sleep(1)

def power(base, exponent):
    return base ** exponent

result = power(2, 3)
print(f"2 raised to the power of 3 is: {result}")

time.sleep(1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print(f"The factorial of 5 is: {result}")

time.sleep(1)

def bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi_value = bmi(weight, height)
print(f"Your BMI is: {bmi_value:.2f}")

time.sleep(1)

print("That's all for today's lesson on functions. See you next time!")
