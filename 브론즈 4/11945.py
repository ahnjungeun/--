# https://www.acmicpc.net/problem/11945

h, w = map(int,input().split())
for _ in range(h):
  print(input()[::-1])