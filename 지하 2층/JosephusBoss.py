import sys

n, k = map(int, sys.stdin.readline().split())
arr = [0 for i in range(n)]
i = 0
answer = []
cnt = 0
while len(answer) < n:
  if i >= n:
    i -= n
  if i < n and cnt == k:
    #print(i, cnt)
    if arr[i-1] == 0:
      arr[i-1] = 1
      if i == 0 :
         answer.append(n)
      else:
        answer.append(i)
      cnt = 1
  elif arr[i-1] != 1:
    cnt += 1
  i += 1

print("<", end="")
for i in range(0, len(answer)-1):
  print(str(answer[i]).rstrip()+", ", end="")

print(str(answer[len(answer)-1])+">", end="")
