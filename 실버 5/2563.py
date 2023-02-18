# https://www.acmicpc.net/problem/2563

m=[[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
  a,b = map(int,input().split())
  for i in range(a-1,a+9):
    for j in range(b-1,b+9):
      m[i][j]=1
s=0
for l in m:
  s+=sum(l)
print(s)