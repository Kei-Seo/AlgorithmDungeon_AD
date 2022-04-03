import sys
sys.setrecursionlimit(10**6)
TC = int(sys.stdin.readline())


for _ in range(TC):
  Time = 0
  N, M, W = map(int, sys.stdin.readline().split())
  road = []

  
  for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    road.append((a, b, c))
    road.append((b, a, c))

  for _ in range(W):
    a, b, c  = map(int, sys.stdin.readline().split())
    road.append((a, b, -c))

  def bellman_ford(s):
    dist = [1e9 for _ in range(N+1)]
    dist[s] = 0 # 시작노드 초기화

    for i in range(N-1): #정점수 만큼 반복
      for u, v, w in road:
        dist[v] = min(dist[v], dist[u] + w)

    for u, v, w in road:
      if dist[u] + w < dist[v]:
        return True
    return False

  if bellman_ford(1):
    print("YES")
  else:
    print("NO")
    
    
