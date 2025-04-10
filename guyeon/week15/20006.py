#332
import sys

input = sys.stdin.readline

p, m = map(int,input().split())

rooms = []

def in_(level, id):
    global m

    for room in rooms:
        if room[0] != 999 and -10 <= room[0]-level <= 10:
            room[1].append((level, id))
            if len(room[1]) >= m:
                room[0] = 999
            return
    
    if m == 1:
        rooms.append([999, [(level, id)]])
    else:
        rooms.append([level, [(level, id)]])

for _ in range(p):
    level, id = input().split()
    in_(int(level), id)

for room in rooms:
    if room[0] == 999:
        print("Started!")
    else:
        print("Waiting!")
    
    room[1].sort(key=lambda x : x[1])
    for r in room[1]:
        print(r[0], end=' ')
        print(r[1])