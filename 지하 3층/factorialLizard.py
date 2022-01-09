import sys

def factory(n):
  if n < 1:
    return 1
  else:
    return n * factory(n-1)


n = int(sys.stdin.readline())

a = factory(n)
cnt = 0

while True:
  if a % 10 == 0:
    a = a//10
    cnt += 1
  else:
    break

print(cnt)


