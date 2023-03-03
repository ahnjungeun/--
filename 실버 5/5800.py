# https://www.acmicpc.net/problem/5800

for i in range(int(input())):
  l = sorted(list(map(int,input().split()))[1:])
  m=0
  for j in range(len(l)-1):
    n = l[j+1]-l[j]
    m = n if n>m else m
  print(f'Class {i+1}')
  print(f'Max {l[-1]}, Min {l[0]}, Largest gap {m}')