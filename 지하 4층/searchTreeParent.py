import sys
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
tree = [0 for _ in range(n+1)]


for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

tree[0] = 1
tree[1] = 1

def DFS(s):
    for i in graph[s]:
      if tree[i] == 0:
        tree[i] = s
        DFS(i)

DFS(1)
for i in range(2, len(tree)):
  print(tree[i])
  

