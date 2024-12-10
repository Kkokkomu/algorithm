from collections import Counter


def solution(numbers):
    answer = 0
    # 소수 리스트
    pn_list = []

    # 에라토스테네스의 체
    prime_number = [True] * 10 ** len(numbers)
    for i in range(2, len(prime_number)):
        if prime_number[i] == False:
            continue

        pn_list.append(i)

        count = 2
        while i * count < len(prime_number):
            prime_number[i * count] = False
            count += 1

    # 소수 리스트를 순회하며 주어진 numbers로
    # 해당 소수를 만들 수 있는지 확인
    n_counter = Counter(numbers)
    for pn in pn_list:
        temp = n_counter.copy()
        # for 문에서 break가 안 걸리면 소수를 만들 수 있으므로 answer 1 증가시킴
        for n in str(pn):
            if temp.get(n) and temp[n] > 0:
                temp[n] -= 1
            else:
                break
        else:
            answer += 1

    return answer
