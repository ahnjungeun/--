# https://www.acmicpc.net/problem/10845

import sys

n = int(input())
res = []

for _ in range(n):
  s = sys.stdin.readline().split()
  
  if len(s)>1:
    num = int(s[1])
    
  if s[0] == 'push': res.append(num)
  elif s[0] == 'pop':
    if not res: print(-1)
    else: print(res.pop(0))
  elif s[0] == 'size': print(len(res))
  elif s[0] == 'empty':
    if not res: print(1)
    else: print(0)
  elif s[0] == 'front':
    if not res: print(-1)
    else: print(res[0])
  elif s[0] == 'back':
    if not res: print(-1)
    else: print(res[-1])