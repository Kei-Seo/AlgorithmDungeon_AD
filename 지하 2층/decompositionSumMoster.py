def remain(n, sum):
  a = n//10
  b = n%10
  if n//10 == 0:
    sum += b
    return sum
  else:
    sum += b
    return remain(a, sum)

n = int(input())
answer = 0
for x in range(n):
  y = remain(x, 0)
  temp = x + y
  if n == temp:
    answer = x    
    break

print(answer)
