#0347
import sys

input = sys.stdin.readline

king, rock, c = input().split()
king = list(king)
rock = list(rock)

king[0] = ord(king[0]) - ord('A')
king[1] = int(king[1])-1

rock[0] = ord(rock[0]) - ord('A')
rock[1] = int(rock[1])-1

def go_rock(cmd):
    # print(f"before rock: {rock}")
    ki = rock[0]
    kj = rock[1]

    if cmd == 'R':
        ki += 1
    elif cmd == 'L':
        ki -= 1
    elif cmd == 'B':
        kj -= 1
    elif cmd == 'T':
        kj += 1
    elif cmd == "RT":
        ki += 1
        kj += 1
    elif cmd == "LT":
        ki -= 1
        kj += 1
    elif cmd == "RB":
        ki += 1
        kj -= 1
    elif cmd == "LB":
        ki -= 1
        kj -= 1
    
    if 0<=ki<8 and 0<=kj<8:
        rock[0] = ki
        rock[1] = kj
        # print(f"after rock: {rock}")
        return True
    else:
        return False


def go_king(cmd):
    # print(cmd)
    # print(f"before king: {king}")
    ki = king[0]
    kj = king[1]

    if cmd == 'R':
        ki += 1
    elif cmd == 'L':
        ki -= 1
    elif cmd == 'B':
        kj -= 1
    elif cmd == 'T':
        kj += 1
    elif cmd == "RT":
        ki += 1
        kj += 1
    elif cmd == "LT":
        ki -= 1
        kj += 1
    elif cmd == "RB":
        ki += 1
        kj -= 1
    elif cmd == "LB":
        ki -= 1
        kj -= 1
    
    if 0<=ki<8 and 0<=kj<8:
        if ki == rock[0] and kj == rock[1]:
            if not go_rock(cmd):
                return
        king[0] = ki
        king[1] = kj
        # print(f"after king: {king}")

for _ in range(int(c)):
    cmd = input().rstrip()
    go_king(cmd)

print(chr(king[0] + ord('A')), end='')
print(king[1]+1)

print(chr(rock[0] + ord('A')), end='')
print(rock[1]+1)