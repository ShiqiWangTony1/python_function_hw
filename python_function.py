# # Task 1
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Division by zero"

# # Task 2
# def main():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    
#     if operation == 'add':
#         result = add(num1, num2)
#     elif operation == 'subtract':
#         result = subtract(num1, num2)
#     elif operation == 'multiply':
#         result = multiply(num1, num2)
#     elif operation == 'divide':
#         result = divide(num1, num2)
#     else:
#         result = "Invalid input. Please choose from add, subtract, multiply, divide."

#     print(f"The result of {operation} operation is: {result}")

# main()


##
# Task 1
def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_item(shopping_list):
    item = input("Enter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

def print_list(shopping_list):
    print("Your shopping list:")
    for item in shopping_list:
        print(f"- {item}")

def main():
    shopping_list = []

    while True:
        print("\nShopping List Maker")
        print("Enter a command: add, remove, print, or quit")
        
        command = input("Your choice: ").strip().lower()
        
        if command == 'add':
            add_item(shopping_list)
        elif command == 'remove':
            remove_item(shopping_list)
        elif command == 'print':
            print_list(shopping_list)
        elif command == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please enter add, remove, print, or quit.")

main()
