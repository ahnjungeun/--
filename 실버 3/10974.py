# https://www.acmicpc.net/problem/10974

from itertools import *
n=int(input())
for i in permutations(range(1,n+1)):
  print(*i)