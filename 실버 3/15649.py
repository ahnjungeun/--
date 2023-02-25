# https://www.acmicpc.net/problem/15649

from itertools import *
a,b=map(int,input().split())
for i in permutations(range(1,a+1),b):
  print(*i)