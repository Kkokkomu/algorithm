#0350
import sys

input = sys.stdin.readline

N=int(input())
li = list(map(int,input().split()))
visited = [-1] * N

for i in range(1,N+1): # 제일 작은 사람부터 순회하고
    cnt=0
    for j in range(N): # 안채워진 순서의 개수가 현재 세우려는 키의 순서와 일치하면 거기에 세움
        if visited[j] == -1:
            if cnt == li[i-1]:
                visited[j] = i
                break
            cnt+=1
print(" ".join(list(map(str,visited))))
        
        