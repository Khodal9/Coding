#Interface for the user to select the area he/she wants.
print("Geometry Calculator")
print(" \n")
print(" \n")
print("1. Calcalute  Area of the Circle \n")
print("2. Calculate  Area of the rectangle \n")
print("3. Calculate  Area of the triangle \n")
print("4. Quit \n")
print(" \n ")
print("Enter your choice (1-4): ")
#Taking Choice as an input from the user
Choice=input()
Choice=float(Choice)
#If statement for 1st Choice Area of the Circle
if Choice==1 :
    print("Enter the radius for the circle \n")
#Radius of the circle
    radius=input()
    radius=float(radius)
#Area of the Circle calculated use pie r square 
    area=3.14*radius*radius
    area=str(area)
#printing the area in cm^2
    print("Area of the Circle is"+area)


#Elif statement for 2nd choice for area and perimeter of the Rectangle
elif Choice==2 :
    print("Enter the Width of the rectangle in cm \n")
    Width=input()
    Width=float(Width)
    print("Enter the Length of the rectangle in cm \n")
    Length=input()
    Length=float(Length)
    area=Width*Length
    area=str(area)
    print("Area of the rectangle is "+ area +"cm^2")
    perimeter=Length + Width
    perimeter=str(perimeter)
    print("And perimeter is " + perimeter +"cm")
#Elif statement for 3rd choice for area and perimeter of the Triangle
elif Choice==3:
    print("Enter the width of the triangle in cm \n")
    Width=input()
    Width=float(Width)
    print("Enter the Length of the triangle in cm \n")
    Length=input()
    Length=float(Length)
    area=(Width*Length)/2
    area=str(area)
    print("Area of the Triangle is "+ area +"cm^2")
    perimeter=Length + Width +Length
    perimeter=str(perimeter)
    print("And perimeter is " + perimeter +"cm")
#Elif statement for quitting the program
elif Choice==4:
    print("You Chose to Quit Bye!")
#Else statement if user enters number which is not in 1-4.
else:
    print("There is no such choice You need to choose between 1 and 4")
    








    

