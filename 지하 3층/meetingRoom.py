import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))

res = 0

arr.sort(key = lambda x: (x[1], x[0]))

pre_e = 0


for s, e in arr:
  temp = 0
  
  if s >= pre_e:
    pre_e = e
    res += 1



print(res)

