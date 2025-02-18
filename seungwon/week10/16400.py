N = int(input())
prime = set([i for i in range(2, N + 1)])
mod = 123456789

for i in range(2, int(N**0.5) + 1):
    if i not in prime:
        continue
    
    count = 2
    while (i * count <= N):
        if (i * count) in prime:
            prime.remove(i * count)
        count += 1
        
dp = [0] * (N + 1)
dp[0] = 1

for e in sorted(prime):
    for i in range(e, N + 1):
        dp[i] = (dp[i] + dp[i - e]) % mod
        
print(dp[N])