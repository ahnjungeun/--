# https://www.acmicpc.net/problem/11656

s=input()
l=[]
for i in range(len(s)):
  l.append(s[i:])
for i in sorted(l):
  print(i)