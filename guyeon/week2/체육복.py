def solution(n, lost, reserve): #1400~1410
    arr=[]
    for i in range(n+2):
        arr.append(1)
    for l in lost:
        arr[l]-=1
    for r in reserve:
        arr[r]+=1
    
    for i in range(1,n+1):
        if arr[i]==2:
            if arr[i-1]==0:
                arr[i]=1
                arr[i-1]=1
            elif arr[i+1]==0:
                arr[i]=1
                arr[i+1]=1
    cnt=0
    for i in range(1,n+1):
        if arr[i]>0: cnt+=1
    return cnt