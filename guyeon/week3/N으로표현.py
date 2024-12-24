def solution(N, number):#1115~
    # 1 /// 5
    # 2 /// 1 10 25
    # 3 /// 6 16 31 4 20 50 125 2
    # 4 /// 
    # 하니씩 숫자 증가하면서 2로 나눈값까지 짝궁 숫자랑 사칙연산
    # 사칙 연산시 set 리스트에 있거나 0이하면 생략
    if number == N: return 1
    
    li = set([N])
    arr = [[],[N]]
    num = 1
    
    while True:
        arr.append([])
        num+=1
        for n in range(1, num//2+1):
            st = ""
            for i in range(num):
                st = st+str(N)
            st = int(st)
            if st not in li:
                li.add(st)
                arr[num].append(st)
            for a in arr[n]:
                for b in arr[num-n]:
                    if a+b not in li:
                        li.add(a+b)
                        arr[num].append(a+b)
                    if a-b>0 and a-b not in li:
                        li.add(a-b)
                        arr[num].append(a-b)
                    elif b-a>0 and b-a not in li:
                        li.add(b-a)
                        arr[num].append(b-1)
                    if a*b not in li:
                        li.add(a*b)
                        arr[num].append(a*b)
                    if a//b != 0 and a//b not in li:
                        li.add(a//b)
                        arr[num].append(a//b)
                    elif b//a != 0 and b//a not in li:
                        li.add(b//a)
                        arr[num].append(b//a)
                if number in arr[num]:
                    return num
    return -1
print(solution(5, 31168))