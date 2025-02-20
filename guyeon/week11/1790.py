import sys

input=sys.stdin.readline

N, K = map(int, input().split())

de = [9*(10**i)*(i+1) for i in range(10)] # 자리수 판별을 위한 배열

ss=0
idx=0 # 자리수 - 1
for i in range(10): # 자리수를 늘려가면서 누적해보고 값을 넘으면 자리수 판정
    ss+=de[i]
    if ss >= K:
        idx=i
        break

n = sum(de[:idx])+1 # 이전 자리수들을 모두 더해서 start값 구하기 ex) 100 1000 10000에서 1의 자리수 누적값
rng = idx+1 # 자리수

d = (K-n)//rng # 자리수 만큼 전진했을때 몇번째에 멈추는지 목표값과 초기값의 차를 나눠서 계산
m = (K-n)%rng # 멈춘 값에서 몇을 전진하면 목표가 나오는지 계산
num = (10**idx)+d

if num > N:
    print(-1)
else:
    print(str(num)[m])
