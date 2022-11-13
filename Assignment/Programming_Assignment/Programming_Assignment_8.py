import numpy as np

def get_matrix_input():
  R = int(input("Number of rows"))
  C = int(input("Number of columns:"))
  no_of_element = R*C
  print(f"Please enter {no_of_element} element in a single line (separated by space): ")
  _input = input()
  entries = list(map(int,_input.split()))
  matrix = np.array(entries).reshape(R, C)
  return matrix



#1. Write a Python Program to Add Two Matrices?

def matrix_add(matrix_1,matrix_2):

  ar1 = np.matrix(matrix_1)
  ar2 = np.matrix(matrix_2)
  _row = ar1.shape[1]
  _col = ar2.shape[0]
  if ar1.shape[1] == ar2.shape[1] and ar1.shape[0] == ar2.shape[0]:
    res = np.matrix(np.zeros((_row,_col)))  
    for x in range(_row):
      for y in range(_col):
          res[x, y] = ar1[x, y] + ar2[x, y]
    return res
  else:
    return "Inorder to add two matrix, both matrix should have same shape/order"


matrix_1 = get_matrix_input()
matrix_2 = get_matrix_input()
print(matrix_add(matrix_1,matrix_2))

#2. Write a Python Program to Multiply Two Matrices?

def matrix_mult(matrix_1,matrix_2):
  ar1 = matrix_1
  ar2 = matrix_2
  _row = ar1.shape[0]
  _col = ar1.shape[1]
  _row_1 = ar2.shape[0]
  _col_1 = ar2.shape[1]
  #print(f"{_row},{_col_1}")
  result = np.matrix(np.zeros((_row,_col_1))) 
  #print(result)

  for i in range(len(ar1)):
    # iterating by column by ar2
    sum = 0
    for j in range(len(ar2[0])):
      # iterating by rows of ar2
      for k in range(len(ar2)):
        result[i][j] += ar1[i][k] * ar2[k][j]

  return(result)  

matrix_1 = get_matrix_input()
matrix_2 = get_matrix_input()
print(matrix_mult(matrix_1,matrix_2))


#3. Write a Python Program to Transpose a Matrix?

def zero_list(rows,col):
  lst = list()
  for i in range(rows):
    _lst = list()
    for j in range(col):
      _lst.append(0)
    lst.append(_lst)
  return lst


def matrix_transpose(matrix_1):
   ar1 = matrix_1
   result = zero_list(len(ar1[0]),len(ar1))
   for i in range(len(ar1)):
     for j in range(len(ar1[0])):
       result[j][i] = ar1[i][j]
   return result

matrix_transpose([[12,7,3],[4,5,8]])


#4. Write a Python Program to Sort Words in Alphabetic Order?

def sort_string(string:"str")->str:
  '''sort words of a string in alphabetically order'''
  words = [word.lower() for word in string.split()]
  words.sort()
  return words


#5. Write a Python Program to Remove Punctuation From a String?

def remove_puncutaion(string:"str")->str:
  ''' returns string without puntuation'''
  punctuations = ''';:'"\,<>./?@#$%^&*_~!()-[]{}'''
  result = ""
  for c in string:
    if c not in punctuations:
      result = result + c
  return result