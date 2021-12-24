testcase = int(input())
answer_list = []
real_priority = 0

for k in range(testcase):
  answer = 0
  n, target = map(int, input().split())
  priority = list(map(int, input().split()))
  max_priority = max(priority)
  real_priority = priority[target]
  priority[target] = 0 # 타겟은의 우선순위는 0임 
  i = 0
  while (len(priority) >= 0):
    if priority[0] == 0:
      if max_priority == real_priority:
         answer += 1
         break
    if max_priority == priority[0]:
      priority.pop(0)
      max_priority = max(priority)
      max_priority = max(max_priority, real_priority)
      answer += 1
      i = 0
    else:
      temp = priority.pop(0)
      priority.append(temp)
      i += 1
  answer_list.append(answer)
  
for x in answer_list:
  print(x)
