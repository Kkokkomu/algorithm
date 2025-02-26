import sys

T = int(input())

def bs(li, n):
    s, e = 0, len(li)-1
    while s <= e:
        m = (s+e)//2
        if li[m] == n:
            return 1
        elif li[m] < n:
            s = m+1
        else:
            e = m-1
    return 0

for _ in range(T):
    N = int(input())

    note1 = list(map(int, input().split()))
    note1.sort()

    M = int(input())

    note2 = list(map(int, input().split()))

    for n2 in note2:
        res=0
        s, e = 0, len(note1)-1
        while s <= e:
            m = (s+e)//2
            if note1[m] == n2:
                res=1
                break
            elif note1[m] < n2:
                s = m+1
            else:
                e = m-1
        print(res)
