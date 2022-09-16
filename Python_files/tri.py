#Pattern I

n = int(input("Enter the size:"))

for i in range(0,n):
    for j in range(0, i + 1):
        print("*", end = " ")
    print("\r")


#Pattern II

n = int(input("enter size:"))

k = 2 * n - 2

for i in range(0, n):
    for j in range(0, k):
        print(end = " ")
        
    k = k - 2
    
    for j in range(0, i + 1):
        print("*", end = " ")
    
    print("\r")
    

#Pattern III            

n = int(input("enter size:"))

k = n - 1

for i in range(0,n):
    for j in range(0,k):
        print(end = " ")
    
    k = k - 1
    
    for j in range(0, i + 1):
        print("*", end = " ")
    
    print("\r")            
       

#Pattern IV

n = int(input("Enter size:"))

num = 1

for i in range(0,n):
    for j in range(0, i + 1):
        print(num, end =" ")
        num = num + 1
    
    print("\r")            


#Pattern V

n = int(input("enter size:"))

num = 65

for i  in range(0,n):
    for j in range(0, i + 1):
        ch = chr(num)
        print(ch, end = " ")
        num = num + 1
        
    print("\r") 

