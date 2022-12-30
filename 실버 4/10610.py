# https://www.acmicpc.net/problem/10610

import itertools
n = sorted(input(),reverse=True)
l = sum(map(int,n))

if l%3==0 and n.count('0'):
  r = []
  for i in itertools.permutations(n,len(n)):
    l = list(i)
    s = int(''.join(l))
    if s%30==0:
      print(s)
      break
else:
  print(-1)

# 코드보완
n = sorted(input(),reverse=True)
l = sum(map(int,n))
if l%3==0 and n.count('0'):
  print(''.join(n))
else:
  print(-1)