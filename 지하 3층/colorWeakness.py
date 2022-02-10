import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
area = [[] for _ in range(n)]
no_area = [[] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def nomal_human(i , j, RGB, n):
  no_area[i][j] = 'X'
  
  for d in range(4):
    x = i + dx[d]
    y = j + dy[d]
    if x >= 0 and x < n and y >= 0 and y < n:
      if no_area[x][y] == RGB:
        no_area[x][y] = 'X'
        nomal_human(x, y, RGB, n)

def absnomal_human(i, j, RGB, n):
  area[i][j] = 'X'

  for d in range(4):
    x = i + dx[d]
    y = j + dy[d]
    if x >= 0 and x < n and y >= 0 and y < n:
      if RGB == 'R' or RGB == 'G':
        if area[x][y] == 'R' or area[x][y] == 'G':
          area[x][y] = 'X'
          absnomal_human(x, y, RGB, n)
      elif area[x][y] == RGB:
        area[x][y] = 'X'
        absnomal_human(x, y, RGB, n) 

for i in range(n):
  rgb = sys.stdin.readline().rstrip()
  
  for j in rgb:
    area[i].append(j)
    no_area[i].append(j)

cnt = 0
no_cnt = 0

for i in range(len(no_area)):
  for j in range(len(no_area)):
    if no_area[i][j] == 'R' or no_area[i][j] == 'G' or no_area[i][j] == 'B':
      nomal_human(i, j, no_area[i][j], n)
      no_cnt += 1
    if area[i][j] == 'R' or area[i][j] == 'G' or area[i][j] == 'B':
      absnomal_human(i, j, area[i][j], n)
      cnt += 1

print(no_cnt, cnt)
    





