import sys

n, t = map(int, sys.stdin.readline().split())

m = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(m)
mid = (left+right)//2

while left<=right :
  mid = (left+right)//2
  temp = 0
  for i in m:
    if i > mid:
      temp += i - mid
  if temp >= t :
    left = mid +1
  else:
    right = mid -1
print(right)
