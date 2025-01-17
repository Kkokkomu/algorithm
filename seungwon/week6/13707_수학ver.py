from math import factorial

N, K = map(int, input().split())

# 조합 공식을 이용하여 풀이
# N을 K개로 나타내는 방법의 수는
# N개의 O 사이에 K - 1개의 |를 넣는 경우의 수와 같다
print((factorial(N + K - 1) // (factorial(K - 1) * factorial(N))) % 1000000000)
