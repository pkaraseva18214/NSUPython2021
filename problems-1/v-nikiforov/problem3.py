def collats(n):
    yield str(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        yield str(n)


print(" -> ".join(collats(int(input()))))
