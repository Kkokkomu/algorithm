def solution(routes):#10:50
    answer = 0
    routes.sort(key=lambda x:x[1])
    print(routes)
    
    cp=-33333
    for r in routes:
        if cp < r[0]:
            answer+=1
            cp=r[1]
    
    return answer