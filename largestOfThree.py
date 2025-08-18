# Write a Python program that uses nested if statements (nested decisions) to get three integers from the user and outputs the largest of the three.

print("Enter three integers:")

# User input validation function
def getUserInput(prompt):
    try:
        return int(input(prompt))  # Try converting input to integer
    except ValueError:
        print("Error, please enter an integer value.")
        return getUserInput(prompt)  # Ask again if invalid

# Get inputs safely
a = getUserInput("First number: ")
b = getUserInput("Second number: ")
c = getUserInput("Third number: ")

# Nested if to find largest
if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("The largest number is:", largest)

