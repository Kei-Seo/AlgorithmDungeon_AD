n, m = map(int, input().split(" "))
c_list = list(map(int, input().split(" ")))
answer = 0

for x in range(len(c_list)):
  temp_ans = 0
  temp = c_list.pop(0)
  temp_list = c_list
  for y in range(len(temp_list)):
    for z in range(y+1, len(temp_list)):
      temp_ans = temp + temp_list[y] + temp_list[z]
      if((m-temp_ans)>=0 and answer<=temp_ans):
        answer = temp_ans
      
print(answer)
