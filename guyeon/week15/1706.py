# 1057
import sys

input = sys.stdin.readline

def splt(st):
    res = []

    li = list(st)
    ss = ""
    for l in li:
        if l != '#':
            ss += l
        else:
            if len(ss) > 1:
                res.append(ss)
            ss = ""
    if len(ss) > 1:
        res.append(ss)
    
    return res

R,C = map(int,input().split())
words = []
for _ in range(R):
    words.append(input().rstrip())
for j in range(C):
    ss = ""
    for i in range(R):
        ss += words[i][j]
    words.append(ss)

res = "zzzzzzzzzzzzzzzzzzzzzzzzz"
for word in words:
    li = splt(word)
    if len(li) != 0:
        res = min(res, min(li))

print(res)