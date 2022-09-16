#Method I

n = int(input("Enter the number:"))

fact = 1

for i in range(1,n+1):
    fact=fact*i
        
print("Factorial of",n,"is",fact)

#Method II

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        fact = 1
        while(n > 0):
            fact = fact * n
            n = n - 1
        return fact
        
a = int(input("Enter the number:"))
print("Factorial of",a,"is",factorial(a))

#Method III

import math

def factorial(n):
    return(math.factorial(n))

a = int(input("Enter the number:"))
print("Factorial of",a,"is",factorial(a))

#Method IV

def factorial(n):
    if n < 0:
        return 0
    elif (n == 0 or n == 1):
        return 1
    else:
        fact = 1
        while(n > 1):
            fact = fact * n
            n = n - 1
        return fact
    
a = int(input("Enter the number:"))
print("Factorial of",a,"is",factorial(a)) 