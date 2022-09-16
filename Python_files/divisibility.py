a = int(input("enter num:"))

if a%5==0:
    print(a, "is divisible by 5 only.")
    if a%11==0:
        print(a, "is divisible by both.")
else:
    print(a, "is not divisible by both.")
    