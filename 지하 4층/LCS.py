import sys

string_1 = sys.stdin.readline().rstrip()
string_2 = sys.stdin.readline().rstrip()



dp = [[0 for _ in range(len(string_2)+1)] for _ in range(len(string_1)+1)]

for i in range(1, len(string_1)+1):
  for j in range(1, len(string_2)+1):
    if string_1[i-1] == string_2[j-1]:
      dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j])
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(max(max(dp)))
