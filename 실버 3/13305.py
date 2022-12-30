# https://www.acmicpc.net/problem/13305

input()
d = list(map(int,input().split()))
m = list(map(int,input().split()))

# 하나씩 비교하고 최소값 기억
num_min = m[0]
s = 0
for i in range(len(m)-1):
  num_min = min(num_min,m[i])
  s += num_min*d[i]
print(s)