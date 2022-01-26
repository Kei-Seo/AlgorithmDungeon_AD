from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())
box = []
for _ in range(col):
  box.append(list(map(int, sys.stdin.readline().split())))

queue = deque()

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for i in range(col):
  for j in range(row):
    if box[i][j] == 1:
      queue.append((i, j))

res = 0

while queue:
  y, x= queue.popleft()
  #print(x, y)

  for i in range(4):
    if x + dx[i] >= 0 and y + dy[i] >= 0 and x + dx[i] < row and y + dy[i] < col:
      #print(x + dx[i], y + dy[i])
      if box[y + dy[i]][x + dx[i]] == 0:
        box[y + dy[i]][x + dx[i]] += (box[y][x] + 1)
        res = max(res,  box[y + dy[i]][x + dx[i]])
        queue.append((y + dy[i], x + dx[i]))

b = False
for i in range(col):
  for j in range(row):
    if box[i][j] == 0:
      b = True
      break
  if b:
    break

if b:
  print("-1")
else:
  if res == 0:
    print(res)
  else:
    print(res-1)



