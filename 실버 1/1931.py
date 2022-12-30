# https://www.acmicpc.net/problem/1931

l=[]
c=1
n=int(input())
for _ in range(n):
  a,b=map(int,input().split())
  l.append((b,a))
l.sort()

pre=l[0][0]
for i in range(len(l)-1):
  if pre<=l[i+1][1]:
    pre=l[i+1][0]
    c+=1
print(c)