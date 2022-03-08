import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
weight = [2e9] * (v+1)
for _ in range(e):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((c, b))

heap = []
def kruskal(s):
  weight[s] = 0
  heapq.heappush(heap, (0, s))
  
  while heap:
    wei, now = heapq.heappop(heap)

    if weight[now] < wei:
      continue
    
    for w, v in graph[now]:
      
      next_w = wei+w
      if next_w < weight[v]:
        weight[v] = next_w
        heapq.heappush(heap, (next_w, v))

kruskal(s)

for i in range(1, v+1):
  if weight[i] == 2e9:
    print('INF')
  else:
    print(weight[i])
