import sys
from collections import deque

while True:
  c_error = False 
  stmt = sys.stdin.readline().rstrip()
  queue = []
  if stmt == ".":
    break
  for t in stmt:
    if t == '(':
      queue.append('(')
    elif t == '[':
      queue.append('[')
    elif t == ']':
      if len(queue) > 0:
        if '[' == queue[len(queue)-1]:
          queue.pop()
        else:
          c_error = True
      else:
        c_error = True
    elif t == ')':
      if len(queue) > 0:
        if '(' == queue[len(queue)-1]:
          queue.pop()
        else:
          c_error = True
      else:
        c_error = True
  if len(queue) == 0 and not c_error:
    print("yes")
  else:
    print("no")

