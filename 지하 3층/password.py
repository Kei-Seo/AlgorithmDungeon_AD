import sys

n, m = map(int, sys.stdin.readline().split())
site = {}

for _ in range(n):
  a, b = map(str, sys.stdin.readline().split())
  site[a] = b 

for _ in range(m):
  print(site[sys.stdin.readline().rstrip()])
