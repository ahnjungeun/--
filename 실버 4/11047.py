# https://www.acmicpc.net/problem/11047

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
s = 0
for i in l[::-1]:
  r = m // i
  if r == 0:
    continue
  else:
    s += r # 여기서 r을 더하는데 0이어도 상관없구나! 계속 이걸로 코드 늘어나네 ㅋㅋ;;
    m %= i
print(s)