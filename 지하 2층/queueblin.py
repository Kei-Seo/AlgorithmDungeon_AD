import sys
n = int(sys.stdin.readline())
queue = []

for _ in range(n):
  command = sys.stdin.readline().strip()
  
  if command == "pop":
    if len(queue) == 0:
      print("-1")
    else:
      temp = queue.pop(0)
      print(temp)
  elif command == "size":
    print(len(queue))
  elif command == "empty":
    if len(queue) == 0:
      print("1")
    else:
      print("0")
  elif command == "front":
    if len(queue) == 0:
      print("-1")
    else:
      print(queue[0])
  elif command == "back":
    if len(queue) == 0:
      print("-1")
    else:
      print(queue[len(queue)-1])
  else:
    command, num = command.split(" ")
    queue.append(int(num))
