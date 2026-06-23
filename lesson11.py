# Error handling in python

import time


try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a number.")
except:
    print("An unexpected error occurred.")
else:
    print(f"You entered: {age}")

time.sleep(1)

while True:
    try:
        number = int(input("Enter a number to divide 100 by: "))
        result = round(100 / number, 2)
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except:
        print("An unexpected error occurred.")
    else:
        print(f"100 divided by {number} is {result}")
        break
