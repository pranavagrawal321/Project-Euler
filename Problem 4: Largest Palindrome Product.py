output = -float("inf")

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        p = i * j

        if p < output:
            break

        if str(p) == str(p)[::-1]:
            output = p
            break

print(output)
