import sys
import heapq
total_n = int(sys.stdin.readline())

for _ in range(total_n):
  sub_n = int(sys.stdin.readline())
  #priority = deque()
  visited = [True] * (1000000) 
  heap = []
  max_heap = []
  for j in range(sub_n):
    command, num = map(str, sys.stdin.readline().split())
    if command == 'I':
      heapq.heappush(heap, (int(num), j))
      heapq.heappush(max_heap,((-int(num), j)))
      visited[j] = False

    elif command == 'D':      
        if num == '-1': 
          while heap and visited[heap[0][1]]:
            heapq.heappop(heap)
          if heap:  
            visited[heap[0][1]] = True
            heapq.heappop(heap)
          
        if num == '1':
          while max_heap and visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
          if max_heap:
            visited[max_heap[0][1]] = True
            heapq.heappop(max_heap)

  while heap and visited[heap[0][1]]:
    heapq.heappop(heap)
  while max_heap and visited[max_heap[0][1]]:
    heapq.heappop(max_heap)

          
  if max_heap and heap:
    print(-1*max_heap[0][0], heap[0][0])
  else:
    print("EMPTY")

