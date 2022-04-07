import sys

n = int(sys.stdin.readline())

def fibonacci(n):
  if n < 2:
    return n

  arr = [0  for _ in range(n+1)]
  arr[1] = 1

  for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

  print(arr[n])

fibonacci(n)
