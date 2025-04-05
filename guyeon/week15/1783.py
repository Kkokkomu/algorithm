# 850
import sys

N,M = map(int,sys.stdin.readline().split())

if N == 1:
    res = 1
elif N == 2:
    res = (M-1)//2 + 1
    if res > 4:
        res = 4
elif M<7:
    res = M-1 + 1
    if res > 4:
        res = 4
else:
    res = M-7 + 4 + 1

print(res)