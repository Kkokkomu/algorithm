import sys
from collections import Counter

input = sys.stdin.readline

N=int(input())

all = []
for _ in range(N):
    all.append(input().strip())

counter = Counter(all)

for _ in range(N-1):
    counter[input().strip()] -= 1

print(counter.most_common(1)[0][0])