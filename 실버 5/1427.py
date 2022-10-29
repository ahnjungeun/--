# https://www.acmicpc.net/problem/1427

s = list(input())
s.sort(reverse=True)
print(*s,sep='')