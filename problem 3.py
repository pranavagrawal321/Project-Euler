n = 600851475143

ans = 1
i = 2
while i * i <= n:
    if n % i == 0:
        n //= i
        ans = max(ans, i)
    else:
        i += 1

if n > 1:
    ans = max(ans, n)

print(ans)
