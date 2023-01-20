# https://www.acmicpc.net/problem/11650

l=[]
for _ in range(int(input())):
    a,b = map(int,input().split())
    l.append((a,b))
for i,j in sorted(l):
  print(i,j)