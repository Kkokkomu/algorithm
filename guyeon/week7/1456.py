import sys

A, B = map(int, sys.stdin.readline().split())

sB = B**(1/2) # 31.1312412414

primes = [True] * (int(sB)+1)
primes[0] = primes[1] = False

for i in range(2, int(sB**(1/2))+1): # 2 ~ 5...
    if primes[i]: # 소수 일 경우에는 해당 소수의 곱들을 소수가 아닌 것으로 처리
        for j in range(2, int(sB//i)+1):
            primes[i*j] = False

res=0
for i in range(2, int(sB)+1):
    if primes[i]:
        j=2
        while i**j <= B:
            if A <= i**j:
                res+=1
            j+=1

print(res)