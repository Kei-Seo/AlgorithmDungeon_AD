import sys
import heapq
input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
    ip = int(input())
    if ip != 0:
        heapq.heappush(heap, -ip)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
        
        
    
