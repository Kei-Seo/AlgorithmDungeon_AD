import sys

n, k = map(int, sys.stdin.readline().split())
multi_n = 1
multi_k = 1
for x in range(k, 0, -1):
  multi_n *= n
  n -= 1
  temp = n
  multi_k *= x


print(int(multi_n/multi_k))
