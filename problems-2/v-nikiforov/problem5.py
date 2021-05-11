n = int(input())

primes = [
    i for i in range(2, n + 1) if next((None for j in range(2, i) if i % j == 0), -1) == -1
]
print(primes)
