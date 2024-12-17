def solution(people, limit): #0400
    people.sort(reverse=True)
    
    cnt = 0
    for p in people:
        tmp = p
        
        if tmp + people[-1] <= limit:
            tmp += people.pop()
        
        cnt+=1
    
    return cnt