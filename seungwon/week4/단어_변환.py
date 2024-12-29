from collections import deque


def solution(begin, target, words):
    # 사용가능한 단어들의 집합
    words_set = set(words)
    words_set.add(begin)
    # 그래프 생성
    # 각 단어에서 한 글자만 바꿔서 만들 수 있는 단어들을 그래프로 표현
    graph = {w: set() for w in words_set}
    # 방문 여부
    is_visited = {w: False for w in words_set}

    # target이 words에 없으면 변환 불가능
    if target not in words:
        return 0

    # 그래프 생성
    # 한 글자만 바꿔서 만들 수 있는 단어들을 그래프로 표현
    for word in words_set:
        # 단어의 각 글자를 바꿔가면서 그래프 생성
        # temp_word가 words_set에 있으면 인접 세트에 추가
        for i in range(len(word)):
            temp = [w for w in word]
            for j in range(26):
                temp[i] = chr(ord("a") + j)
                temp_word = "".join(temp)
                if temp_word != word and temp_word in words_set:
                    graph[word].add(temp_word)
                    graph[temp_word].add(word)

    # BFS를 이용한 최단 경로 탐색
    # 시작 단어부터 target 단어까지의 최단 경로를 찾는다
    # (cost, current_word)의 형태로 큐에 저장
    dq = deque([(0, begin)])

    # BFS
    while dq:
        cost, current_word = dq.popleft()
        if is_visited[current_word]:
            continue
        is_visited[current_word] = True

        # target 단어를 찾으면 cost 반환
        if current_word == target:
            return cost

        for next_word in graph[current_word]:
            dq.append((cost + 1, next_word))

    # target 단어를 찾지 못하면 0 반환
    return 0
