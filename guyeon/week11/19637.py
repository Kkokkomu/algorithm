import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())

ching = []
num=[]
for _ in range(N):
    s, n = input().split()
    ching.append(s)
    num.append(int(n))

for _ in range(M):
    n = int(input())
    left = 0
    right = N-1
    res=0
    while left <= right:
        mid = (left+right)//2
        if n <= num[mid]:
            right = mid-1
            res = mid
        else:
            left = mid+1
    print(ching[res])
