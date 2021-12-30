
zero = [1, 0, 1, 1, 2]
one = [0, 1, 1, 2, 3]

def fibonacci_sum(n):
  if n >= len(one):
    for i in range(len(one), n+1):
      one.append(one[i-1]+one[i-2])
      zero.append(zero[i-1]+zero[i-2])

  print("{} {}".format(zero[n], one[n]))

n = int(input())

for i in range(n):
  fibonacci_sum(int(input()))
  
