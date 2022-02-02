import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]  
visited = [True] * (n+1)
q = deque()
cnt = 0

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)


for j in range(1, n+1):
  if visited[j]:

    q.append(j)
    visited[j] = False
    while q:
      newNode = q.popleft()
      visited[newNode] = False
      for i in graph[newNode]:
        if visited[i]:
          visited[i] = False
          q.append(i)

    cnt += 1



print(cnt)
