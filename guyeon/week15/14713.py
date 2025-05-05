#0159 ~ 0213
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

birds = []
for _ in range(N):
    birds.append(deque(map(str,input().split())))

words = list(map(str,input().split()))

def exist(word):
    for bird in birds:
        if len(bird) != 0 and bird[0] == word:
            bird.popleft()
            return True
    
    return False


for word in words:
    if not exist(word):
        print("Impossible")
        exit()

for bird in birds:
    if len(bird) != 0:
        print("Impossible")
        exit()

print("Possible")