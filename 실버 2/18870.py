# https://www.acmicpc.net/problem/18870

input()
l=map(int,input().split())
r=sorted([[i,v] for i,v in enumerate(l)],key=lambda x : x[1])
p=None
k=-1
for i in range(len(r)):
  if r[i][1]!=p:
    k+=1
  p=r[i][1]
  r[i][1]=k

for i,v in sorted(r):
  print(v,end=' ')