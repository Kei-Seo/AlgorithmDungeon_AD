import sys
from itertools import combinations

n = int(sys.stdin.readline())

for _ in range(n):
  k = int(sys.stdin.readline())
  closet = []
  closet_num = []
  for _ in range(k):
    item, kind = map(str, sys.stdin.readline().split())
    haveItem = False
    for i in range(len(closet)):
      if closet[i] == kind:
        closet_num[i] = closet_num[i] + 1
        haveItem = True
    
    if not haveItem:
      closet.append(kind)
      closet_num.append(1)
  
  res = 1
  for i in closet_num:
    res *= (i+1)

  print(res-1)
 


  
