import sys

n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n+1):
  minValue = 1e9
  j = 1
  while (j**2) <= i:
    minValue = min(minValue, dp[i-(j**2)])
    j += 1
  dp.append(minValue + 1)

print(dp[n])
