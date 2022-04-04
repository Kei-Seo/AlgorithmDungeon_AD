import sys

exp = sys.stdin.readline().rstrip()

stack = []
post = []
prior = {'*':3, '/':3, '-':2, '+':2, '(':1}

for n in range(len(exp)):
  if exp[n].isalpha():
    post.append(exp[n])
  elif exp[n] == '(':
    stack.append(exp[n])
  elif exp[n] == ')':
    while stack[-1] != '(':
      post.append(stack.pop())
    stack.pop()
  else:
    while stack and prior[exp[n]] <= prior[stack[-1]]:
      post.append(stack.pop())
    stack.append(exp[n])

while stack:
  post.append(stack.pop())

for i in post:
  print(i, end='')
