import sys

n = int(sys.stdin.readline())
global com 
com = ''

tree = [[] for _ in range(n)]
def searchTree(n, row, col):
  global com
  if n <= 1:
    com += str(tree[row][col])
    return
  else:
    p = True
    k = tree[row][col]
    for i in range(row, row+n):
      for j in range(col, col+n):
        if k != tree[i][j]:
          p = False
    
    if p:
      com += str(tree[row][col])
      
    else:
      com += '('
      searchTree(n//2, row, col)
      searchTree(n//2, row, col+n//2)
      searchTree(n//2, row+n//2, col)
      searchTree(n//2, row+n//2, col+n//2)
      com += ')'



for i in range(n): 
  s = str(sys.stdin.readline().rstrip())
  for j in s:
    tree[i].append(int(j))


searchTree(n, 0, 0)
print(com)
