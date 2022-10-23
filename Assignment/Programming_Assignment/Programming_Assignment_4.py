#1. Write a Python Program to Find the Factorial of a Number?

def factorial(numb):
  factorial = 1
  for i in range(1,numb + 1):
    factorial = factorial * i
  
  return factorial

numb = int(input("Please enter number "))
fact = factorial(numb)
print(fact)


#2. Write a Python Program to Display the multiplication Table?

def multiplication_table(numb):
  lst = list()
  for i in range(0,10):
    lst.append(numb*(i+1))
  return lst
  
numb = int(input("Please enter number till you want \n multiplication table "))

for i in range(2,numb+1):
  print(multiplication_table(i))


#3. Write a Python Program to Print the Fibonacci sequence?


def Fibonacci(numb):
  fib = list()
  prev_numb = 1
  next_num = 0
  
  for i in range(0,numb+1):
    fib.append(prev_numb + next_num)
    prev_numb = next_num
    next_num = fib[i]
  return fib

numb = int(input("Get Fibonacci sequance of number  "))
_fib = Fibonacci(numb)
for item in _fib:
  print(item)



#4. Write a Python Program to Check Armstrong Number?

def isarmstrong(numb):
  isarmstrong = False
  sum = 0
  for i in range(0,len(str(numb))):
    sum += int(str(numb)[i])**len(str(numb))

  if numb == sum:
    isarmstrong = True

  return isarmstrong

numb = int(input("Enter number to check armstrong "))

if isarmstrong(numb):
  print(f"Entered number{numb} is armstrong number.")
else:
  print(f"Entered number{numb} is not armstrong number.")


#5. Write a Python Program to Find Armstrong Number in an Interval?

numb_from = int(input("Enter number to get armstrong \n from"))
numb_to = int(input(" To"))
print(f"\n\n The armstrong number between {numb_from} and {numb_to} is as follows\n")
for numb in range(numb_from,numb_to):
  if isarmstrong(numb):
    print(numb)


#6. Write a Python Program to Find the Sum of Natural Numbers?

def sum_natural_numb(numb):
  sum = 0
  for i in range(1,numb+1):
    sum+=i
  return sum

numb = int(input("Enter number till to get sum of natural number "))
sum_natural_numb(numb)