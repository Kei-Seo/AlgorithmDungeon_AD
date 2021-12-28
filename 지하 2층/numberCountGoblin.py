import sys

n = int(sys.stdin.readline())
mine = list(map(int, sys.stdin.readline().split(" ")))
what = int(sys.stdin.readline())
count = list(map(int, sys.stdin.readline().split(" ")))
pos_answer = []
neg_answer = []

max_n = max(count)
max_m = max(mine)
real_max = max(max_n, max_m)
min_n = min(count)
min_m = min(mine)
real_min = min(min_n, min_m)

for x in range(real_max+1):
    pos_answer.append(0)
for x in range(abs(real_min)+1):
    neg_answer.append(0)

for x in mine:
  if x >= 0:
    pos_answer[x] += 1
  else:
    x *= -1
    neg_answer[x] +=1

i = 1 
for x in count:
  if x >= 0:
    if i == len(count):
       print(str(pos_answer[x]), end ="")
    else:
      print(str(pos_answer[x])+ " ", end = "")
  else:
    x *= -1 
    if i == len(count):
       print(str(neg_answer[x]), end = "")
    else:
      print(str(neg_answer[x])+ " ", end = "")
  i+=1
  
