#240~300
import sys

N = int(sys.stdin.readline())

high = [9*(10**(i-1))*i for i in range(9)]

lenN = len(str(N))
if lenN == 1:
    print(N)
    exit()

nine = "9" * (lenN-1)

res = sum(high[:lenN])
res += (N-int(nine))*lenN
print(int(res))