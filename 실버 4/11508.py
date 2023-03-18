# https://www.acmicpc.net/problem/11508

import sys
input=sys.stdin.readline
l=sorted([int(input()) for _ in range(int(input()))])[::-1]
s=c=0
for i in l:
  s+=i if c%3!=2 else 0
  c+=1
print(s)