# https://www.acmicpc.net/problem/1246

n,m = map(int,input().split())
l=sorted([int(input()) for _ in range(m)])
k=len(l)
r=[]
for i in l:
  r.append(i*k)
  k-=1

M=max(r)
I=l[r.index(M)]
while M/I>n:
  r.remove(M)
  l.remove(I)
  M=max(r)
  I=l[r.index(M)]
print(I,M)