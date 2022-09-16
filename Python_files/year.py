y = int(input("enter a year: "))

if (y % 4 == 0 and y % 100 != 0):
    print(y, "is a leap year.")
    
elif(y % 400 == 0 and y % 100 == 0):
    print(y, "is a leap year.")
    
else:
    print(y,"is not a leap year.") 