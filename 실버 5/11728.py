# https://www.acmicpc.net/problem/11728

input()
a=map(int,input().split())
b=map(int,input().split())
print(*sorted([*a,*b]))