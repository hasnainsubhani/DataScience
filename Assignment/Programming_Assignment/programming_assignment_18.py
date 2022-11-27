'''Question 1
Create a function that takes a list of non-negative integers and strings and return a new list
without the strings.'''

def reverse(string:str)->str:
  return string[::-1].swapcase()


string = 'Hasnain'
print(reverse(string))



'''Question 2
The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
opposite case.'''


string = 'writeyourcodehere'
first,*middle,last = 'writeyourcodehere'
print(first)
print(''.join(middle))
print(last)


'''Your task is to unpack the list writeyourcodehere into three variables, being first,
middle, and last, with middle being everything in between the first and last element. Then
print all three variables.'''


string = 'writeyourcodehere'
first,*middle,last = 'writeyourcodehere'
print(first)
print(''.join(middle))
print(last)


'''Question 4
Write a function that calculates the factorial of a number recursively.'''

def factorial(numb:int)->int:
  '''Question 4
  Write a function that calculates the factorial of a number recursively.'''
  if (numb==1 or numb==0):
        return 1
  else:
    return numb*factorial(numb-1)

print(factorial(5))