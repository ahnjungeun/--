# https://www.acmicpc.net/problem/10039

s = 0
for _ in range(5):
  n = int(input())
  if n < 40:
    n = 40
  s += n
print(int(s/5))