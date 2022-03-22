import sys
from collections import deque

q = deque()
n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for i in range(n):
  tmp = sys.stdin.readline().rstrip()
  for j in range(m):
    arr[i][j] = int(tmp[j])

q.append((0, 0, 1))
visit[0][0][1] = 1

def breakWall():
  while q:
    x, y, w = q.popleft()

    if x == n-1 and y == m-1:
      return visit[x][y][w]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0<= ny < m:
          if arr[nx][ny] == 1 and w == 1:
            q.append((nx, ny, w-1))
            visit[nx][ny][0] = visit[x][y][1] + 1
          elif arr[nx][ny] == 0 and visit[nx][ny][w] == 0:
            q.append((nx, ny, w))
            visit[nx][ny][w] = visit[x][y][w] + 1
  return -1        
              
  

print(breakWall())

