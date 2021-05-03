a = int(input())
result = []
for i in range(2, int(a ** (1 / 2) + 1)):
    k = 0
    while a % i == 0:
        a //= i
        k += 1
    if k != 0:
        result.append([i, k])
print(result)
