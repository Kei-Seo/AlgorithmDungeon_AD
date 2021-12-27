while(True):
  triangle = list(map(int, input().split(" ")))
  if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
    break;
  
  triangle.sort(reverse = True)
  a = triangle[0] * triangle[0]
  b = triangle[1] * triangle[1]
  c = triangle[2] * triangle[2]

  if a == (b+c) :
    print("right")
  else:
    print("wrong")


  
