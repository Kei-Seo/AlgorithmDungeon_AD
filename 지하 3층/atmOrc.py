import sys

n = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

total_sum = 0
temp_sum = 0
for i in n_list:
  temp_sum += i
  total_sum += temp_sum

print (total_sum)

