import sys

n, r = map(int, sys.stdin.readline().split())
arr = []
combi = list(map(int, sys.stdin.readline().split()))
combi.sort()
def recursion(s, n, r):
  if len(arr) == r:
    for i in arr:
      print(i , end = ' ')
    print()
    return
  else:
    for i in range(s, n+1): 
      arr.append(combi[i])
      recursion(i, n, r)
      arr.pop()

recursion(0, n-1, r)


  
