# https://www.acmicpc.net/problem/15656

from itertools import *
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in product(l,repeat=m):
    print(*i)