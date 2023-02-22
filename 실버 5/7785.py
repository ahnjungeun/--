# https://www.acmicpc.net/problem/7785

l={}
for _ in range(int(input())):
  n,w = input().split()
  if w=='enter':
    l[n]=w
  else:
    del l[n]
for i in sorted(l.keys(),reverse=True):
  print(i)