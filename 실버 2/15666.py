# https://www.acmicpc.net/problem/15666

from itertools import *
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for i in sorted(set(combinations_with_replacement(l,m))):
    print(*i)