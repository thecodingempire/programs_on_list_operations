""" This program gets list of values from the user and counts the number of occurence of each element in the list and prints it"""

mylist=eval(input('Enter list of values: '))  #getting input as a list
counters={}                                   #created a empty dictionary to keep count of occurence of element in list
for element in mylist:                        #looping through mylist(variable)
    if element not in counters:               
        counters[element] = 1 #creating       #the element is stored in the dictionary (counters)
    elif element in counters:
        counters[element] = counters[element]+1  #the occurence of the element is updated in the dictionary (counters)
for frequency in counters:
    print(frequency,'occured',counters[frequency],'times in the given list')  #printing all the elements in counters in other words it prints the frequency of elements in a list which user entered
    
