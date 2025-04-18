# 1850
import sys

cmds = list(sys.stdin.readline().rstrip())

idxs = {'q':0,'u':1,'a':2,'c':3,'k':4}

ducks = []
res = 0
for cmd in cmds:
    idx = idxs[cmd]
    # print(idx)
    # print(ducks)

    if idx not in ducks:
        if idx == 0:
            ducks.append(1)
            res +=1
            continue
        else:
            print(-1)
            exit()
    for i in range(len(ducks)):
        if ducks[i] == idx:
            if idx != 4:
                ducks[i] = ducks[i] + 1
            else:
                ducks[i] = 0
            break
    # print(ducks)
    # print()

for duck in ducks:
    if duck != 0:
        print(-1)
        exit()
print(res)