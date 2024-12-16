def solution(word):
    alpha = ["A", "E", "I", "O", "U"]
    cnt = 1
    my_dict = dict()
    tmp = []

    # 5중 반복문
    for a1 in alpha:
        if len(tmp) < 1:
            tmp.append(a1)
        else:
            tmp[0] = a1
        my_dict["".join(tmp)] = cnt
        cnt += 1
        for a2 in alpha:
            if len(tmp) < 2:
                tmp.append(a2)
            else:
                tmp[1] = a2
            my_dict["".join(tmp)] = cnt
            cnt += 1
            for a3 in alpha:
                if len(tmp) < 3:
                    tmp.append(a3)
                else:
                    tmp[2] = a3
                my_dict["".join(tmp)] = cnt
                cnt += 1
                for a4 in alpha:
                    if len(tmp) < 4:
                        tmp.append(a4)
                    else:
                        tmp[3] = a4
                    my_dict["".join(tmp)] = cnt
                    cnt += 1
                    for a5 in alpha:
                        if len(tmp) < 5:
                            tmp.append(a5)
                        else:
                            tmp[4] = a5
                        my_dict["".join(tmp)] = cnt
                        cnt += 1
                    tmp.pop()
                tmp.pop()
            tmp.pop()
        tmp.pop()

    return my_dict[word]
