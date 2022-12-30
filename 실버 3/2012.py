# https://www.acmicpc.net/problem/2012

import sys
input=sys.stdin.readline
n = int(input())
a = []
s = 0
for _ in range(n):
  a.append(int(input()))
a.sort()
for i in range(n):
  s+=abs(a[i]-i-1)
print(s)