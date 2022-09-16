# #Method-I

a = int(input("Enter the value of N1:"))
b = int(input("Enter the value of N2:"))
a,b=b,a
print("Value of N1 after interchange:",a)
print("Value of N2 after interchange:",b)

# #Method-II

a = int(input("Enter the value of N1:"))
b = int(input("Enter the value of N2:"))
c=a
a=b
b=c
print("Value of N1 after interchange:",a)
print("Value of N2 after interchange:",b)

# #Method-III

a = int(input("Enter the value of N1:"))
b = int(input("Enter the value of N2:"))
a = a+b
b = a-b
a = a-b
print("Value of N1 after interchange:",a)
print("Value of N2 after interchange:",b)

#Method IV

a = int(input("Enter the value of N1:"))
b = int(input("Enter the value of N2:"))
a = a ^ b
b = a ^ b
a = a ^ b
print("Value of N1 after interchange:",a)
print("Value of N2 after interchange:",b)

#Method V

a = int(input("Enter the value of N1:"))
b = int(input("Enter the value of N2:"))
a = a * b
b = a / b
a = a / b
print("Value of N1 after interchange:",a)
print("Value of N2 after interchange:",b)

#Method VI

a = int(input("Enter the value of N1:"))
b = int(input("Enter the value of N2:"))
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print("Value of N1 after intrchange:",a)
print("Value of N2 after intrchange:",b)