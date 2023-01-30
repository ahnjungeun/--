# https://www.acmicpc.net/problem/3036

import math
input()
l=input().split()
a=int(l[0])
for i in l[1:]:
  i=int(i)
  g=math.gcd(a,i)
  print(f'{int(a/g)}/{int(i/g)}')