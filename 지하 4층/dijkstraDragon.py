import sys 
input = sys.stdin.readline
INF = 1e9
v, e = map(int, input().split())
start_node = int(input())
graph =[[] for _ in range(v+1)]
distance = [INF for _ in range(v+1)]
visited = [False for _ in range(v+1)]


for i in range(e):
  i, a, b = map(int, input().split())
  graph[i].append((a, b))

distance[start_node] = 0 # 시작노드 초기화
visited[start_node] = True

for i in graph[start_node]: # 시작노드에서 갈 수 있는 노드
  distance[i[0]] = i[1]

for i in range(v-1):
  min_value = INF
  index = 0
  for j in range(v+1): # 방문 x 이면서 시작노드와 가장 가까운 노드
    if not visited[j] and distance[j] < min_value :
      min_value = distance[j]
      index = j
  
  visited[index] = True # 방문처리
  
  for next in graph[index]:
    cost = distance[index] + next[1]
    if distance[next[0]] > cost:
      distance[next[0]] = cost
  

print(distance)
    
