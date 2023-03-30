# https://www.acmicpc.net/problem/15664

from itertools import *
n,m=map(int, input().split())
l=sorted(map(int, input().split()))
for i in sorted(set(combinations(l, m))):
    print(*i)