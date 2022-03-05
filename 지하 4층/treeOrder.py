import sys
n = int(sys.stdin.readline())

class Node(object):
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

tree = {}

for _ in range(n):
  a, b, c = input().rstrip().split()
  tmp = Node(data = a, left=b, right=c)
  tree[a] = tmp

pre_res = []
post_res = []
in_res = []


def preOrder(node):
  pre_res.append(node)
  tmp = tree[node]
  if tmp.left != '.':
    preOrder(tmp.left)
  if tmp.right != '.':
    preOrder(tmp.right)

def postOrder(node):
  tmp = tree[node]
  if tmp.left != '.':
    postOrder(tmp.left)
  if tmp.right != '.':
    postOrder(tmp.right)
  post_res.append(node)

def inOrder(node):
  tmp = tree[node]
  if tmp.left != '.':
    inOrder(tmp.left)
  in_res.append(node)
  if tmp.right != '.':
    inOrder(tmp.right)
    

preOrder('A')
inOrder('A')
postOrder('A')
for c in pre_res:
  print(c, end='')
print()
for c in in_res:
  print(c, end='')
print()
for c in post_res:
  print(c, end='')
  
  
