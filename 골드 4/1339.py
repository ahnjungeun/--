# https://www.acmicpc.net/problem/1339

l=[input() for _ in range(int(input()))]

o={}
for i in l:
  d=len(i)-1
  for j in i:
    if j in o:
      o[j]+=pow(10,d)
    else:
      o[j]=pow(10,d)
    d-=1

o=sorted(o.items(),key=lambda x:x[1])[::-1]

d={}
n=9
for i,j in o:
  d[i]=str(n)
  n-=1

for i in range(len(l)):
  for j in l[i]:
    l[i]=l[i].replace(j,d[j])

r=0
for i in l:
  r+=int(i)
print(r)