import sys
from collections import deque

q = deque()
n, m, l = map(int, sys.stdin.readline().split())
box = [[[0 for _ in range(n) ] for _ in range(m)] for _ in range(l)]
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
max_cnt = 0  
for i in range(l):
  for j in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))
    for k in range(n):
      box[i][j][k] = tmp[k]
      if box[i][j][k] == 1:
        q.append((i, j, k))

while q:
  z, x, y = q.popleft()
  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]
    if 0 <= nx < m and 0 <= ny < n and 0 <= nz < l:
      if box[nz][nx][ny] == 0:
        box[nz][nx][ny] = box[z][x][y] + 1
        q.append((nz, nx, ny))

possible = True
day = -2
for i in range(l):
  for j in range(m):
    for k in range(n):
      if box[i][j][k] == 0:
        possible = False
        print(-1)
        break
      day = max(day, box[i][j][k])

if possible:
  if day == -1:
    exit(0)
  else:
    print(day-1)
