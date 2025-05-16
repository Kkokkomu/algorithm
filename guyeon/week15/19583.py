# 먼저 시작 시간보자 작거나 같은 이름들 전부 set에 저장
# 끝난 시간 이후에는 break하고
# 퇴실에 적합한 인원이면, set에 인원과 비교
import sys

input = sys.stdin.readline

S,E,Q = input().split()

sts1 = set()
sts2 = set()

while True:
    try:
        time, name = input().split()

        if time <= S:
            sts1.add(name)
        elif E <= time <= Q:
            sts2.add(name)
    except:
        break

print(len(sts1&sts2))