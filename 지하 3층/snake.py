import sys
from collections import deque
u, d = map(int, sys.stdin.readline().split())
up = []
down = []

for _ in range(u):
  a, b = map(int, sys.stdin.readline().split())
  up.append((a, b))

for _ in range(d):
  a, b = map(int, sys.stdin.readline().split())
  down.append((a, b))

dist = [-1] * (101)
dist[1] = 0
q = deque()
q.append(1)
while q:
  a = q.popleft()
  for i in range(1, 7):
    nt = a+i
    if a+i > 100:
      continue 
    for u_1, u_2 in up:
      if u_1 == a+i:
        nt = u_2
        break 
    for d_1, d_2 in down:
      if d_1 == a+i:
        nt = d_2
        break
    if dist[nt] == -1:
      dist[nt] = dist[a] + 1
      q.append(nt)

print(dist[100])
  
