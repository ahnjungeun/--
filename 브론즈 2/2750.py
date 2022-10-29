# https://www.acmicpc.net/problem/2750

n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
l.sort()
for i in l:
  print(i)