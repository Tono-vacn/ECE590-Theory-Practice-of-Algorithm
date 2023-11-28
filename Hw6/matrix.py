import time
import sys
import functools
import os

@functools.cache
def matcal(s,e):
  if s==e:
    return mat[e],0
  if s+1==e:
    return (mat[s],mat[e]),size[s]*size[s+1]*size[e+1]
  min_num = float('inf')
  idx = -1
  for i in range(s,e):
    l1,s1 = matcal(s,i)
    l2,s2 = matcal(i+1,e)
    min_num = min(min_num, s1+s2+size[s]*size[i+1]*size[e+1])
    if min_num == s1+s2+size[s]*size[i+1]*size[e+1]:
      idx = i
  return (matcal(s,idx)[0],matcal(idx+1,e)[0]),min_num

  

if __name__ == '__main__':

  grid = []
  with open(sys.argv[1]) as f:
    for line in f.readlines():
      grid.append([val for val in line.strip().split(',')])
  #grid = [['A', 10, 20], ['B', 20, 30], ['C', 30, 40], ['D', 40, 30]]
  # grid = [['A',7,3],
  # ['B',3,5],
  # ['C',5,4]]
  
  
  # grid = [  ['A',40,20],
  # ['B',20,30],
  # ['C',30,10],
  # ['D',10,30]]
  
  # print(grid)
  mat = [line[0] for line in grid]
  l = len(mat)
  size = [int(grid[0][1])]
  size.extend([int(grid[i][2]) for i in range(0,l)])
  #h,w = len(gird), len(gird[0])

  op_num,c = matcal(0,l-1)
  
  print(op_num)
  print(c)
  
  # direction = []
  time_rec = []
  for i in range(15):
    s = time.perf_counter()
    op_num,c = matcal(0,l-1)
    e = time.perf_counter()
    time_rec.append(e-s)
    matcal.cache_clear()
    
  # for val in time_rec:
  #   print(val*pow(10,9))
  
  #print(time_rec)
  print(int(sum(time_rec)/15*pow(10,9)))
  
    
    


  