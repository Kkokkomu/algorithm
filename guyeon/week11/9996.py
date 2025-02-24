#830
import sys

input = sys.stdin.readline

N = int(input())

st = input().strip()
mnlen = len(st) -1
idx = st.index('*')
left = st[:idx]
right = st[idx+1:]
rl = len(right)

for _ in range(N):
    stt = input().strip()
    if len(stt) >= mnlen:
        # print(f"stt[:idx]: {stt[:il:]}, right: {righdx]}, left: {left}")
        # print(f"stt[idx:]: {stt[-rt}")

        if stt[:idx] == left and stt[-rl:] == right:
            print("DA")
            continue
    print("NE")