import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)


N = [0] * (n+1)
N[0] = 1e9
for i in range(1, n+1):
  q = deque()
  q.append((i, 1)) 
  visited = [False]*(n+1)
  visited[i] = True
  
  while q:   
    
    add = 0
    node, cnt = q.popleft()
    for j in graph[node]:
      if not visited[j]:
        q.append((j, cnt+1))
        N[i] += cnt 
        visited[j] = True


target = min(N)
for i in range(len(N)):
  if target == N[i]:
    print(i)
    break




      

      

 


  
