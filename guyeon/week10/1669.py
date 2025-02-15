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
    # print(f"cumul : {cumul}")
    # print(f"now : {now}")
    # print()

    for i in (1,0,-1):
        tmp = now + i
        e = ((tmp+1)*(tmp))//2
        # print(i)

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