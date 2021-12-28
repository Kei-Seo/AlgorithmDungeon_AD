
n = int(input())
for _ in range(n):
  brackets = input()
  bracket = []
  for x in range(len(brackets)):
    end = True
    if x == 0 and brackets[0] == ')':
      # 첫 괄호가 ) 로시작하면 잘못된거임
      print("NO")
      end = False
      break
    if brackets[x] == '(':
      bracket.append('(')
    else:
      if len(bracket) == 0:
        print("NO")
        end = False
        break
      bracket.pop()
  
  if end :
    if len(bracket) == 0 :
      print ("YES")
    else:
      print("NO")


      



