# https://www.acmicpc.net/problem/15654

from itertools import *
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in permutations(l,m):
    print(*i)