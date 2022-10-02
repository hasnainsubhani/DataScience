"""
1 What is indentation error? Why indentation is important? Give one simple example?

     Indentation is used to create a code block which will be ececuted after some coditional statement by shifting atleast one space.

     let take an example of IF statement 

     if True:
     print("line 1...")
     print("line 2")

     Here if statement does not have any line of code which will be executed, 
     here all three line is independet line of code hence compiler 
     will thow an indentation exception

     The correct statement is as follows
     if True:
        print("line 1...")
        print("line 2")

"""

"""
2 Correct the following code and write the comment where you made the correction?

class_started = bool(input("Hey friend, is class started?: [0-False/1-True]"))

if class_started: print("Since class started...") 
    print("Lets concentrate") 
else: 
    print("Since class is not started...") print("let's revise")

"""

# Since the class bool is a subclass of the class int 
# hence correct statement is as follows 
class_started = bool(int(input("Hey friend, is class started?: [0-False/1-True]")))

if class_started:
   print("Since class started...")
   print("Lets concentrate")
else:
   print("Since class is not started...")
   print("let's revise")


"""
3 Use if else condition to verify that dataype of input() method in python is always string.
"""

var = input("Please write any thing ")

var_string = "This is string type variable";

if type(var) == type(var_string):
  print("Data type of entered statement is string.")
else:
  print(f"Data type of entered statement is {type(var)}")


"""
Take 3 variables and assign integer values to them. Find the largest variable, by only using the if and else conditions.

"""

var1 = int(input("first number"))
var2 = int(input("second number"))
var3 = int(input("third number"))

if var1 > var2:
  if var1 > var3:
    print(f"Largest number between {var1}, {var2} and {var3} is {var1}")
  else:
    print(f"Largest number between {var1}, {var2} and {var3} is {var3}")
else:
  if var2 > var3:
    print(f"Largest number between {var1}, {var2} and {var3} is {var2}")
  else:
    print(f"Largest number between {var1}, {var2} and {var3} is {var3}")



"""
What would be the solution?

True

False

a = 6
b = 10
print( not ( not a == 10 or not b == 10) )
Ans - False



Find the answer as well as find out the reason behind the result? -

case 1:

  A = 5.0
  B = 10/2
  print(A is B)
Ans - False Reason - Both variable points two different location.*

case 2:

  A = 5.0
  B = int(10/2)
  print(A is B)
Ans - False Reason - Both variable points two different location.variable's memory location is assigned at runtime*

case 3:

  A = 5.0
  B = float(10/2)
  print(A is B)
Ans - False Reason - Both variable points two different location.variable's memory location is assigned at runtime*

"""


"""

7 Write a program that asks the user to enter a number. You should print out a message to the user, 
either “That number is divisible by either 3 or 5”, or “That number is not divisible by either 3 or 5”. 
Be sure to consider the data type of the input you are taking in from the user. Use a single if/else block to solve this problem.

"""

var = int(input("Please write any thing "))

if var%3 == 0 or var%5 ==0:
  print(f"That number {var} is divisible by either 3 or 5")
else:
  print(f"That number {var} is not divisible by either 3 or 5")



"""
8 Take user input for length and width. Then calculate the area of rectangle. 
Also print as per length and width whether its a square of rectangle.

"""

len = int(input("please enter length of ractangle (L):"))
wd = int(input("please enter width of ractangle (W):"))

shape = "ractangle"
ar = len*wd

if len==wd:
  print(f"since length {len} is equall to width {wd} hence it is square and it's area is {ar}")
  shape = "Square"
else:
  print(f"since length {len} is not equall to width {wd} hence it is ractangle and it's area is {ar}")

print(f"Area of {shape} is {ar}") 


"""
9 Take two variable radius_1 and radius_2 and calculate the area of circle_1 and circle_2. 
Also print which circle has large area. If area is equal then print area is equal.

"""

radius_1 = int(input("please enter radius_1:"))
radius_2 = int(input("please enter radius_2:"))

ar1 = 3.14*radius_1**2
ar2 = 3.14*radius_2**2

if ar1==ar2:
  print(f"Area {ar1} of circle having radius {radius_1} is equall to the area {ar2} of circle having radius {radius_2}")
else:
    if ar1>ar2:
      print(f"Area {ar1} of circle having radius {radius_1} is greater than the area {ar2} of circle having radius {radius_2}")
    else:
      print(f"Area of circle having radius {radius_1} is less than the  area {ar2} of circle having radius {radius_2}")


"""
10 Check whether a year is leap year or not. Use nested if...else to solve this problem. 
A leap year is exactly divisible by 4 except for century years (years ending with 00). 
The century year is a leap year only if it is perfectly divisible by 400.

"""

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