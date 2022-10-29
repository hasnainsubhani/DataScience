#1. Write a Python Program to find sum of array?

def sum_of_array(arr):
  sum = 0
  for i in range(0,len(arr)):
    sum = sum+arr[i]
  return sum

import array
arr = array.array('i', [1, 2, 3, 1, 5])
sum = sum_of_array(arr)
print(f"sum of {arr} is {sum}")

#2. Write a Python Program to find largest element in an array?

def largest_val_array(arr):
  largest = arr[0]
  for i in range(1,len(arr)):
    if largest < arr[i]:
      largest = arr[i]
  return largest

import array
arr = array.array('i', [1, 2, 3, 1, 5])
largest = largest_val_array(arr)
print(f"largest element in {arr} is {largest}")


#3 Write a Python Program for array rotation?

def Rotate_array(arr):
  _arr = array.array('i')
  j=0
  for i in range(len(arr)-1,-1,-1):
    _arr.append(arr[i])
    j= j+1
  return _arr

import array
arr = array.array('i', [1, 2, 3, 1, 5])
print(Rotate_array(arr))

print(f"After rotating {arr} new { Rotate_array(arr)}")


#4. Write a Python Program to Split the array and add the first part to the end?

import array
arr = [1, 2, 3, 1, 5]
_arr = []
_arr = arr[:int(len(arr)/2)]
for i in range(0,len(_arr)):
  arr.append(_arr[i])
print(arr)


#5. Write a Python Program to check if given array is Monotonic?

def isMonotonic(arr):
    x, y = [], []
    x.extend(arr)
    y.extend(arr)
    x.sort()
    y.sort(reverse=True)
    if(x == arr or y == arr):
        return True
    return False


arr = [5,4,3,2,1]

print(isMonotonic(arr))