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
    for i in range(0, n+1):
      if not combi[i] in arr:
        arr.append(combi[i])
        recursion(i+1, n, r)
        arr.pop()

recursion(0, n-1, r)


  
