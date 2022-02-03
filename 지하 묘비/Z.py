import sys

n, r, c = map(int, sys.stdin.readline().split())
k = 2**n
res = 0

while n != 0:
  n -= 1

  if r < 2**n and c < 2**n:
    res += (2**n) * (2**n) * 0
  elif r >= 2**n and c < 2**n:
    res += (2**n) * (2**n) * 2
    r -= (2**n)
  elif r < 2**n and c >= 2**n:
    res += (2**n) * (2**n) * 1
    c -= (2**n)
  elif r >= 2**n and c >= 2**n:
    res += (2**n) * (2**n) * 3
    r -= (2**n)
    c -= (2**n)

print(res)
