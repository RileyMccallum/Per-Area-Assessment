'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
#Basic starting stuff
import math

import os

history = []

#Welcome Message
print("\033[95mHello! Welcome to the Perimeter and Area Calculator. \nThis Program can calculate the perimeter and area to any of the following shapes:\033[0m")

#Recatangle Calculations w/ f-string
def rectangle():
    print("\nEnter the dimensions of the rectangle:")
    length = float(input("\033[96mLength: \033[0m"))
    width = float(input("\033[96mWidth: \033[0m"))
    area = length * width
    perimeter = 2 * length + 2 * width
    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}\n")
#History code for rectangles
    history.append(f"Rectangle with length={length} and width={width}: \nArea={area}, Perimeter={perimeter}\n")

#Circle Calculations1
def circle():
    print("\nEnter the dimensions of the circle:")
    radius = float(input("\033[96mRadius: \033[0m"))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"\nArea: {area}")
    print(f"Circumference: {circumference}\n")
#History code for circles
    history.append(f"Circle with radius={radius}: Area={area}, \nCircumference={circumference}\n")

#Triangle Calculations
def triangle():
    print("\nEnter the dimensions of the triangle:")
    base = float(input("\033[96mBase: \033[0m"))
    height = float(input("\033[96mHeight: \033[0m"))
    side1 = float(input("\033[96mSide 1: \033[0m"))
    side2 = float(input("\033[96mSide 2: \033[0m"))
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}\n")
#History code for Triangles
    history.append(f"Triangle with base={base}, height={height}, side1={side1}, \nside2={side2}: Area={area}, Perimeter={perimeter}\n")

#Parallelogram Calculations
def parallelogram():
    print("\nEnter the dimensions of the parallelogram:")
    base = float(input("\033[96mBase: \033[0m"))
    height = float(input("\033[96mHeight: \033[0m"))
    side = float(input("\033[96mSide: \033[0m"))
    area = base * height
    perimeter = 2 * base + 2 * side
    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}\n")
#History code for Parallelograms
    history.append(f"Parallelogram with base={base}, height={height}, \nside={side}: Area={area}, Perimeter={perimeter}\n")

#Console Clearing
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
  
#User Experience
while True:
    print("\n\033[91mPlease choose a shape:\033[0m")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Parallelogram")
    print("5. Show history")
    print("6. Clear Console")
    print("7. Quit")
  
#User Input Outcomes
    choice = input("\033[94mEnter choice (1-6): \033[0m")
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
        break
    else:
        print("\033[\n92mSorry, this is not a valid choice. Please try again.\n\033[0m")
      