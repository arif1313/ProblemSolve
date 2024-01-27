while True:
    x = int(input())
    if x == 0:
        break

    sequence = " ".join(map(str, range(1, x + 1)))
    print(sequence)
