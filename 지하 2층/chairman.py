import sys

n = int(sys.stdin.readline())

for _ in range(n):
  floor = int(input())
  room = int(input())
  
  ap = [[] for _ in range(floor+1)]
  
  for i in range(floor+1):
    for j in range(room):
      if i == 0:  
        ap[i].append(j+1)
      else:
        temp = 0
        for k in range(j+1):
          temp += ap[i-1][k]
        ap[i].append(temp)

  print(ap[floor][room-1])



  
