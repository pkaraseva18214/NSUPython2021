numbers = [int(i) for i in input().split()]
a, b = map(int, input().split())
result = [a if i < a else b if i > b else i for i in numbers]
print(result)
