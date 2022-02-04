import sys
from collections import deque


n = int(sys.stdin.readline())


for _ in range(n):
  num, target = map(int, sys.stdin.readline().split())
  q = deque()
  q.append((num, ""))
  visited = [True] * (10000)
  visited[num] = False
  
  while q:
    tn, ts = q.popleft()
    if tn == target: 
      print(ts)
      break

    #D
    x = tn * 2
    if x > 9999:
      x = x%10000
    if visited[x]:
      q.append((x, ts + "D"))
      visited[x] = False
    #S
    y = tn - 1
    if y < 0:
      y = 10000 + y
    if visited[y]:
      q.append((y, ts + "S"))
      visited[y] = False
    #L
    j = tn // 1000
    k = tn % 1000  
    k = k * 10
    k += j
    if visited[k]:
      q.append((k, ts +"L"))
      visited[k] = False
    #R
    a = tn%10
    b = tn//10
    a *= 1000
    a += b
    if visited[a]:
      q.append((a, ts+ "R"))
      visited[a] = False
    
   
