import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ioi = str(sys.stdin.readline().rstrip())
cnt = 0
p = 0
j = 0
while j < m-1:
  if ioi[j-1] == 'I' and ioi[j] == 'O' and ioi[j+1] == 'I':
    p += 1
    if p == n:
      cnt += 1
      p -= 1
    j += 1
  else:
    p = 0   
  j +=1

print(cnt)
