import time
import sys
import functools
import os

#@functools.cache
def getCoin(i,j,h,w):
  if i == h-1 and j == w-1:
    return gird[i][j]
  if i == h-1:
    ways[i][j] = -1
    return gird[i][j] + getCoin(i, j+1,h,w)
  if j == w-1:
    ways[i][j] = 1
    return gird[i][j] + getCoin(i+1, j,h,w)
  
  n,w = getCoin(i+1, j,h,w), getCoin(i, j+1,h,w)
  if n > w:
    ways[i][j] = 1
  else:
    ways[i][j] = -1
  return gird[i][j] + max(n,w)

if __name__ == '__main__':

  # gird = []
  # with open(sys.argv[1]) as f:
  #   for line in f.readlines():
  #     gird.append([int(val) for val in line.strip().split(',')])
  # print(gird)
  # h,w = len(gird), len(gird[0])
  

  
  gird = [[0,4,1,3,11],
            [8,2,4,5,6],
            [1,7,3,9,0],
            [0,12,1,2,0]]
  h,w = len(gird), len(gird[0])
  ways = [[0 for _ in range(w)] for _ in range(h)]

  
  direction = []
  time_rec = []
  for i in range(15):
    s = time.perf_counter()
    coin_num = getCoin(0,0,h,w)
    e = time.perf_counter()
    time_rec.append(e-s)
    #getCoin.cache_clear()
  
  i,j = 0,0
  while ways[i][j]!=0 and i<h and j <w:
    if ways[i][j] == 1:
      direction.append('N')
      i += 1
    else:
      direction.append('W')
      j += 1
  direction.reverse()
  print(''.join(direction))
  print(coin_num)
  print(int(sum(time_rec)/10*pow(10,9)))
    
    


  