import sys

n, k = map(int, sys.stdin.readline().split())

poketmon_int_key = {}
poketmon_name_key = {} 

for i in range(n):
  name = sys.stdin.readline().rstrip()
  poketmon_int_key[i] = name
  poketmon_name_key[name] = i 

 
for _ in range(k):
  something = sys.stdin.readline().rstrip()
  if something.isdigit() :
    print(poketmon_int_key[int(something)-1])
  else:
    print(poketmon_name_key[something]+1)
