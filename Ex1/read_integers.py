number=''
list_numbers=[]
list_negav=[]
list_even_numbers=[]


while number !=0:
    number=int(input('Please type in an integer: '))
    list_numbers.append(number)
    if number==0:
        break

def negative_integer(list_numbers):
    for number in list_numbers:
        if number<0:
            list_negav.append(number)
    return len(list_negav)

def even_numbers(list_numbers):
    for number in list_numbers:
        if number%2==0:
           list_even_numbers.append(number) 
    return len(list_even_numbers)
  
print('Number of even numbers is', even_numbers(list_numbers))   
  