

def solution(name):

    cnt=0
    ll = len(name)
    word =[]
    for i in range(ll):
        word.append('A')
    # print(word)

    pt = 0
    while ''.join(word) != name:
        lp = rp = 99
        # print(f"pt: {pt}")
        for i in range(ll):
            # print(f"word[(pt+i)%ll] : {word[(pt+i)%ll]}, name[(pt+i)%ll: {name[(pt+i)%ll]}")
            if word[(pt+i)%ll] != name[(pt+i)%ll]:
                rp = i
                # print(f"rp: {rp}")
                break
        for i in range(ll):
            # print(f"word[(pt-i)%ll] : {word[(pt-i)%ll]}, name[(pt-i)%ll: {name[(pt-i)%ll]}")
            if word[(pt-i)%ll] != name[(pt-i)%ll]:
                lp = i
                # print(f"lp: {lp}")
                break
        if rp > lp:
            pt = (pt-lp)%ll
            cnt+=lp
        else:
            pt = (pt+rp)%ll
            cnt+=rp
        # print(f"cnt: {cnt}")
        # print(f"pt : {pt}")
        
        cnt += (min((ord(word[pt])-ord(name[pt]))%26, (ord(name[pt])-ord(word[pt]))%26))
        word[pt] = name[pt]
        # print(f"word : {word}")
        # print(f"cnt: {cnt}")
        # print()
        
    return cnt