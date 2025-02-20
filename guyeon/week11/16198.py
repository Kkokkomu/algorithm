import sys

input = sys.stdin.readline

N=int(input())
li = list(map(int,input().split()))

res=0
def dfs(arr, num):
    global res
    if len(arr)==2:
        if res < num:
            res=num
            return
    for i in range(1, len(arr)-1):
        dfs(arr[:i] + arr[i+1:], num + arr[i-1]*arr[i+1])

dfs(li,0)

print(res)