import sys

n = int(sys.stdin.readline())

arr = {}
m = list(map(int, sys.stdin.readline().split()))
j = 1

for i in m:
  arr[j] = i
  j += 1

arr2 = sorted(arr.items(), key=lambda x: x[1])

res = [0]*(n+1)
pre = -1
k = 0 
for y in arr2:
  if y[1] == pre:
    res[y[0]] = k-1
  else:  
    res[y[0]] = k
  k += 1
  pre = y[1]

for i in range(1, n+1):
  print(res[i], end = ' ')
