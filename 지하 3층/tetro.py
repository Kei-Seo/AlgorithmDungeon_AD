import sys

row, col = map(int, sys.stdin.readline().split())

tetro = []

for i in range(row):
  tetro.append(list(map(int, sys.stdin.readline().split())))

shape = [
[[1,2,3], [0, 0, 0]], [[-1,-2,-3], [0, 0, 0]], [[0,0,0], [1,2,3]], [[0,0,0], [-1,-2,-3]], 
[[-1, 0, -1], [0, -1, -1]],  [[1, 0, 1], [0, -1, -1]], [[-1, 0, -1], [0, 1, 1]], [[1, 0, 1], [0, 1, 1]], 
[[-1, 0, -1], [0, -1, -1]],  [[1, 0, 1], [0, -1, -1]], [[-1, 0, -1], [0, 1, 1]], [[1, 0, 1], [0, 1, 1]],
[[0, 0, 1], [-1, -2, -2]], [[0, 0, -1], [-1, -2, -2]], [[0, 0, 1], [1, 2, 2]], [[0, 0, -1], [1, 2, 2]],
[[1, 2, 2], [0, 0, -1]], [[1, 2, 2], [0, 0, 1]], [[-1, -2, -2], [0, 0, -1]], [[-1, -2, -2], [0, 0, 1]],
[[1, 1, 2], [0, -1,-1]], [[0, 1, 1], [-1, -1, -2]], [[-1, -1, -2], [0, -1, -1]] , [[0, -1, -1], [-1, -1, -2]],
[[1, 1, 2], [0, 1,1]], [[0, 1, 1], [1, 1, 2]], [[-1, -1, -2], [0, 1, 1]] , [[0, -1, -1], [1, 1, 2]],
[[1, 1, 2], [0, -1,0]], [[1, 1, 2], [0, 1,0]], [[-1, -1, -2], [0, -1,0]] , [[-1, -1, -2], [0, 1, 0]],
[[0, 1, 0], [1, 1, 2]], [[0, -1, 0], [1, 1, 2]], [[0, 1, 0], [-1, -1, -2]] , [[0, -1, 0], [-1, -1, -2]]
]
m = 0
for i in range(row):
  for j in range(col):
    for s in shape:
      x_1 = i + s[0][0]
      x_2 = i + s[0][1]
      x_3 = i + s[0][2]
      y_1 = j + s[1][0]
      y_2 = j + s[1][1]
      y_3 = j + s[1][2]
      if x_1 < row and x_2 < row and x_3 < row and y_1 < col and y_2 < col and y_3 < col and x_1 >= 0 and x_2 >= 0 and x_3 >= 0 and y_1 >= 0 and y_2 >= 0 and y_3 >= 0 :

        temp = tetro[x_1][y_1] + tetro[x_2][y_2] + tetro[x_3][y_3] + tetro[i][j]

        m = max(m, temp)

print(m)
