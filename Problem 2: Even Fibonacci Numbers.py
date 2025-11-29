limit = 4_000_000

a, b = 2, 8
total = a + b

while total <= limit:
    c = 4 * b + a

    if c > limit + total:
        break

    total += c
    a, b = b, c

print(total)
