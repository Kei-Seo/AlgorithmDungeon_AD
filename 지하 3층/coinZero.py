import sys

n, k = map(int, sys.stdin.readline().split())
kinds = []

for _ in range(n):
  kinds.append(int(sys.stdin.readline())) 

cnt = 0
pre = 1

while k > 0:

  pre = kinds[0]
  for i in kinds:
    if k - i < 0:
      break
    elif k - i == 0:
      pre = i
    pre = i


  while k >= 0:
    k -= pre
    cnt += 1

  k += pre
  cnt -= 1
  
print(cnt)
