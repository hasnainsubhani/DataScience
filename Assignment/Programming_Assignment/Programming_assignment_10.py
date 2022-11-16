
def List_Sort(lst :'list',order:'str' = 'asc')->list:
  '''returns sorted list in asc or desc order based on order passed by user default is asc order'''
  for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
      if order == 'asc':
        if lst[i] > lst[j]:
          temp = lst[i]
          lst[i] = lst[j]
          lst[j] = temp
      else:
          if lst[i] < lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
  return lst

#1. Write a Python program to find sum of elements in list?

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for item in lst:
  sum = sum+item
print(sum)

#2. Write a Python program to Multiply all numbers in the list?

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multi = 1
for item in lst:
  multi = multi*item
print(multi)


#3. Write a Python program to find smallest number in a list?

def Smallest_Number(lst :'list')->list:
  '''returns smallest number in a list'''
  sorted_list = List_Sort(lst)
  return sorted_list[0]

lst = [4,5,6,2,3,9,10,7,8]
s = Smallest_Number(lst)
print(s)

#4. Write a Python program to find largest number in a list?

def Largest_Number(lst :'list')->list:
  '''returns largest number in a list'''
  sorted_list = List_Sort(lst,order='Desc')
  return sorted_list[0]

lst = [4,5,6,2,3,9,10,7,8]
s = Largest_Number(lst)
print(s)

#6. Write a Python program to find N largest elements from a list?

def Nlargest_Number(lst :'list',n:'int')->list:
  '''returns N largest number in a list'''
  sorted_list = List_Sort(lst,order='Desc')
  if n >= len(lst):
    n = len(lst)
  return sorted_list[n-1]


  
#5. Write a Python program to find second largest number in a list?


lst = [4,5,6,2,3,9,10,7,8]
l = Nlargest_Number(lst,2)
print(l)

#7. Write a Python program to print even numbers in a list?

def Even_Numb(lst :'list')->list:
  '''returns even numbers list in a list'''
  l = lambda x: (x % 2 == 0)
  return list(filter(l,lst))

#8. Write a Python program to print odd numbers in a List?

def Odd_Numb(lst :'list')->list:
  '''returns odd numbers list in a list'''
  l = lambda x: (x % 2 != 0)
  return list(filter(l,lst))

lst = [4,5,6,2,3,9,10,7,8]
print(Odd_Numb(lst))

#9. Write a Python program to Remove empty List from List?

def RemoveBlankList(lst:'list')->list:
  '''Removes empty List from List?'''
  result = list()
  for item in lst:
    if type(item)==list:
      if len(item)>0:
        result.append(item)
    else:
      result.append(item)
  return result;


lst = [4,[5,6,2],[],3,9,[10,7],8,[]]
s = RemoveBlankList(lst)
print(s)


#10. Write a Python program to Cloning or Copying a list?

def List_Clone(lst):
    lst_copy = lst[:]
    return lst_copy

lst = [4,[5,6,2],[],3,9,[10,7],8,[]]
s = List_Clone(lst)
print(s)


#11. Write a Python program to Count occurrences of an element in a list?

def ListItem_Count(lst:'list')->None:
  '''Count occurrences of an element in a list'''
  numbs = set()
  for i in range(0,len(lst)):
      if lst[i] not in numbs:
        cnt = lst.count(lst[i])
        numbs.add(lst[i])
        print(f"{lst[i]} is {cnt} times in list")


lst = [4,5,6,2,4,4,10,7,8]
ListItem_Count(lst)