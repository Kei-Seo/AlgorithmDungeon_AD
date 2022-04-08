import sys

n, b = map(int, sys.stdin.readline().split())
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

def mul(A, B):
  tmp = [[0 for _ in range(len(A))] for _ in range(len(A))]
  
  for i in range(len(tmp)):
    for j in range(len(tmp)):
      c = 0
      for k in range(len(tmp)):
        c += A[i][k] * B[k][j]
      tmp[i][j] = c % 1000
  return tmp

def square(arr, b):
  if b == 1:
    for x in range(len(arr)):
      for y in range(len(arr)):
        arr[x][y] %= 1000
    return arr

  tmp = square(arr, b//2)

  if b % 2 :
    # 홀수라면
    return mul(mul(tmp, tmp), arr)
  else:
    return mul(tmp, tmp)

result = square(arr, b)
for r in result:
    print(*r)
