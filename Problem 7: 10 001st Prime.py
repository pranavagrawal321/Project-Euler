"""
Rosser’s Theorem (Improved upper bound)

For every n >= 6

p(n) < n * (ln(n) + ln(ln(n)))
"""

import math


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

        p += 1

    return [i for i in range(2, n + 1) if prime[i]]


n = 10001
limit = int(n * (math.log(n) + math.log(math.log(n))))

primes = sieve(limit)

print(primes[n - 1])
