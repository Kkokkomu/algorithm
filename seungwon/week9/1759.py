vowels = set(['a', 'e', 'i', 'o', 'u'])

L, C = map(int, input().split())
word = ['a'] * L
candidates = sorted(input().split())
result_candidates = []
result = []

def dfs(round, count):
    if count == L:
        result_candidates.append(''.join(word))
        return
    
    if round == C:
        return
    
    # 선택
    word[count] = candidates[round]
    dfs(round + 1, count + 1)
    
    # 미선택
    dfs(round + 1, count)
        
dfs(0, 0)

for r in result_candidates:
    rule1 = False
    rule2 = False
    count = 0
    
    for alpha in r:
        if alpha in vowels:
            rule1 = True
        else:
            count += 1
            
    if count >= 2:
        rule2 = True
    
    if rule1 and rule2:
        result.append(r)

result.sort()

for answer in result:
    print(answer)