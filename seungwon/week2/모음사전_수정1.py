count = 1
alpha = ["A", "E", "I", "O", "U"]
my_dict = dict()
tmp = []


# 재귀로 완전탐색
def dfs():
    global count

    if len(tmp) == 5:
        return

    for a in alpha:
        tmp.append(a)
        my_dict["".join(tmp)] = count
        count += 1
        dfs()
        tmp.pop()


def solution(word):
    dfs()

    return my_dict[word]
