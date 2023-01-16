# https://www.acmicpc.net/problem/10814

l=[]
for _ in range(int(input())):
  a,n = input().split()
  l.append([int(a),n])
for i in sorted(l,key=lambda x:x[0]):
  print(*i)