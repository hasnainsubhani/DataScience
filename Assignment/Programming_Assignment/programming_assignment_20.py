'''Question1
Create a function that takes a list of strings and integers, and filters out the list so that it
returns a list of integers only.'''

def filter_list(data:list)->list:
  '''Write a function that takes a list of elements and returns only the integers.'''
  Only_Integer = list()
  for item in data:
    if type(item) == int:
      Only_Integer.append(item)

  return Only_Integer


l = [1, 2, 3,'a', 'b', 'c', 4]
r = filter_list(l)
print(r)


'''Question2
Given a list of numbers, create a function which returns the list but with each element&#39;s
index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
number at index 1, etc...'''

def add_index(lst:list)->list:
  '''Given a list of numbers, create a function which returns the list but with each element&#39;s
  index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
  number at index 1, etc...'''
  result = list()
  for i in range(0,len(lst)):
    result.append(i+lst[i])

  return result


l = [1, 2, 3,4, 5]
r = add_index(l)
print(r)


'''Question3
Create a function that takes the height and radius of a cone as arguments and returns the
volume of the cone rounded to the nearest hundredth.'''


import math
def cone_volume(h:int,r:int)->float:
  '''Create a function that takes the height and radius of a cone as arguments and returns the
  volume of the cone rounded to the nearest hundredth.'''
  volumn = round((math.pi*(r**2)*h)/3,2)
  return volumn


print(cone_volume(3,2))


'''Write a function that gives the number of dots with its corresponding triangle number of the
sequence.'''


def trangle(numb:int)->int:
  '''Write a function that gives the number of dots with its corresponding triangle number of the
  sequence.'''
  no_of_dots = 0
  for i in range(1,numb+1):
    no_of_dots +=i
    
  return no_of_dots


print(trangle(215))


'''Question5
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
returns the missing number.'''

def missing_num(lst:list)->int:
  '''Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
  returns the missing number.'''
  lst.sort()
  missing_numb = 0
  for i in range(0,len(lst)):
    if i+1 != lst[i]:
      missing_numb = i+1
      break
    elif i+1 == len(lst):
       missing_numb = len(lst)+1
       break
  return missing_numb


l= [1,2,3,4,6,7,8,9,10,11,12]
print(missing_num(l))