# https://www.acmicpc.net/problem/15655

from itertools import *
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in combinations(l,m):
    print(*i)