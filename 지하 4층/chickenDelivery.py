import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
village = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
chicken = []
c_cnt = 0

def selectChicken(arr, n):
  result = []
  if n == 0:
    return [[]]

  for i in range(0, len(arr)):
    elim = arr[i]
    rest_arr = arr[i + 1:]
    for C in selectChicken(rest_arr, n-1):
      result.append([elim] + C)

  return result

  
  

for i in range(n):
  tmp = list(map(int, sys.stdin.readline().split()))
  for j in range(n):
    village[i][j] = tmp[j]
    if village[i][j] == 2:
      chicken.append((i, j, 0))
      c_cnt += 1

tmp = []
for i in range(c_cnt):
  tmp.append(i)

s_chicken = selectChicken(tmp, m)
res = []
for S in s_chicken:
  visit = [[1e9 for _ in range(n)] for _ in range(n)]
  tmp_visit = [[False for _ in range(n)] for _ in range(n)]
  q = deque()

  for s in S:
    q.append(chicken[s])
    
  while q:
    x, y, c = q.popleft()
    if c == 0:
      tmp_visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if village[nx][ny] == 1 :
          visit[nx][ny] = min(visit[nx][ny], c+1) 
        if tmp_visit[nx][ny] == False:
          q.append((nx, ny, c+1))
          tmp_visit[nx][ny] = True

  t = 0
  for i in range(n):
    for j in range(n):
      if visit[i][j] != 1e9:
        t += visit[i][j]

  res.append(t)

print(min(res))
  

  
