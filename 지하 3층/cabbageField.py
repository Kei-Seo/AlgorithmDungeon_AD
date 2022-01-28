import sys
from collections import deque

n = int(sys.stdin.readline())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
  m, n, k = map(int, sys.stdin.readline().split())

  field = [[0 for _ in range(m)] for _ in range(n)]
  for i in range(k):
    a, b  = map(int, sys.stdin.readline().split())
    field[b][a] = 1

  q = deque([])
  cnt = 0
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:

        field[i][j] = 2
        q.append([i, j])

        while q:
          x, y = q.popleft()
          for d in range(4):
            if x+dx[d] >= 0 and x+dx[d] < n and y+dy[d] >=0 and y+dy[d] < m:
              if field[x+dx[d]][y+dy[d]] == 1:
                field[x+dx[d]][y+dy[d]] = 2
                q.append([x+dx[d], y+dy[d]])
      
        cnt += 1
  print(cnt)

  
