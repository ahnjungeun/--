# https://www.acmicpc.net/problem/1049

n,m = map(int,input().split())
A,B = [],[]
for _ in range(m):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)
A.sort()
B.sort()
q=n//6
r=n%6

if A[0]>6*B[0]:
  print(n*B[0])
else:
  ans=(q+1)*A[0] if r*B[0]>A[0] else q*A[0]+r*B[0]
  print(ans)