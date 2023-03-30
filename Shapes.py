#Starting Stuff
history = []
import math

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("\033[31mSorry. Invalid input. Please enter an integer:\033[0m")
          
#Recatangle Calculations w/ f-string
def rectangle():
    print("\nEnter the dimensions of the rectangle:")
    length = get_integer_input("\033[96mLength: \033[0m")
    width = get_integer_input("\033[96mWidth: \033[0m")
    area = length * width
    perimeter = 2 * length + 2 * width
    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}\n")
#History code for rectangles
    history.append(f"Rectangle with length={length} and width={width}: \nArea={area}, Perimeter={perimeter}\n")

#Circle Calculations1
def circle():
    print("\nEnter the dimensions of the circle:")
    radius = get_integer_input("\033[96mRadius: \033[0m")
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"\nArea: {area}")
    print(f"Circumference: {circumference}\n")
#History code for circles
    history.append(f"Circle with radius={radius}: Area={area}, \nCircumference={circumference}\n")

#Triangle Calculations
def triangle():
    print("\nEnter the dimensions of the triangle:")
    base = get_integer_input("\033[96mBase: \033[0m")
    height = get_integer_input("\033[96mHeight: \033[0m")
    side1 = get_integer_input("\033[96mSide 1: \033[0m")
    side2 = get_integer_input("\033[96mSide 2: \033[0m")
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}\n")
#History code for Triangles
    history.append(f"Triangle with base={base}, height={height}, side1={side1}, \nside2={side2}: Area={area}, Perimeter={perimeter}\n")

#Parallelogram Calculations
def parallelogram():
    print("\nEnter the dimensions of the parallelogram:")
    base = get_integer_input("\033[96mBase: \033[0m")
    height = get_integer_input("\033[96mHeight: \033[0m")
    side = get_integer_input("\033[96mSide: \033[0m")
    area = base * height
    perimeter = 2 * base + 2 * side
    print(f"\nArea: {area}")
    print(f"Perimeter: {perimeter}\n")
#History code for Parallelograms
    history.append(f"Parallelogram with base={base}, height={height}, \nside={side}: Area={area}, Perimeter={perimeter}\n")