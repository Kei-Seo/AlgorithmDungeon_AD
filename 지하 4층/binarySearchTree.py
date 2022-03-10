import sys
sys.setrecursionlimit(10 ** 6)
tree = []
def postOrder(start , end):
  if start > end:
    return 
  root = tree[start]
  index = start+1

  while index <= end:
    if tree[index] > root:
      break
    index += 1

  postOrder(start+1, index-1)
  postOrder(index, end)
  print(root)

while True:
  try:
    tree.append(int(sys.stdin.readline()))
  except:
    break

postOrder(0, len(tree)-1)
