import sys 


n = int(sys.stdin.readline())
INF = 1e9
answer = [INF] * (n+1)

answer[3] = 1
if n >= 5:
  answer[5] = 1 

for i in range(6, n+1):
    answer[i] = min(answer[i-5]+1, answer[i-3]+1)
    
if INF <= answer[n]:
  print(-1)
else:
  print(answer[n])
