import sys

n, m = map(int, sys.stdin.readline().split())
nn = set()
mm = set()

for _ in range(n):
  nn.add(sys.stdin.readline().rstrip())


for _ in range(m):
  mm.add(sys.stdin.readline().rstrip())

result = sorted(list(nn & mm))

print(len(result))
for find in result:
  print(find)
