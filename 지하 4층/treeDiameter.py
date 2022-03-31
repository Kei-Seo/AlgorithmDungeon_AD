import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

while True:
  try:
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
  except:
    break
    
  
distance = [0 for _ in range(n+1)] 
distance[1] = 0
visit[1] = True
def dfs(a):
  for b, c in graph[a]:
    if not visit[b]:
      visit[b] = True
      distance[b] = distance[a] + c
      dfs(b)


def findMaxIndex():
  m = max(distance)
  for i in range(n+1):
    if m == distance[i]:
      return i
  
dfs(1)
k = findMaxIndex()
distance = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]
visit[k] = True
dfs(k)
print(max(distance))
