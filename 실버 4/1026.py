# https://www.acmicpc.net/problem/1026

n = input()
l = sorted(map(int,input().split()))
l2 = sorted(map(int,input().split()),reverse=True)
s = 0
for i in range(len(l)):
  s += l[i]*l2[i]
print(s)