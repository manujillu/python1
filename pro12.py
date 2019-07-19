from itertools import combinations
Si,s=map(int,input().split())
li=len(str(Si))
lst=list(combinations(str(Si),li-s))
lst=sorted(lst)
print(*lst[0],sep='')
