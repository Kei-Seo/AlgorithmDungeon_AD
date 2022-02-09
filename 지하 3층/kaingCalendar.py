import sys

num  = int(sys.stdin.readline())

for _ in range(num):  
  i, j, x, y = map(int, sys.stdin.readline().split())
  n = 0
  m = 0

  if i > j:
    n = i
    m = j
    temp = x
    x = y
    y = temp
  else:
    n = j
    m = i

  b = abs(m-n)
  c_y = x 
  cnt = 0

  if c_y == y:
      print(x)
      continue

  while cnt < n:
    cnt += 1
    c_y -= b
    if c_y <= 0:
      c_y += n
    if c_y == y:
      break
    
  res = m*cnt + x
 
  if cnt == n:
    print(-1)
  else:
    print(res)
