# https://www.acmicpc.net/problem/5532

import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
a = math.ceil(a/c)
b = math.ceil(b/d)
print(l-a if a>b else l-b)