# This function takes 2 matricies (as lists of lists)
# and performs matrix multiplication on them.
# Note: you may not use any matrix multiplication libraries.
# You need to do the multiplication yourself.
# For example, if you have
#     a=[[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [4,0,7]]
#     b=[[1,2],
#        [3,4],
#        [5,6]]
#  Then a has 4 rows and 3 columns.
#  b has 3 rows and 2 columns.
#  Multiplying a * b results in a 4 row, 2 column matrix:
#  [[22, 28],
#   [49, 64],
#   [76, 100],
#   [39, 50]]

from datetime import datetime
import random
import time

def generateMatrix(szr,szc,num):
  data = []
  for i in range(szr):
    data.append([])
    for j in range(szc):
      data[i].append(random.randint(0,num))
  return data

def printInt(data):
    for i in data:
        print("%7d" %i,",",sep="",end="")
    print()
    
def printFloat(data):
    for i in data:
        print("%2.5f" %i,",",sep="",end="")
    print()

def matrix_mul(a,b):
    assert(len(a[0])==len(b))
    res = [[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
      for j in range(len(b[0])):
        for k in range(len(a[0])):
          res[i][j]+=a[i][k]*b[k][j]
    return res
    # Write me
    #return a

if __name__=='__main__':
    #generate data size:
    size = 4
    size_rec = []
    cnt = 1
    while(cnt*size<=512):
      size_rec.append(cnt*size)
      cnt*=2
    printInt(size_rec)
    
    data_many,data_square,data_few = [],[],[]
    # case many
    for sz in size_rec:
      arr_many = generateMatrix(4*sz,sz,10)
      arr_many2 = generateMatrix(sz,sz//4,10)
      start = time.perf_counter()
      ans = matrix_mul(arr_many,arr_many2)
      #end = datetime.now()
      end = time.perf_counter()
      data_many.append(end-start)
    printFloat(data_many)
    
    # case square
    for sz in size_rec:
      arr_moderate = generateMatrix(sz,sz,10)
      arr_moderate2 = generateMatrix(sz,sz,10)
      #start = datetime.now()
      start = time.perf_counter()
      ans = matrix_mul(arr_moderate,arr_moderate2)
      #end = datetime.now()
      end = time.perf_counter()
      data_square.append(end-start)
    printFloat(data_square)
    
    # case few
    for sz in size_rec:
      arr_rare = generateMatrix(sz//4,sz,10)
      arr_rare2 = generateMatrix(sz,sz*4,10)
      #start = datetime.now()
      start = time.perf_counter()
      ans = matrix_mul(arr_rare,arr_rare2)
      #end = datetime.now()
      end = time.perf_counter()
      data_few.append(end-start)
    printFloat(data_few)
      