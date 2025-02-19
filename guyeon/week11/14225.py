import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

arr = [False] * (2000009)

def dfs(depth,idx,ss):
    if depth == N:
        return
    
    ss+=S[idx]
    arr[ss]=True
    dfs(depth+1,idx+1,ss)
    dfs(depth+1,idx+1,ss-S[idx])

dfs(0,0,0)
while True:
    print()
for i in range(1,2000009):
    if not arr[i]:
        print(i)
        exit()
