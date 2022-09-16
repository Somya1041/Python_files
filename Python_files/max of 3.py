#max of 3 num

a = int(input("Give value of a:"))
b = int(input("Give value of b:"))
c = int(input("Give value of c:"))

if a>b:
    if a>c:
        print(a, "is greatest.")
        
    else:
        print(c, "is greatest.")   
        
else:
    if b>c:
        print(b, "is greatest.")
        
    else:
        print(c, "is greatest.")             