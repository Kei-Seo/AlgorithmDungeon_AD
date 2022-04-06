import sys
n = int(sys.stdin.readline())

for _ in range(n):
  col = int(sys.stdin.readline())
  
  st = []
  for i in range(2):
    st.append(list(map(int, sys.stdin.readline().split())))
 
  for i in range(1, col):
    if i == 1:
      st[0][i] += st[1][0]
      st[1][i] += st[0][0]

    else:
      st[0][i] += max(st[1][i-1], st[1][i-2])
      st[1][i] += max(st[0][i-1], st[0][i-2])

  print(max(st[1][col-1], st[0][col-1]))
    
    
    
    
    
  
  
