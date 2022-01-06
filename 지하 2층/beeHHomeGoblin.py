import sys

n = int(sys.stdin.readline())
cnt = 1
for i in range(n):
  cnt = cnt + 6*i
  if n <= cnt:
    print(i+1)
    break

  
