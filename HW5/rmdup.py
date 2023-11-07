# removes duplicates from data.
# This function keeps the last occurence of each element
# and preserves order.
# So rmdup([1,2,3,2,1,4,2]) should return [3,1,4,2]

from datetime import datetime
import random
import time

def printFloat(data):
    for i in data:
        print("%2.5f" %i,",",sep="",end="")
    print()

def generateArray(sz,num):
  data = []
  for i in range(sz):
    data.append(random.randint(0,num))
  return data

def rmdup(data):
    # Write me
    res = []
    rec = set()
    for i in range(len(data)-1,-1,-1):
      if data[i] not in rec:
        res.append(data[i])
        rec.add(data[i])
    res.reverse() 
    return res
  
if __name__=='__main__':
  size = 4096
  size_rec = []
  cnt = 1
  while(cnt*size<=4194304):
    size_rec.append(cnt*size)
    cnt*=2
  print(size_rec)
  
  data_many,data_moderate,data_rare = [],[],[]
  
  # many duplicates
  for sz in size_rec:
    arr_many = generateArray(sz,sz/2048)
    #start = datetime.now()
    start = time.perf_counter()
    ans = rmdup(arr_many)
    #end = datetime.now()
    #start = time.perf_counter()
    end = time.perf_counter()
    data_many.append(end-start)
  printFloat(data_many)
  
  #moderate duplicates
  for sz in size_rec:
    arr_moderate = generateArray(sz,sz/16)
    #start = datetime.now()
    start = time.perf_counter()
    ans = rmdup(arr_moderate)
    #end = datetime.now()
    end = time.perf_counter()
    data_moderate.append(end-start)
  printFloat(data_moderate)
  
  #rare duplicates
  for sz in size_rec:
    arr_rare = generateArray(sz,sz*4)
    #start = datetime.now()
    start = time.perf_counter()
    ans = rmdup(arr_rare)
    #end = datetime.now()
    end = time.perf_counter()
    data_rare.append(end-start)
  printFloat(data_rare)  




        
