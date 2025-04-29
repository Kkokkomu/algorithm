#14:00
import sys
from collections import Counter

input = sys.stdin.readline

N=int(input())

cnn = Counter(input().rstrip())

res = 0

def dict_len(dc):
    res = 0
    for v in dc.values():
        res += v
    return res

for _ in range(N-1):
    word = Counter(input().rstrip())
    if dict_len(word-cnn) <= 1 and dict_len(cnn-word) <= 1:
        res += 1

print(res)

