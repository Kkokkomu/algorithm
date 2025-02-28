import sys
#0200

def mul(li):
    res=1
    for l in li:
        res*=l
    return res

def uc(a,b):
    if a < b:
        a,b = b,a
    while True:
        c = a%b
        if c==0:
            return b
        a=b
        b=c

N=int(input())
liN = list(map(int,input().split()))

M=int(input())
liM=list(map(int,input().split()))

res = str(uc(mul(liN), mul(liM)))

if len(res) > 9:
    res = res[-9:]
print(res)