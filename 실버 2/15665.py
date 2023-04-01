# https://www.acmicpc.net/problem/15665

from itertools import *
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in sorted(set(product(l,repeat=m))):
    print(*i)