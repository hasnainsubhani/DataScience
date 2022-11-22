'''Question1
Write a function that takes a list and a number as arguments. Add the number to the end of
the list, then remove the first element of the list. The function should then return the updated
list.'''

def Next_In_Lines(_lst:list,numb:int)->list:
  '''Write a function that takes a list and a number as arguments. Add the number to the end of
  the list, then remove the first element of the list. The function should then return the updated
  list.'''
  _lst.append(numb)
  _lst.pop(0)
  return _lst



_lst = [1,2,3,4,5]
r = Next_In_Lines(_lst,6)
print(r)



'''Question2
Create the function that takes a list of dictionaries and returns the sum of people&#39;s budgets.'''

def Get_Budgets(Data:list)->float:
  '''Create the function that takes a list of dictionaries and returns the sum of people's budgets.'''
  Tot_budget = 0
  for item in Data:
    if type(item)==dict:
      Tot_budget += item['budget']

  return Tot_budget


data = [
{ 'name': 'John', 'age': 21, 'budget': 23000 },
{ 'name': 'Steve', 'age': 32, 'budget': 40000 },
{ 'name': 'Martin', 'age': 16, 'budget': 2700 }
]
r = Get_Budgets(data)
print(r)


'''Question3
Create a function that takes a string and returns a string with its letters in alphabetical order.'''

def Alphabet_Soup(string:str)->str:
  '''Create a function that takes a string and returns a string with its letters in alphabetical order.'''
  _string = list()
  for i in range(0,len(string)):
    _string.append(string[i])

  for i in range(0,len(_string)):
    for j in range(i+1,len(_string)):
      if _string[i] > _string[j]:
        temp = _string[i]
        _string[i] = _string[j]
        _string[j] = temp

  return ''.join(_string)


r = Alphabet_Soup("javascript")
print(r)


'''Question4
Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly.
What will be the value of your investment at the end of the 10 year period?
Create a function that accepts the principal p, the term in years t, the interest rate r, and the
number of compounding periods per year n. The function returns the value at the end of term
rounded to the nearest cent.'''

def compound_interest(p:float,t:int,r:float,n:int)->float:
  ''''''
  FA = p*( 1 + r/n)**(n*t)
  return FA


ci = compound_interest(100, 1, 0.05, 1)
print(ci)
