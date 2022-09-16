def multiply_list(list):
    result = 1
    for x in list:
        result = result * x
    return result

list1  = [2,4,6,8]
print(multiply_list(list1))



tup = (1,2,5,3,6,7,4,6,3,6)
for i in tup:
    if tup.count(i) > 1:
        print(i)    