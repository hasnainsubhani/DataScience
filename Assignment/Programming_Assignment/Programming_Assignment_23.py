'''Question 1
Create a function that takes a number as an argument and returns True or False depending
on whether the number is symmetrical or not. A number is symmetrical when it is the same as
its reverse.'''

def Is_Symmetrical(numb)->bool:
  '''Create a function that takes a number as an argument and returns True or False depending
  on whether the number is symmetrical or not. A number is symmetrical when it is the same as
  its reverse.'''
  Symmetrical = False
  numb1 = numb
  numb2 = numb
  l = 0
  while(numb1>0):
    l = l+1
    numb1 = int(numb1/10)

  sum = 0
  while l>0:
    sum = sum + ((numb2%10)*(10**(l-1)))
    numb2 = int(numb2/10)
    l = l-1
  
  if numb == sum:
    Symmetrical = True

  return Symmetrical



'''Question 2
Given a string of numbers separated by a comma and space, return the product of the
numbers.'''

def Multiply_Nums(numb:str)->int:
    '''Given a string of numbers separated by a comma and space, return the product of the numbers.'''
    prod = 1
    for item in numb.split(","):
        prod = prod*int(item.rstrip())
    return prod


'''Question 3
Create a function that squares every digit of a number.'''

def Square_digit(numb:int)->int:
  '''Create a function that squares every digit of a number.'''
  numb2 = numb
  numb1 = numb
  l = 0
  while(numb1>0):
    l = l+1
    numb1 = int(numb1/10)
  SN = ""
  sum = list()
  for i in range(1,l+1):
    SN = (numb2%10)**2
    sum.append(SN)
    numb2 = int(numb2/10)
  
  return int(''.join(map(str,sum)))



'''Question 4
Create a function that sorts a list and removes all duplicate items from it.'''

def Setify(lst:'list')->list:
  '''Create a function that sorts a list and removes all duplicate items from it.'''  
  s = set(lst)
  return (list(s))


'''Question 5
Create a function that returns the mean of all digits.'''


def Mean(numb)->int:
  '''Create a function that returns the mean of all digits.'''
  numb1 = numb
  numb2 = numb
  l = 0
  while(numb1>0):
    l = l+1
    numb1 = int(numb1/10)
  length = l
  sum = 0
  while l>0:
    sum = sum + (numb2%10)
    numb2 = int(numb2/10)
    l = l-1  
  
  return int(sum/length)