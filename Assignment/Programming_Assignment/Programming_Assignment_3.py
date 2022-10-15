# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

numb = int(input("Enter a number"))
if(numb == 0):
    print("Entered number {numb} is zero")
elif(numb > 0):
    print("Entered number {numb} is positive")
elif(numb < 0):
    print("Entered number {numb} is negative")


# 2. Write a Python Program to Check if a Number is Odd or Even?

numb = int(input("Enter a number"))
if(numb % 2 == 0):
    print("Entered number {numb} is even")
else:
    print("Entered number {numb} is odd")


# 3. Write a Python Program to Check Leap Year?

var = int(input("Please year in 'yyyy' format "))

if var%100 == 0:
  if var%400 == 0:
    print(f" Year {var} is a leap year")
  else:
    print(f" Year {var} is not a leap year")
elif var%4==0:
    print(f" Year {var} is a leap year")
else:
    print(f" Year {var} is not a leap year")



# 4. Write a Python Program to Check Prime Number?

num = int(input("Enter a number: "))

if num > 1:
   for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
   else:
        print(num, "is a prime number")
   
else:
   print(f"{num} is not a prime number")


# 5 . Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

number = int(input("Enter a number: "))

for num in range(2,number):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            break
    else:
        print(num, "is a prime number")