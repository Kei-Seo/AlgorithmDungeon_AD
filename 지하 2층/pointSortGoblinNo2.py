import sys

n = int(sys.stdin.readline())
m = []

for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  m.append((a, b))

c = sorted(m, key = lambda x : x[0])
d = sorted(c, key = lambda x : x[1])
for i in d:
  print(i[0], i[1])
