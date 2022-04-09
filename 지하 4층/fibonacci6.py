import sys
N = int(sys.stdin.readline())

matrix = [[1, 1], [1, 0]]

def mul(A, B):
  t = [[0, 0], [0, 0]]
  for i in range(len(A)):
    for j in range(len(A)):
      e = 0
      for k in range(len(A)):
        e += A[i][k] * B[k][j]
      t[i][j] = e % 1000000007
  return t
      
def calFibonacci(arr, n):
  if n == 1:
    for i in range(len(arr)):
      for j in range(len(arr)):
        arr[i][j] %= 1000
    return arr
    
  tmp = calFibonacci(arr, n//2)
  if n % 2 :
    return mul(mul(tmp, tmp), matrix)
  else:
    return mul(tmp, tmp)


print(calFibonacci(matrix, N)[0][1])
