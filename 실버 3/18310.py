# https://www.acmicpc.net/problem/18310

n=int(input())
l=sorted(map(int,input().split()))
print(l[(n-1)//2])