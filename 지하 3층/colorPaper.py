import sys

n = int(sys.stdin.readline())
 
w = 0
b = 0
arr = []

for _ in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))


def checkSqure(arr, r, s, n):

  global w, b 

  check = True
  standard = arr[r][s]

  for i in range(r, r+n):
    for j in range(s, s+n):
      if arr[i][j] != standard:
        check = False
  
  if check:
    if standard == 0:
      w += 1
    elif standard == 1:
      b += 1
  else:
    checkSqure(arr, r, s, n//2) 
    checkSqure(arr, r+n//2, s, n//2)
    checkSqure(arr, r, s+n//2, n//2)
    checkSqure(arr, r+n//2, s+n//2, n//2)
    return

checkSqure(arr, 0, 0, n)

print(w, b)
