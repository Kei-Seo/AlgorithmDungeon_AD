import sys

n = int(sys.stdin.readline())
arr = []
arr.append(0)
arr.append(1)
arr.append(1)
arr.append(1)
arr.append(2)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(7)
arr.append(9)
arr.append(12)
for i in range(11, 101):
  arr.append(arr[i]+arr[i-4])

for _ in range(n):
  k = int(sys.stdin.readline())
  print(arr[k])
