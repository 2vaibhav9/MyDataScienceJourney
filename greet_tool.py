# greet_tool.py
def greet_employee(name, shift):
    if shift == "morning":
        print(f"Good morning, {name}!")
    elif shift == "night":
        print(f"Good evening, {name}!")
    else:
        print(f"Hello, {name}!")

# Try your own test cases
greet_employee("Ravi", "morning")
greet_employee("Priya", "night")