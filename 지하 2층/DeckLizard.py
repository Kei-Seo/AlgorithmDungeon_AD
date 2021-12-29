import sys
n = int(sys.stdin.readline())
deck = []

for _ in range(n):
  command = sys.stdin.readline().strip()
  
  if command == "pop_front":
    if len(deck) == 0:
      print("-1")
    else:
      temp = deck.pop(0)
      print(temp)
  elif command == "pop_back":
    if len(deck) == 0:
      print("-1")
    else:
      temp = deck.pop()
      print(temp)
  elif command == "size":
    print(len(deck))
  elif command == "empty":
    if len(deck) == 0:
      print("1")
    else:
      print("0")
  elif command == "front":
    if len(deck) == 0:
      print("-1")
    else:
      print(deck[0])
  elif command == "back":
    if len(deck) == 0:
      print("-1")
    else:
      print(deck[len(deck)-1])
  else:
    command, num = command.split(" ")
    if command == "push_back":
      deck.append(int(num))
    elif command == "push_front":
      deck.insert(0, int(num))
      
