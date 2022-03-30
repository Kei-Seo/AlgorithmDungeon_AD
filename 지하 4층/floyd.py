import sys

n = int(sys.stdin.readline())
n_bus = int(sys.stdin.readline())
distance = [[1e9 for i in range(n)] for j in range(n)]
city = []
for _ in range(n_bus):
  a, b, c = map(int, sys.stdin.readline().split())
  distance[a-1][b-1] = min(distance[a-1][b-1], c)
  city.append([a, b, c])

for i in range(n):
  for j in range(n):
    if i == j:
      distance[i][j] = 0

def floyd():

  for k in range(0, n):
    for i in range(0, n):
      for j in range(0, n):
        distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
  
floyd()

for i in range(n):
  for j in range(n):
    if distance[i][j] == 1e9:
      print(0, end=' ')
    else:
      print(distance[i][j], end= ' ')
  print()

  
