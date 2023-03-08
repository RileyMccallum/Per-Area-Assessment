'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
#Basic starting stuff
import math

history = []

#Recatangle Ca;culations w/ f-string
def rectangle():
    print("Enter the dimensions of the rectangle:")
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    perimeter = 2 * length + 2 * width
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    history.append(f"Rectangle with length={length} and width={width}: Area={area}, Perimeter={perimeter}")

#Circle Calculations
def circle():
    print("Enter the dimensions of the circle:")
    radius = float(input("Radius: "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")
    history.append(f"Circle with radius={radius}: Area={area}, Circumference={circumference}")

#Triangle Calculations
def triangle():
    print("Enter the dimensions of the triangle:")
    base = float(input("Base: "))
    height = float(input("Height: "))
    side1 = float(input("Side 1: "))
    side2 = float(input("Side 2: "))
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    history.append(f"Triangle with base={base}, height={height}, side1={side1}, side2={side2}: Area={area}, Perimeter={perimeter}")

#Parallelogram Calculations
def parallelogram():
    print("Enter the dimensions of the parallelogram:")
    base = float(input("Base: "))
    height = float(input("Height: "))
    side = float(input("Side: "))
    area = base * height
    perimeter = 2 * base + 2 * side
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    history.append(f"Parallelogram with base={base}, height={height}, side={side}: Area={area}, Perimeter={perimeter}")

while True:
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Parallelogram")
    print("5. Show history")
    print("6. Quit")
    choice = input("Enter choice (1-6): ")
    if choice == '1':
        rectangle()
    elif choice == '2':
        circle()
    elif choice == '3':
        triangle()
    elif choice == '4':
        parallelogram()
    elif choice == '5':
        print("Session history:")
        for item in history:
            print(item)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Try again.")