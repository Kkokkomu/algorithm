import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, divid = map(int, input().split())

mx = -int(1e9)
mn = int(1e9)

def dfs(n, ssum, pl, mi, mu, di):
    global mx
    global mn
    if n == N-1:
        if ssum > mx:
            mx = ssum
        if ssum < mn:
            mn = ssum
        return
    
    if pl != 0:
        dfs(n+1, ssum+nums[n+1], pl-1, mi, mu, di)
    if mi != 0:
        dfs(n+1, ssum-nums[n+1], pl, mi-1, mu, di)
    if mu != 0:
        dfs(n+1, ssum*nums[n+1], pl, mi, mu-1, di)
    if di != 0:
        dfs(n+1, int(ssum/nums[n+1]), pl, mi, mu, di-1)
        # if ssum < 0 and nums[n+1] > 0:
        #     dfs(n+1, (-1 * ((-1 * ssum)//nums[n+1])), pl, mi, mu, di-1)
        # else:
            # dfs(n+1, ssum//nums[n+1], pl, mi, mu, di-1)
    

dfs(0, nums[0],plus,minus,mul,divid)
print(mx)
print(mn)