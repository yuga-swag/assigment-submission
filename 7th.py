# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check the age and display the appropriate message
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")