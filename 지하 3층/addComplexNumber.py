import sys

n  = int(sys.stdin.readline())
ap = [[] for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
global m 
m = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
  s = str(sys.stdin.readline().rstrip())
  for j in s:
    ap[i].append(int(j))

def dfs(a, b):
  global m
  ap[a][b] = -1
  m += 1
  for i in range(4):
    y = a+dy[i]
    x = b+dx[i]
    if x >= 0 and x < len(ap) and y >= 0 and y < len(ap):
      if ap[y][x] == 1:
        ap[y][x] = -1
        dfs(y, x)
        

res = []
cnt = 0

for i in range(n):
  for j in range(n):
    if ap[i][j] == 1:
      cnt += 1
      dfs(i, j)
      res.append(m)
      m = 0

print(cnt)
res.sort()
for r in res:
  print(r)
