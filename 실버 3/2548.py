# https://www.acmicpc.net/problem/2548

n=int(input())-1
print(sorted(map(int,input().split()))[n//2])