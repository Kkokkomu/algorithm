import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

S = deque()
for _ in range(N):
    S.append(input().strip())

T=""
while len(S)>1:
    ll = len(S)
    for i in range(ll//2):
        if S[i] < S[ll-i-1]:
            T += S.popleft()
            break
        elif S[i] > S[ll-i-1]:
            T += S.pop()
            break
        elif i == (ll//2)-1:
            T += S.popleft()
            break
T += S.pop()

# 멋있는 한 줄
print(*[T[i:i+80] for i in range(0, len(T), 80)], sep='\n')