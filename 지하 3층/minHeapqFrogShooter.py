import heapq
import sys

input = sys.stdin.readline

i = int(input())
heap = []
answer = []

for _ in range(i):
    ip = int(input())
    if ip != 0:
        heapq.heappush(heap, ip)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))



