import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n+1) 
for i in range(1, n+1):
  dp[i] = nums[i-1] + dp[i-1]


for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(dp[b] - dp[a-1])
  
