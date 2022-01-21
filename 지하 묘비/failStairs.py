import sys

n = int(sys.stdin.readline())
stairs = []
dp = [0] * (n+1)
stairs.append(0)
for _ in range(n):
  stairs.append(int(sys.stdin.readline()))

ans = 0
i = 0
cnt = 1
while i < n:
  if i ==  n-1:
    ans += stairs[i+1]
    break


  a = max(stairs[i+1], stairs[i+2])

  if a == stairs[i+1] and cnt == 2:
    cnt = 1
    ans += stairs[i+2]
    if i == n:
      ans += stairs[i+1]
      break
    i = i+2
  elif a == stairs[i+1]:
    cnt += 1
    ans += stairs[i+1]
    if i == n:
      ans += stairs[i+1]
      break
    i = i+1
  else:
    cnt = 1
    ans += stairs[i+2]
    if i == n:
      ans += stairs[i+2]
      break
    i = i+2




print(ans)

