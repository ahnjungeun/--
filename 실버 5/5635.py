# https://www.acmicpc.net/problem/5635

import datetime as dt
l=[]
for _ in range(int(input())):
  n,d,m,y=input().split()
  l.append((dt.datetime(int(y),int(m),int(d)),n))
l.sort()
print(l[-1][1],l[0][1],sep='\n')