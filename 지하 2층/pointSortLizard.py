import sys

n = int(sys.stdin.readline())
point_list = []
for _ in range(n):
  point_list.append(list(map(int, sys.stdin.readline().split())))

point_list.sort()

for point in point_list:
  print(str(point[0])+" "+str(point[1]))


