#Q1

n = int(input("Enter the size of list you want to create:"))

l = []

a = ""

for i in range(n):
    a = input("Enter the elements:")
    l.append(a)
print("The made list:",l)

p = input("Enter the element u wanna check:")

if p in l:
    print("The element is at",l.index(p)+1,"position.")
else:
    print("Wrong input.")
    
#Q2

list = [1,3,4,2,4,2,4,4,5]
print("The position is at",list.index(4)+1)

#Q3
#list.index(elemnet,start,end)
#returns the lowest index where the element appears.

list = [6,2,7,8,5,7,4,2,1,8]
print("The position is at",list.index(7,1,9)+1)

list = ['cat','bat','mat','fat','hat','cat','get','pot']
print("The position is at",list.index('cat',2,6)+1)

#Q4

list = [1,2,3,[4,5,6],('bat','cat')]
print("The position is at",list.index([4,5,6])+1)
