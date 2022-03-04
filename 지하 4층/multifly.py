import sys
a, b, c = map(int, sys.stdin.readline().split())

def mul(a, b):
  if b == 1:
    return a%c
  else:
    tmp = mul(a, b//2)
    if a%2 == 0:
      return (tmp * tmp) % c
    else:
      return (tmp * tmp * a) % c
  
print(mul(a,b))
                    
