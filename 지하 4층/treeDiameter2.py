import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(n):
  tmp = list(map(int, sys.stdin.readline().split()))
  for j in range(1, len(tmp)-1, 2):
    graph[tmp[0]].append((tmp[j], tmp[j+1]))

distance= [0] * (n+1)
visited = [False] * (n+1)
def DFS(n):
  for a, b in graph[n]:
    if not visited[a]:
      visited[a] = True
      distance[a] = distance[n] + b
      DFS(a)

def findMaxIndex():
  m = max(distance)
  for i in range(len(distance)):
    if m == distance[i]:
      return i
    
visited[1] = True
DFS(1)
k = findMaxIndex()
distance= [0] * (n+1)
visited = [False] * (n+1)
visited[k] = True
DFS(k)
print(max(distance))


