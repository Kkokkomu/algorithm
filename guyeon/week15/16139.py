#1500
import sys

input = sys.stdin.readline

def get_idx(s):
    return ord(s)-97

st = input().rstrip()
N = int(input())
dec = [[0] * len(st) for _ in range(26)]

dec[get_idx(st[0])][0] = 1

for i in range(1, len(st)):
    idx = get_idx(st[i])
    for j in range(len(dec)):
        if idx == j:
            dec[j][i] = dec[j][i-1]+1
        else:
            dec[j][i] = dec[j][i-1]

def fre(s, e, tg):
    s = int(s)
    e = int(e)
    idx = get_idx(tg)

    if st[s] == tg:
        return dec[idx][e]-dec[idx][s] + 1
    else:
        return dec[idx][e]-dec[idx][s]
    
for _ in range(N):
    tg,b,c = input().split()
    print(fre(b,c,tg))
