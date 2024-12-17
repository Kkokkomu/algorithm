from itertools import permutations

def solution(k, dungeons):#0412~0419
    
    res = 0
    p = permutations(dungeons)
    for pp in p:
        kk=k
        cnt=0
        for ppp in pp:
            if kk >= ppp[0]:
                cnt+=1
                kk-=ppp[1]
            else:
                break
                
        if res < cnt:
            res = cnt
    
    return res