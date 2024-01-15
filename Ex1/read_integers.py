number=''
list_numbers=[]
list_negav=[]


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

  