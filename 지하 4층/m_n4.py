import sys

n, r = map(int, sys.stdin.readline().split())
arr = []

def recursion(s, n, r):
  if len(arr) == r:
    for i in arr:
      print(i , end = ' ')
    print()
    return
  else:
    for i in range(s, n+1):
      arr.append(i)
      recursion(i, n, r)
      arr.pop()

recursion(1, n, r)


  
