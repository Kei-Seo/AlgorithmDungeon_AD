import sys
from collections import deque
time = 0
map_size = int(sys.stdin.readline())
s_size = 2
cur_size = 0
sea = [[0 for _ in range(map_size)] for _ in range(map_size)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
sx = 0 
sy = 0
for i in range(map_size):
  tmp = list(map(int, sys.stdin.readline().split()))
  for j in range(map_size):
    sea[i][j] = tmp[j]
    if sea[i][j] == 9:
      sea[i][j] = 0
      sx = i

      sy = j
  
while True:
  q = deque()
  q.append((sx,sy,1))
  visit = [[False for _ in range(map_size)] for _ in range(map_size)]
  visit[sx][sy] = True
  priority = []
  min_t = 1e9
  hasFind = False
  while q:
    x, y, t = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and ny >= 0 and nx < map_size and ny < map_size:
        if min_t < t:
          hasFind = True
          break
        elif s_size > sea[nx][ny] and sea[nx][ny] != 0 and not visit[nx][ny]:
          priority.append([t, nx, ny])
          visit[nx][ny] = True
          min_t = t
        elif s_size == sea[nx][ny] or sea[nx][ny] == 0:
          if not visit[nx][ny]:
            visit[nx][ny] = True
            q.append((nx, ny, t+1))
    if hasFind:
      break

  if len(priority) == 0:
    print(time)
    break
  else:
    priority.sort()
    sea[priority[0][1]][priority[0][2]] = 0
    cur_size += 1
    time += priority[0][0]
    sx = priority[0][1]
    sy = priority[0][2]
    if cur_size == s_size :
      s_size += 1
      cur_size = 0
    
