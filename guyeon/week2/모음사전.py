from itertools import product

def solution(word): #0424
    ap=['A','E','I','O','U']
    s=set()
    for i in range(1,6):
        p=product(ap,repeat=i)
        for pp in p:
            s.add(''.join(pp))
    l = sorted(list(s))
    
    for i in range(len(l)):
        if l[i] == word:
            return i+1
