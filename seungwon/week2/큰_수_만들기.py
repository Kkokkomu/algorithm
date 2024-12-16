def solution(number, k):
    # number를 순회하며 숫자들을 stack에 삽입
    stack = [number[0]]

    # stack의 앞쪽에 있는 원소들이 가장 큰 수가 되도록
    # number 숫자들을 순회하며
    # stack의 마지막 숫자가 현재 숫자보다 작은 경우
    # stack의 마지막 숫자를 제거하고 k를 1 감소
    # k가 0이 될때까지 반복
    for n in number[1:]:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1

        stack.append(n)

    # k가 남은 경우 stack의 뒷부분을 제거
    while k:
        stack.pop()
        k -= 1

    return "".join(stack)
