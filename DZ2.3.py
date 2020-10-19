fizz = int(input("Enter first number"))
buzz = int(input("Enter second number"))
a = int(input("Enter the third one"))

for c in range (1, a +1):

    if (c % fizz == 0) and (c % buzz == 0):
        print("FB")
    elif c % fizz == 0:
        print ("F")
    elif c % buzz == 0:
        print ("B")
    else:
        print(c)
