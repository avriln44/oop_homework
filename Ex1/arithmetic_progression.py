list_numbers=[]
list_squared_terms=[]
number=int(input('Please type in a number which is bigger than 2 '))
for i in range(3,number+1,3):
    if i%3==0:
        list_numbers.append(i)

# function which returns the length of the list
def length_list(list_numbers):
    return len(list_numbers)

# function which returns the sum of all the terms in the list
def sum_terms(list_numbers):
    return sum(list_numbers)

# function which returns the sum of all the squared terms in the list
def sum_squared_terms(list_numbers):
    for number in list_numbers:
        number=number*number
        list_squared_terms.append(number)
    return sum(list_squared_terms)

print('List of arithmetic progression is', list_numbers)  
print('Number of the terms is', length_list(list_numbers)) 
print('Sum of the terms is', sum_terms(list_numbers))
print('Sum of the squared terms is ', sum_squared_terms(list_numbers))