# 1. Write a Python program to convert kilometers to miles?

Kilometer = float(input("Enter distance in kilometers"))
miles = Kilometer*0.62137119
print(f"{Kilometer} kilometer is = {miles} miles")


# 2. Write a Python program to convert Celsius to Fahrenheit?

Celsius = float(input("Enter temperature in Celsius"))
Fahrenheit = (Celsius*1.8) + 32
print(f"{Celsius} Celsius is = {Fahrenheit} Fahrenheit")


# 3. Write a Python program to display calendar?

import calendar
yy = int(input("Enter year in YYYY format"))
mm = int(input("Enter month in mm format"))
print(calendar.month(yy, mm))


# 4 Write a Python program to solve quadratic equation?
import math

a = float(input("Enter value of a ")) 
b = float(input("Enter value of b ")) 
c = float(input("Enter value of c ")) 

dis = b * b - 4 * a * c 
sqrt_val = math.sqrt(abs(dis)) 

if dis > 0: 
    print((-b + sqrt_val)/(2 * a)) 
    print((-b - sqrt_val)/(2 * a)) 
    
elif dis == 0: 
    print(-b / (2 * a)) 

else:
    print(- b / (2 * a), " + i", sqrt_val) 
    print(- b / (2 * a), " - i", sqrt_val) 


# 5 Write a Python program to swap two variables without temp variable?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Number before swap")
print(f"a = {a}")
print(f"b = {b}")

a = a+b
b = a-b 
a = a-b

print("Number after swap")
print(f"a = {a}")
print(f"b = {b}")