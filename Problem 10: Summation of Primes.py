n = 2_000_000
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

print(sum(list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(is_prime))))))
