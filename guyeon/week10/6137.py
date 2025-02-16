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

while len(T) > 80:
    print(T[:80])
    T = T[80:]
print(T)