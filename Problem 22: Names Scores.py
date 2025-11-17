letter = {chr(i): i - 64 for i in range(65, 91)}

with open("0022_names.txt") as f:
    data = sorted(eval(f.read()))

    print(
        sum([sum([letter[i] for i in word] * (data.index(word) + 1)) for word in data])
    )
