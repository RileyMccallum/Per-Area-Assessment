# Importing required modules
import os
from Shapes import rectangle, circle, triangle, parallelogram, history

# Clear console function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear history function
def clear_history():
    global history
    history = []
    print("\n\033[93mHistory Cleared\033[0m")

# Welcome message
print("*" * 90)
print("\033[95mHello! Welcome to the Perimeter and Area Calculator. \nThis Program can calculate the perimeter and area to any of the following shapes:\033[0m")
print("*" * 90)

# User interface
while True:
    print("\n\033[91mPlease choose a shape:\033[0m")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Parallelogram")
    print("5. Show history")
    print("6. Clear Console")
    print("7. Clear History")
    print("8. Quit")

    # User input outcomes
    choice = input("\033[94mEnter choice (1-8): \033[0m")
    if choice == '1':
        rectangle()
    elif choice == '2':
        circle()
    elif choice == '3':
        triangle()
    elif choice == '4':
        parallelogram()
    elif choice == '5':
        print("\n\033[93mSession history:\033[0m")
        for item in history:
            print(item)
    elif choice == '6':
        clear_console()
    elif choice == '7':
        clear_history()
    elif choice == '8':
        break
    else:
        print("\033[\n92mSorry, this is not a valid choice. Please try again.\n\033[0m")
