import sys
import heapq
n = int(sys.stdin.readline())
heap = []
minus_heap = []
for _ in range(n):
  k = int(sys.stdin.readline())
  if 0 == k:
    if len(heap) == 0 and len(minus_heap) == 0:
      print(0)
      continue
    elif len(heap) != 0 and len(minus_heap) == 0:
      a = heapq.heappop(heap)
      print(a)
    elif len(heap) == 0 and len(minus_heap) != 0:
      t, b = heapq.heappop(minus_heap)
      print(b)
    else:    
      a = heapq.heappop(heap)
      t, b = heapq.heappop(minus_heap)
      if abs(a) == abs(b):
        if a <= b:
          heapq.heappush(minus_heap, (-b, b))
          print(a)
        else:
          heapq.heappush(heap, a)
          print(b)
      elif abs(a) < abs(b):
        heapq.heappush(minus_heap, (-b, b))
        print(a)
      else:
        heapq.heappush(heap, a)
        print(b)
  else:
    if k < 0:
      heapq.heappush(minus_heap, (-k, k))
    else:
      heapq.heappush(heap, k)
    
