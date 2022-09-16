list={'Somya','CSE21173','2101020487','CSE'}
print(list)



list={1,2,3,4,5,6,7,8,9,10}
for num in list:
    if num%2==0:
        print(num)
        

        
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3 = list1+list2
print(list3)


    
list=[4,5,8,10,31]
print(list)

flag=0

list=list[:]
list.sort()

if(list == list):
   flag=1
    
if(flag):
    print("List is sorted.")
else:
    print("List is not sorted.")



    
list=[1,2,3,4,5]
total=sum(list)
print("Sum:", total)




list=[1,2,3,4,2,3,1]
for i in list:
    c=list.count(i)
    if c!=1:
        list.remove(list[i])
print(list)