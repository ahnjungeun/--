# https://www.acmicpc.net/problem/17219

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l={}
for _ in range(n):
  i,v=input().strip().split()
  l[i]=v
f=[input().strip() for _ in range(m)]
for i in f:
  print(l[i])