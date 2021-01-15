"""
Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

list1 = [11, 22, 33, 44]
list2 = [100, 200, 300, 400]

output:

10 400
20 300
30 200
40 100

"""
list1 = [11, 22, 33, 44]
list2 = [100, 200, 300, 400]
list2=list2[::-1]                #reversing list2
list_to_print=zip(list1,list2)   #combining list1 and list2 in order to make easy for iteration its like (11,100) (22,200)......
for a,b in list_to_print:        #unpacking each element in list_to_print(variable)
    print(a,b)
