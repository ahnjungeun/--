# https://www.acmicpc.net/problem/14469

l=[]
for _ in range(int(input())):
  a,b=map(int,input().split())
  l.append((a,b))
s=0
for i,j in sorted(l):
  s+= i+j-s if s<i else j
print(s)