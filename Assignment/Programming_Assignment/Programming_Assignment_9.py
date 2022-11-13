#1. Write a Python program to check if the given number is a Disarium Number?

def isDisarium(numb:"int")->bool:
  '''Check the number is Disarium Number'''
  sum=0
  for i in range(len(str(numb))):
    sum = sum + int(str(numb)[i])**(i+1)
  if sum == numb:
    return True
  else:
    return False

isDisarium(135)

#2. Write a Python program to print all disarium numbers between 1 to 100?

def getDisarium_number(numb:"int")->list:
  '''return list of disarium number between 1 to numb'''
  lst = list()
  for n in range(1,numb):
   if isDisarium(n):
     lst.append(n)
  return(lst)

a = getDisarium_number(100)
print(a)

#3. Write a Python program to check if the given number is Happy Number?

def isHappyNumb(number:"int")->bool:
  '''Check the number is Happy Number'''
  numbs = set()
  sum=0
  while sum != number:
    #print(f"numb = {number}")
    for i in range(len(str(number))):
      sum = sum + int(str(number)[i])**2

    #print(f"Number={number} and Sum={sum}") 
    if sum == 1:
      return True
    elif sum in numbs:
      return False
    else:
      numbs.add(number)
      number = sum
      sum=0

a = isHappyNumb(94)
print(a)

#4. Write a Python program to print all happy numbers between 1 and 100?

def GetHappy_Number(numb:"int")->list:
  '''return list of happy number between 1 to numb'''
  lst = list()
  for n in range(1,numb):
   if isHappyNumb(n):
     lst.append(n)
  return(lst)

a = GetHappy_Number(100)
print(a)

#5. Write a Python program to determine whether the given number is a Harshad Number?

def IsHarshad(numb:"int")->bool:
  '''Check the number is Harshad Number'''
  sum=0
  for i in range(len(str(numb))):
    sum = sum + int(str(numb)[i])
  if numb%sum==0:
    return True
  else:
    return False

a= IsHarshad(21)
print(a)

#6. Write a Python program to print all pronic numbers between 1 and 100?

def GetHarshad_Number(numb:"int")->list:
  '''return list of happy number between 1 to numb'''
  lst = list()
  for n in range(1,numb):
   if IsHarshad(n):
     lst.append(n)
  return(lst)


a = GetHarshad_Number(100)
print(a)