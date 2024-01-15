import random
list_numbers=[]
for i in range(10): 
    # number input from user 
    number=int(input('Please type in a number: '))

    list_numbers.append(number)
    # list_numbers.sort()

print('List of numbers', list_numbers)

list_strings=[]
for j in range(10):
    string=input('Please type in a string: ')
    list_strings.append(string)  
 # list_strings.sort()
print('List of strings', list_strings)
