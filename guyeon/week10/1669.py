import sys

input = sys.stdin.readline

X, Y = map(int, input().split())
if X==Y:
    print(0)
    exit()

dest = Y-X

cnt = 1
now = 1
cumul = 1
while cumul < dest:
    for i in (1,0,-1):
        tmp = now + i
        e = ((tmp+1)*(tmp))//2

        if e+cumul < dest:
            now +=i
            cumul +=tmp
            break
        elif e+cumul == dest:
                cnt += tmp
                print(cnt)
                exit()
    cnt += 1

print(cnt)