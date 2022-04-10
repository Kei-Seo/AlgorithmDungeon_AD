import sys

N = int(sys.stdin.readline())
arr = [[' ' for _ in range(N*2)] for _ in range(N)]


def smallTriganlge(i, j, size):
  if size == 3:
    arr[i][j] = '*'
    arr[i+1][j-1] = arr[i+1][j+1] = '*'

    for k in range(-2, 3):
      arr[i+2][j+k] = '*'
  else:
    newSize = size//2
    smallTriganlge(i, j , newSize)
    smallTriganlge(newSize+i, newSize+j, newSize)
    smallTriganlge(newSize+i, j - newSize, newSize)
    
smallTriganlge(0, N-1, N)

for i in range(N):
  for j in range(N*2):
    print(arr[i][j], end ='')
  print()
    
    
  
