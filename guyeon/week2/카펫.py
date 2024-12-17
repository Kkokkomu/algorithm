from math import sqrt

def solution(brown, yellow): # 0352~0405
    sy = int(sqrt(yellow))
    
    for i in range(1,sy+1):
        if yellow%i == 0:
            if ((i+2)*2 + (yellow//i)*2) == brown:
                return [yellow//i+2,i+2]
