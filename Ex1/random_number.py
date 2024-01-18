import random
def random_number():
  list_number=[1,2,3,4,5,6]
  number=random.choice(list_number)
  return number

# Print out the number where the function is called
print(random_number())