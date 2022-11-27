'''Question1
Create a function that takes a string and returns a string in which each character is repeated
once.'''

def double_char(string:str)->str:
  '''Create a function that takes a string and returns a string in which each character is repeated
  once.'''
  _result = list()
  for i in range(0,len(string)):
    _result.append(string[i]*2)

  return ''.join(_result)


print(double_char('hasnain'))


'''Question2
Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
if another variable type is given.'''


def reverse(val:bool)->str:
  '''Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
  if another variable type is given.'''
  reverse = "boolen expected"
  if type(val)==bool:
    if val == True:
      reverse = False
    else:
      reverse = True
      
  return reverse

print(reverse(False))


'''Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it n
number of times. The paper starts off with a thickness of 0.5mm.'''


def num_layer(n:int)->float:
  '''Create a function that returns the thickness (in meters) of a piece of paper after folding it n
  number of times. The paper starts off with a thickness of 0.5mm.'''
  thickness = .5*.001
  total_thickness = thickness*(2**n)
  return str(total_thickness)+"m"

print(num_layer(21))


'''Create a function that takes a single string as argument and returns an ordered list containing
the indices of all capital letters in the string.'''

def index_of_caps(string:str)->list:
  '''Create a function that takes a single string as argument and returns an ordered list containing
  the indices of all capital letters in the string.'''
  _index = list()
  for i in range(0,len(string)):
    if(string[i].islower()==False):
      _index.append(i)

  return _index

print(index_of_caps('STRIKE'))