from itertools import permutations
def sosu(n):
    if n==1 or n==0: return False
    for i in range(2,n):
        if n%i == 0: return False
    return True
    
    
def solution(numbers):# 0335~0351
    m=set()
    cnt=0
    
    for i in range(1,len(numbers)+1):
        p=permutations(numbers,i)
        for pp in p:
            m.add(int(''.join(pp)))
        
    for mm in m:
        if sosu(mm) == True: 
            cnt+=1
            
    return cnt