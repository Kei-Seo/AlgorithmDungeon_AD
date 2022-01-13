import sys

n = int(sys.stdin.readline())
m = []
sum = 0
for i in range(n):
  t = int(sys.stdin.readline())
  if t == 0:
    a = m.pop()
    sum -= a
  else:
    m.append(t)
    sum += t

print(sum)
  

