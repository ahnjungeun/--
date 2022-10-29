# https://www.acmicpc.net/problem/3052

l = map(int,open(0))
s = set([])
for i in l:
  s.add(i % 42)
print(len(s))