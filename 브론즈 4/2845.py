# https://www.acmicpc.net/problem/2845

a, b = map(int,input().split())
list1 = list(map(int,input().split()))
total = a*b
for i in list1:
  print(i - total,end=' ')