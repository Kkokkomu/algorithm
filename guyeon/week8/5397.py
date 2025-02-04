import sys # 특수문자 출력

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    L = list(input().strip())

    right = []
    left = []
    for l in L:
        if l == "<":
            if left:
                right.append(left.pop())
        elif l == ">":
            if right:
                left.append(right.pop())
        elif l == "-":
            if left:
                left.pop()
        else:
            left.append(l)
    print("".join(left+right[::-1]))