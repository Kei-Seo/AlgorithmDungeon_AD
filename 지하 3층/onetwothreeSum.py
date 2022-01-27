import sys


n = int(sys.stdin.readline())


for _ in range(n):
  t = int(sys.stdin.readline())
  cnt = 0
  dp = []
  dp.append(0)
  dp.append(1)
  dp.append(2)
  dp.append(4)

  for i in range(4, t+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

  print(dp[t])
    

  
