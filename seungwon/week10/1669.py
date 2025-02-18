X, Y = map(int, input().split())
gap = Y - X
count = 0
num = 1
sum_val = 0
is_odd = False

while sum_val < gap:
    if is_odd:
        sum_val += num
        num += 1
        is_odd = False
    else:
        sum_val += num
        is_odd = True
    count += 1

print(count)