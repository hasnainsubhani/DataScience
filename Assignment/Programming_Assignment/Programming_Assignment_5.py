#1. Write a Python Program to Find LCM?

def lcm(numbers):
  factor = list()
  for i in range(0,len(numbers)):
    factor_1 = list()
    for j in range(1,51):
      factor_1.append(numbers[i]*j)
    factor.append(factor_1)
  
  common_factor = list()

  for item in factor[0]:
    common = 0
    for i in range(1,len(factor)):
      for j in range(0,50):
        if item == factor[i][j]:
          common = common+1

    if common == len(factor)-1:
      common_factor.append(item)
  return common_factor[0]




_numbers = list()
factor_1 = list()
for _ in range(int(input())):
  _numbers.append(int(input()))

print(f"LCM of {_numbers} is {lcm(_numbers)}")



#2. Write a Python Program to Find HCF?

def Prime_Number(number):
  prime_numb = list()
  for num in range(2,number):
      for i in range(2, int(num/2)+1):
          if (num % i) == 0:
              break
      else:
        prime_numb.append(num)
  return prime_numb 


def Prime_factor(numb):
  prime_factor = list()
  prime_numb = Prime_Number(numb)
  getfactor = True
  while getfactor:
    for i in range(0,len(prime_numb)):
      if numb%prime_numb[i]==0:
        numb = numb/prime_numb[i]
        prime_factor.append(prime_numb[i])
        if numb == 1:
          getfactor = False

  return prime_factor


factor = list()
numbers = list()
factor_1 = list()
for i in range(int(input("Enter number count whose \n HCF you want to find "))):
        numbers.append(int(input(f"Enter number {i}  ")))


for i in range(0,len(numbers)):
  _primefactor = Prime_factor(numbers[i])
  #print(_primefactor)
  factor.append(_primefactor)

common_factor = list()
for item in factor[0]:
    #print(f"Item = {item}")
    common = 0
    for i in range(1,len(factor)):
      for j in range(0,len(factor[i])):
        #print(f"factor = {factor[i][j]}")
        if item == factor[i][j]:
          common = common+1
          break

    #print(f"common {common} and length {len(factor)-1}")

    if common == len(factor)-1:
      common_factor.append(item)
      common == 0
      #print(f"common_factor is {common_factor}")
HCF = 1
for item in common_factor:
  HCF = HCF*item

print(f"HCF of {numbers} is {HCF}")


#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

def Decimal_to_BOH_Converter(numb,type):
  if type == "hexadecimal":
    _no = 16
  elif type == "octal":
    _no = 8
  else:
    _no = 2

  factor = list()
  getfactor = True
  
  while getfactor:
    factor.append(numb%_no)
    numb = numb//_no
    if numb < _no:
      if numb == 10:
        factor.append("A")
      elif numb == 11:
        factor.append("B")
      elif numb == 12:
        factor.append("C")
      elif numb == 13:
        factor.append("D")
      elif numb == 14:
        factor.append("E")
      elif numb == 15:
        factor.append("F")
      else:  
        factor.append(numb)
      getfactor = False
  return reversed(factor)

numb = int(input("Enter the number you want to convert "))
typ = input("into type binary,octal or hexadecimal ")
lst = list(Decimal_to_BOH_Converter(numb,typ))
for i in lst:
  if i == 10:
    print("A", end='')
  elif i == 11:
    print("B", end='')
  elif i == 12:
    print("C", end='')
  elif i == 13:
    print("D", end='')
  elif i == 14:
    print("E", end='')
  elif i == 15:
     print("F", end='')
  else: 
    print(i, end='')


#4. Write a Python Program To Find ASCII value of a character?

_char = int(input("Enter the character to get ASCII value  "))
print(f"The ASCII value of {_char} is {ord(_char)}")


#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def _sum(numb):
  total = 0
  for item in numb:
    total = total + item
  return total

def _multiply(numb):
  total = 1
  for item in numb:
    total = total*item
  return total

def _Calci():
  numbers = list()
  opt = input("what do you want to do add,subtract,multiply or divide ")
  if opt == "add":
    for i in range(int(input("How many numbers do you want to add "))):
      numbers.append(int(input(f"please enter number_{i+1} ")))
    print(f"sum of {numbers} is {_sum(numbers)}")
  elif opt == "subtract":
    mumb_1 = int(input("Please enter first number "))
    mumb_2 = int(input("Please enter second number "))
    print(f"Result of {mumb_1} - {mumb_2} is {mumb_1 - mumb_2}")
  elif opt == "divide":
    mumb_1 = int(input("Please enter first number "))
    mumb_2 = int(input("Please enter second number "))
    print(f"Result of {mumb_1} / {mumb_2} is {mumb_1 / mumb_2}")
  elif opt == "multiply":
    for i in range(int(input("How many numbers do you want to multiply "))):
      numbers.append(int(input(f"please enter number_{i+1} ")))
    print(f"Multiplication of {numbers} is {_multiply(numbers)}")
  else:
    print("Invalid operation")

_Calci()