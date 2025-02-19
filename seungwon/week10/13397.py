N, M = map(int, input().split())
li = list(map(int, input().split()))
left = 0
right = max(li) - min(li)
answer = 99999

while left <= right:
    mid = (left + right) // 2
    
    min_val = 99999
    max_val = -99999
    cnt = 1
    
    for i in range(len(li)):
        min_val = min(min_val, li[i])
        max_val = max(max_val, li[i])
        
        if max_val - min_val > mid:
            cnt += 1
            min_val = li[i]
            max_val = li[i]
    
    if cnt <= M:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
        
print(answer)