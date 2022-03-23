import sys

n = int(input())
arr = [[0 for _ in range(501)] for _ in range(501)]
tmp = list(map(int, sys.stdin.readline().split()))
arr[0][1] = tmp[0]
for i in range(1, n):
  tmp = list(map(int, sys.stdin.readline().split()))
  for j in range(len(tmp)):
    arr[i][j+1] = max(arr[i-1][j] + tmp[j], arr[i-1][j+1] + tmp[j])

print(max(arr[n-1]))
