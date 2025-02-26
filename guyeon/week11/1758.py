import sys

input = sys.stdin.readline

N = int(input())

li=[]
for _ in range(N):
    li.append(int(input()))

li.sort(reverse = True)
res = 0
for i in range(N):
    n = li[i] - (i)
    if n > 0:
        res += n
print(res)