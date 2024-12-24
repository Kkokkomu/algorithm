from collections import deque

def solution(n, costs):
    ans=0
    costs.sort(key=lambda x:x[2])
    s=set([costs[0][0]])
    
    # 중간에 건너 뛰는 상황 때문에 이중 반복문 필요
    while len(s) != n:
        for c in costs:
            if c[1] in s and c[0] in s:
                continue
            if c[1] in s or c[0] in s:
                ans+= c[2]
                s.add(c[1])
                s.add(c[0])
                break
    return ans