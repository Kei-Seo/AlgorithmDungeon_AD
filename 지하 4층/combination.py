import sys

n, r = map(int, sys.stdin.readline().split())
r2 = r
ans = 0
denominator = 1
numerator = 1
for _ in range(r):
  denominator *= n
  n -= 1
  numerator *= (r2)
  r2 -= 1

print(denominator//numerator)
  
