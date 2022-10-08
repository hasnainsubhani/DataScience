### 1  Write a Python program to print "Hello Python"?

print("Hello Python")

###2. Write a Python program to do arithmetical operations addition and division.?
num1 = int(input("Enter first number :"))
num2 = int(input("Enter first number :"))
operator = input("Enter what operation you want to do( addition or division) :")

if operator == "addition":
    result = num1 + num2
elif operator == "division":
    result = num1/num2
else:
    result = "No valid operation."

if  result == "No valid operation.":
    print(f"{result} ")
else:
    print(f"{operator} of {num1} and {num2} is = {result}")
     

### Write a Python program to find the area of a triangle?

base = float(input("Enter base of trangle :"))
height = float(input("Enter height of traingle :"))
Area = (base*height)/2
print(f"The area of a triangle is {Area}")


### 4. Write a Python program to swap two variables?

var1 = "Hasnain"
var2 = "Subhani"

print(f"var1 : {var1}  var2 : {var2}")

var = var1
var1 = var2
var2 = var

print(f"After swap var1 : {var1}  var2 : {var2}")


### 5. Write a Python program to generate a random number?
import random
numb = int(input("No of random number"))

random_number = random.randint(0,numb)