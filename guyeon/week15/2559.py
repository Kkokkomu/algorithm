import sys

input = sys.stdin.readline

N,K = map(int,input().split())

days = list(map(int, input().split()))

left = 0
rifht = K-1
res = sum(days[:K])
now = res
for i in range(1, N-K+1):
    res = max(res, days[i:i+K])
print(res)
