# https://www.acmicpc.net/problem/1758

n=int(input())
l=sorted([int(input()) for _ in range(n)])[::-1]
s=0
for i,v in enumerate(l):
  s+= 0 if v<i else v-i
print(s)