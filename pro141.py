mi1,ni=map(str,input().split())
t=0
if len(mi1)>len(ni):
  mi1,ni=ni,mi1
r=0
while r<len(mi1):
  t+=(ord(ni[r])-ord(mi1[r]))
  r+=1
for r in range(r,len(ni)):
  t+=ord(ni[r])-ord('a')+1
print(t)
