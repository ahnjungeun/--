# https://www.acmicpc.net/problem/1439

import math
l = input()
pre = ''
count = 0
for i in l:
  if pre != i:
    count+=1
  pre = i
print(math.ceil(((count-1)/2)))