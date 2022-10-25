#1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fibonacci_recur(n):
  if n <= 1:
    return n
  else:
    return(fibonacci_recur(n-1) + fibonacci_recur(n-2))

numb = int(input("Please enter positive number \n to get fibonacci series "))

# check if the number of terms is valid
if numb <= 0:
  print("Input is invalid !!")
else:
  print(f"Fibonacci series upto {numb} :")
  for i in range(numb):
    print(fibonacci_recur(i+1))


#2. Write a Python Program to Find Factorial of Number Using Recursion?

def factorial_recur(n):
  if n <= 1:
    return n
  else:
    return(factorial_recur(n-1)*n)

numb = int(input("Please enter positive number \n to get factorial "))
if numb <= 0:
  print("Input is invalid !!")
else:
  print(factorial_recur(numb))


#3. Write a Python Program to calculate your Body Mass Index?

def Bmi(height,weight):
  BMI = weight/(height/100)**2
  return BMI

height = int(input("Please enter height in centimeter "))
weight = int(input("Please enter weight in kg "))
_BMI = Bmi(height,weight)
print(f"BMI for height {height} cm and weight {weight} kg is {_BMI}")


#4. Write a Python Program to calculate the natural logarithm of any number?

import math
def _log(numb,base):
  if numb > 10:
    return math.log1p(numb)
  else:
    return math.log(numb,base)

numb = int(input("Please enter the positive number to find log "))
if numb < 10:
  base = int(input("Please enter the base of log "))
  
ln = _log(numb,base)
print(f"Log of number {numb} of base {base} is : {ln}")

#5. Write a Python Program for cube sum of first n natural numbers?

def sum_cube_natural_numb(numb):
  sum = 0
  for i in range(1,numb+1):
    sum+=i**3
  return sum

numb = int(input("Enter number till to get sum of cube of natural number "))
sum_cube_natural_numb(numb)