import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))

left = 0
right = max(li)
res = 0

def isValid(mid):
    low = high = li[0]
    divid = 1
    for n in li:
        if high < n:
            high = n
        if low > n:
            low = n
        if high-low > mid:
            divid+=1
            high=n
            low=n
    return divid <= M

while left <= right:
    mid = (right+left)//2

    if isValid(mid):
        right = mid-1
        res = mid
    else:
        left = mid+1
print(res)