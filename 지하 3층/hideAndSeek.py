import sys
from collections import deque


subin, sister = map(int, sys.stdin.readline().split())
q = deque()
q.append((subin, 0))
visited = set()


while q:
  cur_subin, cnt = q.popleft()
  
  if cur_subin == sister:
    print(cnt)
    break
   
  if not (cur_subin-1) in visited and cur_subin-1 <= 100000 and  cur_subin-1 >= 0:
    q.append((cur_subin-1, cnt+1))
    visited.add(cur_subin-1)

  if not (cur_subin+1) in visited and cur_subin+1 <= 100000:
    q.append((cur_subin+1, cnt+1))
    visited.add(cur_subin+1)

  if not (cur_subin*2) in visited and cur_subin*2 <=100000:
    q.append((cur_subin*2, cnt+1))
    visited.add(cur_subin*2)

   
  
   
  
