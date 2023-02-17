# https://www.acmicpc.net/problem/2822

l=sorted([(int(input()),i) for i in range(1,9)],reverse=True)
r=[]
s=0
for i,j in l[:5]:
  s+=i
  r.append(j)
print(s)
print(*sorted(r))