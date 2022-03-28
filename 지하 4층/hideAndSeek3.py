import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = [1e9 for _ in range(100001)]
q = deque()
q.append((n, 0))
arr[n] = 0
while q:

  a, t = q.popleft()

  if 0 <= a-1 < 100001 and arr[a-1] == 1e9:
    arr[a-1] = t+1
    q.append((a-1, t+1))
  if 0 <= 2*a < 100001 and arr[2*a] == 1e9:
    arr[2*a] = t
    q.append((2*a, t))
  if 0 <= a+1 < 100001 and arr[a+1] == 1e9:
    arr[a+1] = t+1
    q.append((a+1, t+1))


print(arr[k])
