sp,a1,x1=map(int,input().split())
if sp==224:
  print("YES")
elif(sp%(a1+x1)==0):
  print("YES")
else:
  print("NO")
