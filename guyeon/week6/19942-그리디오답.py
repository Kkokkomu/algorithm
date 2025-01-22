import sys
from collections import deque

N = int(sys.stdin.readline())
mp, mf, ms, mv = map(int, sys.stdin.readline().split())

li = []
for i in range(N):
    p, f, s, v, c = map(int, sys.stdin.readline().split())
    li.append([p, f, s, v, c, i])
print(li)
li = sorted(li, key=lambda x: x[4], reverse=True)
li = deque(li)
print(li)

buckets = deque()

sp = sf = ss = sv = 0
for _ in range(3):
    buckets.append(li.popleft())
    sp += buckets[-1][0]
    sf += buckets[-1][1]
    ss += buckets[-1][2]
    sv += buckets[-1][3]
print()
while li:
    current = li.popleft()
    # 리스트 맨위 원소(젤 비싼거)부터
    for bucket in buckets:
        print(f"buckets {buckets}")
        print(f"current {current}")
        print(f"li {li}")


    # 버킷에 젤 비싼것들부터 검사해서 대체 가능한지 확인
        if mp <= sp - (bucket[0]-current[0]):
            if mf <= sf - (bucket[1]-current[1]):
                if ms <= ss - (bucket[2]-current[2]):
                    if mv <= sv - (bucket[3]-current[3]):
                        if bucket[4] != current[4]:
                            buckets.remove(bucket)
                            buckets.append(current)
                            sp = sp - (bucket[0]-current[0])
                            sf = sf - (bucket[1]-current[1])
                            ss = ss - (bucket[2]-current[2])
                            sv = sv - (bucket[3]-current[3])
                            print(f"buckets {buckets}")
                            break
    

res = 0
for bucket in buckets:
    res+=bucket[4]
print(res)

buckets = sorted(buckets, key=lambda x: x[5], reverse=True)
for bucket in buckets:
    print(bucket[5], end=' ')

print(f"sp {sp}, sf {sf}, ss {ss}, sv {sv}")
print(buckets)