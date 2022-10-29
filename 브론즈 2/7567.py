# https://www.acmicpc.net/problem/7567

p = ''
res = 0
for i in input():
  if i == p:
    res += 5
  else:
    res += 10
  p = i
print(res)