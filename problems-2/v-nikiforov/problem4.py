print("Enter sequence to search for.")
str2find = input()
f = open('pi.txt', 'r')
pi = ''.join(f.read()[2:].split('\n'))
index = 0
co = 0
res = []
while (id := pi.find(str2find, index)) != -1:
    index = id + 1
    if co < 5:
        res.append(id)
    co += 1

print(f'Found {co} results.')
print(f"Positions: {' '.join(map(str, res))}")
