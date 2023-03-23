# https://www.acmicpc.net/problem/15657

from itertools import *
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in combinations_with_replacement(l,m):
  print(*i)