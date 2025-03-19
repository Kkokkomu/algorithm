#1202
import sys

input = sys.stdin.readline

N=int(input())

li=[0,1,1,2]
ssli = sum(li)

for i in range(4,N+1):
    # 증식
    li.append(ssli)
    ssli += ssli

    # 사망
    if i%2==0:
        if i>2:
            ssli -= li[i-3]
            li[i-3] = 0
        if i>3:
            ssli -= li[i-4]
            li[i-4] = 0

print(sum(li[:N+1]))