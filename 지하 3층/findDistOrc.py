import sys

n = int(sys.stdin.readline())

graph = [[] for i in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]
visit = []
n_list = []
for i in range(n):
  n_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
  for j in range(n):
    if n_list[i][j] == 1:
      graph[i].append(j)


for i in range(n):

    visit.append(i)
    while len(visit) > 0:
      new_node = visit.pop(0)

      for j in graph[new_node]:
        if answer[i][j] != 1:
          answer[i][j] = 1
          visit.append(j)

for a in answer:
  for j in a:
    print(j, end=" ")
  print()
