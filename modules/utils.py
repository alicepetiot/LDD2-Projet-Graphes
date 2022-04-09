import random

def remove_all(l, x):
  '''
  output : 'a list
  removes all the occurences of x in l
  '''
  for i in range(len(l)):
    if x in l:
      l.remove(x)
  return l

def count_occurrences(l,x):
  '''
  output : int
  counts all the occurences of x in l
  '''
  cpt = 0
  for i in l:
    if i == x:
      cpt = cpt + 1
  return cpt

def random_int_list(n, bound):
  '''
  output : int list
  generates a list with random int between 0 and bound of the lengh n 
  '''
  l = []
  for i in range(n):
    int_alea = random.randint(0,bound)
    l.append(int_alea)
  return l

def print_matrix(matrix):
  '''
  display a matrix
  '''
  for i in range(len(matrix)):
    print(matrix[i])
  print("\n")

def random_matrix(n,bound,null_diag=False,form="free"):
  matrix = []
  '''generate a matrix of size n.n with random int between 0 and bound'''
  for i in range(n):
    ligne = random_int_list(n,bound)
    matrix.append(ligne)
    if null_diag:
      matrix[i][i] = 0

  rand2 = random.randint(0,1)
  for i in range(n):
    for j in range(n):
      if form=="symetric":
        matrix[i][j] = matrix [j][i]       
      elif form=="oriented":    
        rand = random.randint(0,1)
        if rand == 0 and matrix[i][j] != 0:
          matrix[j][i] = 0
        elif rand == 1 and matrix [j][i] != 0:
          matrix[i][j] = 0
      elif form=="triangular":
        if rand2 == 0 and i>j:
            matrix[i][j] = 0
        elif rand2 == 1 and j>i:
            matrix[i][j] = 0
  return matrix