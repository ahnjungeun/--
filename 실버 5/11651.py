# https://www.acmicpc.net/problem/11651

l=[]
for _ in range(int(input())):
  x,y=map(int,input().split())
  l.append((y,x))
for y,x in sorted(l):
  print(x,y)