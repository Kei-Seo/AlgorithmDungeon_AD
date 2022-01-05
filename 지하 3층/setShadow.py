import sys

input = sys.stdin.readline

n = int(input())
answer = set([])
for _ in range(n):
  tokens = input().rstrip()
  if tokens == "all":
    answer= set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  elif tokens == "empty":
    answer = set([])
  else:
    token, x = tokens.split(" ")
    if token == "add":
      answer.add(int(x))
    elif token == "remove":
      check = False
      for i in answer:
        if i == int(x):
          check = True
      if check:
        answer.remove(int(x))
    elif token == "check":
      check = False
      for i in answer:
        if i == int(x):
          check = True
      if check:
        print(1)
      else:
        print(0)
    
    elif token == "toggle":
      check = False
      for i in answer:
        if i == int(x):
          check = True
      if check:
        answer.remove(int(x))
      else:
        answer.add(int(x))
