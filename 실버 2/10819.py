# https://www.acmicpc.net/problem/10819

from itertools import *
n=int(input())
l=map(int,input().split())
s=0
for i in permutations(l,n):
  p=i[0]
  t=0
  for j in i[1:]:
    t+=abs(j-p)
    p=j
  s=max(s,t)
print(s)