# https://www.acmicpc.net/problem/1181

l=[]
for _ in range(int(input())):
  n = input()
  l.append((len(n),n))
pre=''
for i,j in sorted(l):
  if pre!=j:
    print(j)
    pre=j