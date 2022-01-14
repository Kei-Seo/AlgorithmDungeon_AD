import sys

k, m, b = map(int, sys.stdin.readline().split())
floor = []
for _ in range(k):
  floor.append(list(map(int, sys.stdin.readline().split())))

down = min(min(floor))
up = max(max(floor))
h = 0
t = 1e9
for n in range(down, up+1):
  c = True
  pile = 0
  cut = 0
  temp_t = 0
  for i in range(k):
    for j in range(m):
      if floor[i][j] < n:
        # 블록을 쌓아야한다
        pile += n - floor[i][j]
        #temp_t += n-current
        #temp_b -= n-current
      elif floor[i][j] > n:
        # 블록을 깍아야 한다
        cut += floor[i][j] - n
        #temp_t += 2*(current-n)
        #temp_b += current-n
    
  if b + cut >= pile:
    temp_t = 2*cut + pile
    if t >=temp_t:
      h = max(n, h)
      t = temp_t

print(t,h)
