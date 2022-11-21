'''Question1
Create a function that takes three parameters where:
 x is the start of the range (inclusive).
 y is the end of the range (inclusive).
 n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.'''

def List_Operation(x:int,y:int,n:int)->list:
  '''Return an ordered list with numbers in the range that are divisible by the third parameter n.
     Return an empty list if there are no numbers that are divisible by n.'''
  lst = list()
  for i in range(x,y+1):
    if i%n == 0:
      lst.append(i)
  return lst


r = List_Operation(15,20,7)
print(r)



'''Question2
Create a function that takes in two lists and returns True if the second list follows the first list
by one element, and False otherwise. In other words, determine if the second list is the first
list shifted to the right by 1.'''


def Simon_Says(lst1:list,lst2:list)->bool:
  '''Create a function that takes in two lists and returns True if the second list follows the first list
    by one element, and False otherwise. In other words, determine if the second list is the first
    list shifted to the right by 1.'''
  for i in range(0,len(lst1)):
    if i < len(lst1)-1 and lst1[i]==lst2[i+1]:
      simon_says = True
      break
    else:
      simon_says = False

  return simon_says

r = Simon_Says([1,2,3,4,5],[5,5,1,2,3])
print(r)


'''Question3
A group of friends have decided to start a secret society. The name will be the first letter of
each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.'''

def Society_Name(lst:list)->str:
  '''A group of friends have decided to start a secret society. The name will be the first letter of
     each of their names, sorted in alphabetical order.
     Create a function that takes in a list of names and returns the name of the secret society.'''
  lst.sort()
  Result=list()

  for item in lst:
    Result.append(item[0])
  
  return ''.join(Result)


lst = ['Phoebe', 'Chandler', 'Rechal','Ross','Monica','Joey']
r = Society_Name(lst)
print(r)


'''Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it&#39;s an &quot;isogram&quot;.'''

def Is_Isogram(string:str)->bool:
  '''An isogram is a word that has no duplicate letters. Create a function that takes a string and
  returns either True or False depending on whether or not it&#39;s an &quot;isogram&quot;.'''
  Is_Isogram = True
  for i in range(0,len(string)):
    for j in range(i+1,len(string)):
      if string[i].lower() == string[j].lower():
        Is_Isogram = False
        break
  return Is_Isogram


r = Is_Isogram('Consecutive')
print(r)


'''Question5
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.'''

def Is_In_Order(string:str)->bool:
  '''Create a function that takes a string and returns True or False, depending on whether the
  characters are in order or not.'''
  Is_In_Order = True
  for i in range(0,len(string)):
    if i<len(string)-1 and string[i] > string[i+1]:
      Is_In_Order = False

  return Is_In_Order
  

r = Is_In_Order('xyzz')
print(r)