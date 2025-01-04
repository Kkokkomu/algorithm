from collections import deque

def solution(numbers, target):#1739~1812
    numbers.sort(reverse=True)
    
    num = sum(numbers)
    li = deque([num]) # bfs 큐 초기화
    
    for n in numbers: # 각 숫자를 하나씩 돌면서 남아있는 값에 더하거나 뺌. 때문에 그래프의 깊이는 2^len(number)가 될 것
        ll = len(li)
        for i in range(ll): # 큐에 남아있는 수들의 갯수만큼 순회
            edge = li.popleft() # 남아있는 수를 하나 빼서
            li.append(edge) # 하나는 더하는 것(그냥 그대로 추가)
            if edge - n*2 >= target: # 하나는 빼는 것. 이때 만약 타겟보다 값이 적다면 이후에 깊어져도 값이 커지지는 않으므로 큐에 추가하지 않음
                li.append(edge - n*2)
    return li.count(target) # 마지막 리프노드들에서 target이 얼마나 만들어 졌는지  count
