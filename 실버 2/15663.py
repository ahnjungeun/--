# https://www.acmicpc.net/problem/15663

from itertools import *
n,m=map(int,input().split())
l=map(int,input().split())
for i in sorted(set(permutations(l,m))):
    print(*i)