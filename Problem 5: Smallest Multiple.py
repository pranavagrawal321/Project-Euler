import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


n = list(range(1, 20))
output = n[0]

for i in n[1:]:
    output = lcm(output, i)

print(output)
