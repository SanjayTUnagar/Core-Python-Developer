
#Switch case program 

x = int(input("Enter number 1 to 4: "))

match x:

    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
     print("Default")