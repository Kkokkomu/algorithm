import itertools

round_li = list(itertools.combinations(range(6), 2))
current = [[0]*3 for _ in range(6)] 
result = [[0]*3 for _ in range(6)]

def dfs(round):
  if round == 15:
    if current == result:
      return True
    return False

  t1, t2 = round_li[round]
  # t1이 이김
  current[t1][0] += 1
  current[t2][2] += 1
  if current[t1][0] > result[t1][0] or current[t2][2] > result[t2][2]:
    r1 = False
  else:
    r1 = dfs(round+1)
  # 원복
  current[t1][0] -= 1
  current[t2][2] -= 1

  # #t2가 이김
  current[t1][2] += 1
  current[t2][0] += 1
  if current[t1][2] > result[t1][2] or current[t2][0] > result[t2][0]:
    r2 = False
  else:
    r2 = dfs(round+1)
  # 원복
  current[t1][2] -= 1
  current[t2][0] -= 1

  # 비김
  current[t1][1] += 1
  current[t2][1] += 1
  if current[t1][1] > result[t1][1] or current[t2][1] > result[t2][1]:
    r3 = False
  else:
    r3 = dfs(round+1)
  # 원복
  current[t1][1] -= 1
  current[t2][1] -= 1

  return r1 or r2 or r3
  

answer = []
for _ in range(4):
    li = list(map(int, input().split()))

    w_count = 0
    l_count = 0
    
    for i in range(0, 16, 3):
        w, d, l = li[i], li[i+1], li[i+2]
        
        if w+d+l != 5:
            answer.append(0)
            break
        
        w_count += w
        l_count += l
        k = i//3
        result[k][0], result[k][1], result[k][2] = w, d, l
    else:
        current = [[0]*3 for _ in range(6)] 
        if w_count != l_count or not dfs(0):
            answer.append(0)
            continue

        answer.append(1)

print(*answer)