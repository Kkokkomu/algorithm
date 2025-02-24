import sys

input = sys.stdin.readline

N = int(input())

li = list(map(int, input().split()))
li.sort()

if N%2==0:
    print(sum(li[N//2:])*2)
else:
    print(sum(li[N//2+1:])*2+li[N//2])