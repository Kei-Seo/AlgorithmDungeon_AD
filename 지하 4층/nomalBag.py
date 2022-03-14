import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
stuff = []
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  stuff.append([a, b])
 

stuff.sort()

for i in range(1, N+1):
  total = K
  for j in range(1, K+1):
    w = stuff[i-1][0]
    v = stuff[i-1][1]

    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
    

print(dp[N][K])


  
  
  
