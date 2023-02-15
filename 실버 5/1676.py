# https://www.acmicpc.net/problem/1676

import math
n=int(input())
c=0
for i in str(math.factorial(n))[::-1]:
  if i!='0':
    print(c)
    break
  c+=1