'''Question1
Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
number).
2. If the number cannot be divided evenly by 4, simply return the number.'''

'''Using list comprehension method'''

numb = 10
[x*10 if x%4 == 0 else x for x in range(1,numb+1)]

'''Using loop method '''

def Amplify(numb:'int')->list:
  '''
  Create a function that takes an integer and returns a list from 1 to the given number, where:
  1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
  number).
  2. If the number cannot be divided evenly by 4, simply return the number.
  '''
  result = list()
  for item in range(1,numb+1):
    if item%4==0:
      result.append(item*10)
    else:
      result.append(item)

  return result


l = Amplify(25)
print(l)



'''Question2
Create a function that takes a list of numbers and return the number that&#39;s unique.'''

def Unique(lst:'list')->int:
  '''
  Create a function that takes a list of numbers and return the number that's unique.
  '''
  for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
      if lst[i] == lst[j]:
        duplicate = lst[i]
        break;

  for items in lst:
    if items != duplicate:
      uni = items
      break
  return uni


l = [0,0,0,.77,0,0,0,0]
r = Unique(l)
print(r)



'''Question3
Your task is to create a Circle constructor that creates a circle with a radius provided by an
argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).'''

import math
class Circle_Constructor:
  def __init__(self,Radius):
    self.r = Radius
  
  def getArea(self):
    return math.pi*self.r**2

  def getPerimeter(self):
    return math.pi*self.r*2


obj = Circle_Constructor(5)
a = obj.getArea()
b = obj.getPerimeter()
print(f"Area of circle = {a}")
print(f"Perimeter of circle = {b}")


'''Question4
Create a function that takes a list of strings and return a list, sorted from shortest to longest.'''

def Sort_By_Length(lst:'list')->list:
  '''Create a function that takes a list of strings and return a list, sorted from shortest to longest.'''
  for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
      if len(lst[i])>len(lst[j]):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp

  return lst


l = ["Turning","Einstein","Jung"]
r = Sort_By_Length(l)
print(r)


'''Question5
Create a function that validates whether three given integers form a Pythagorean triplet. The
sum of the squares of the two smallest integers must equal the square of the largest number to
be validated.'''

def Pythagorean_Triplet(a:int,b:int,c:int)->bool:
  '''Create a function that validates whether three given integers form a Pythagorean triplet. The
  sum of the squares of the two smallest integers must equal the square of the largest number to
  be validated.'''
  lst = list()
  lst.append(a)
  lst.append(b)
  lst.append(c)
  for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
      if lst[i]>lst[j]:
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp

  
  if(int(lst[0])**2 + int(lst[1])**2 == int(lst[2])**2):
    PythagoreanTriplet = True
  else:
    PythagoreanTriplet = False
  return PythagoreanTriplet


print(Pythagorean_Triplet(1,2,3))