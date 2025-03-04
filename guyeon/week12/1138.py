#0350
import sys

input = sys.stdin.readline

N=int(input())
li = list(map(int,input().split()))
visited = [-1] * N

for i in range(1,N+1):
    cnt=0
    for j in range(N):
        if visited[j] == -1:
            if cnt == li[i-1]:
                visited[j] = i
                break
            cnt+=1
print(" ".join(list(map(str,visited))))
        
        