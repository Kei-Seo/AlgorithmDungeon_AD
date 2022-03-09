import sys
import heapq

n = int(sys.stdin.readline())
city = [[] for _ in range(n+1)]

for _ in range(int(sys.stdin.readline())):
  a, b, c = map(int, sys.stdin.readline().split())
  city[a].append((c, b))
s, d = map(int, sys.stdin.readline().split())
heap = []
distance = [2e9 for _ in range(n+1)]

def shortestDistanceCity(s):
  distance[s] = 0
  
  for c, b in city[s]:
    heapq.heappush(heap, (c, b))
    if distance[b] > c:
      distance[b] = c

  while heap:
    cost , b = heapq.heappop(heap)
    
    if cost > distance[b]:
      continue

    for n_cost, n_city in city[b]:
      tmp = n_cost + distance[b]

      if tmp < distance[n_city]:
        distance[n_city] = tmp
        heapq.heappush(heap, (tmp, n_city))



shortestDistanceCity(s)
print(distance[d])

    
  
