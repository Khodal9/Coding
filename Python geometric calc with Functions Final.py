
#Made a function for calculating area of the square
def square():
    print("Enter the side of the square")
    side=float(input())
    area=side*side
    print("Area of the square is" + str(area))
    perimeter=4*side
    print("Perimeter of the square is",str(perimeter))
#Made a function for calculation area of the rectangle
def rectangle():
    print("Enter the side of the Rectangale")
    Length=float(input())
    print("Enter the Breadth of the rectangale ")
    Breadth=float(input())
    area=Length*Breadth
    print("Area of the square is" + str(area))
    perimeter=2*(Length+Breadth)
    print("Perimeter of the rectangle is",str(perimeter))
#Made a function for calculating the area of the circle
def circle():
    print("Enter the Radius of the circle")
    Radius=float(input())
    area=3.14*Radius
    print("Area of the circle is" + str(area))


#Making a starting interface for the user to enter the choice.
print("Geometric Calculator \n")
print(" 1-Square\n 2-Rectangle\n 3-Area of Circle\n 4-Quit")
print("Enter Your choice")
Choice=int(input())
#Calling the Functions as per the choice.
if Choice==1:
    square()
elif Choice==2:
    rectangle()
elif Choice==3:
    circle()
elif Choice==4:
    print("You Chose to Quit Bye!")
else:
    print("No such choice available")
