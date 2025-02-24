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
    print(ching[bisect_left(num, n)])
