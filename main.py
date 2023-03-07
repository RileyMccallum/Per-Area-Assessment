'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
#Basic starting stuff
import math
#Variable for storing calculation till the end
history = []

#Rectangle Calulations
def rectangle():
  print("Please Enter Dimensions")
  l=int(input("Length : "))
  w=int(input("Width : "))
  area=l*w
  perimeter=2*(l+w)
  print("Area of Rectangle : ",area)
  print("Perimeter of Rectangle : ",perimeter)
  