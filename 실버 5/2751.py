# https://www.acmicpc.net/problem/2751

import sys
n = int(input())
res = []
for _ in range(n):
  res.append(int(sys.stdin.readline()))
for i in sorted(res):
  print(i)