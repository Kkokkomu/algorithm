import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
fts = list(map(int, input().split()))

cnt = defaultdict(int)

res = 0
left = 0
setCnt = 0
for right in range(N):
    if cnt[fts[right]] == 0:
        setCnt += 1
    cnt[fts[right]] += 1

    while 2 < setCnt:
        cnt[fts[left]] -= 1
        if cnt[fts[left]] == 0:
            setCnt-=1
        left += 1
    
    res = max(res, right-left+1)
print(res)

# 슬라이싱 윈도우가 좋다 하더라...