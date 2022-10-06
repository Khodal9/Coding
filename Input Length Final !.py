print("Hello,WElCOME!\n Please Enter Your Username")
#Taking name 
char=input()
Length=len(char)
a=0
while a==0:
    #Checking Length
    if Length <2:
        print("Sorry,Username Must be Longer than 1 letter")
    elif Length >20:
        print("Sorry,Username Cannot be more than 20 letters in length")
        #Checking if it contains Capital and a number
    else:
        if char>='A' and char<='Z' or char>='0' and char<='9':
            print("Your username is", char.strip(" ") )
            break
        else:
            print(" Error! Enter the name again! Run again")
            break