import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
m = [[] for _ in range(a)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(a):
  t = input()
  for j in t:
    m[i].append(int(j))    


visited = [[False for _ in range(b)] for _ in range(a)]

q = deque() 
q.append((0, 0))

while q:
  x, y = q.popleft()
  visited[x][y] = True

  for i in range(4):
    tx = dx[i] + x
    ty = dy[i] + y
    if tx < a and ty < b:
      if m[tx][ty] == 1:
        if tx >= 0 and ty >= 0 and not visited[tx][ty]:
          m[tx][ty] = m[x][y] + 1
          q.append((tx, ty))
        
 
print(m[a-1][b-1])
