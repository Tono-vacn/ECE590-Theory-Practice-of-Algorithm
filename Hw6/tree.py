import time
import sys
import functools
import collections
class TreeNode:
    def __init__(self, val, freq, left, right):
        self.val=val
        self.freq=freq
        self.left=left
        self.right=right
        self.cost = None
        pass
    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        left = str(self.left) if self.left is not None else '()'
        right = str(self.right) if self.right is not None else '()'
        return '({} {} {})'.format(self.val,left,right)
        
    def computeCost(self):
        if self.cost is not None:
            return self.cost
        def helper(n,depth):
            if n is None:
                return 0
            return depth * n.freq + helper(n.left, depth+1) + helper(n.right, depth +1)
        self.cost = helper(self, 1)
        return self.cost
    pass
pass

# Your code here.
@functools.cache
def buildTree(s,e,height):
  if e<s:
    return None,0
  if e==s:
    return TreeNode(kl[s],vl[s],None,None),height*vl[s]
  min_val = float('inf')
  idx = -1
  for i in range(s,e+1):
    l,r = buildTree(s,i-1,height+1),buildTree(i+1,e,height+1)
    min_val = min(min_val,l[1]+r[1]+vl[i]*height)
    idx = i if min_val == l[1]+r[1]+vl[i]*height else idx
  left = buildTree(s,idx-1,height+1)[0]
  right = buildTree(idx+1,e,height+1)[0]
  node_ = TreeNode(kl[idx],vl[idx],left,right)
  return node_,min_val

if __name__ == '__main__':
  #dickv = set()
  kl = []
  vl = []
  with open(sys.argv[1]) as f:
    for line in f.readlines():
      key,val = line.strip().split(':')
      kl.append(int(key))
      vl.append(int(val))
      
  # print(kl)
  # print(vl)
      
  res = buildTree(0,len(kl)-1,1)
  print(res[1])
  print(res[0])
  
  times=[]
  for i in range(10):
      start = time.perf_counter()
      buildTree(0,len(kl)-1,1)
      end = time.perf_counter()
      buildTree.cache_clear()
      times.append(end-start)
  print(int(sum(times)/10*pow(10,9)))
  
  