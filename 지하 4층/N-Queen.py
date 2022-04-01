import sys

n = int(sys.stdin.readline())
cnt = 0
queen = [0] * n
visited = []

def checkQueen(x):
  for i in range(x):
    if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x-i):
      return False
  return True
    

def DFS(s):
  global cnt
  # 탈출조건
  if s == n:
    cnt += 1
    return 

  else:
    for i in range(n):
      queen[s] = i
      if checkQueen(s):
        DFS(s+1)

DFS(0)
print(cnt)
