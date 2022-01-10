import sys

node = int(sys.stdin.readline())
n = int(sys.stdin.readline())
graph = [[] for _ in range(node+1)]
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  
cnt = 0
queue = []
queue.append(1)
visited = [False] * (node + 1)
visited[1] = True

while len(queue) > 0:
  i = queue.pop(0)  
  for j in graph[i]:
    if not visited[j]:
      visited[j] = True
      cnt += 1
      queue.append(j)

print(cnt)
