# https://www.acmicpc.net/problem/11399

n = int(input())
l = sorted(map(int,input().split()))
s = 0
for i in range(len(l)):
  s += sum(l[:i+1])
print(s)