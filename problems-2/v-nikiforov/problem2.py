words = {}
with open("problem2.txt", "r") as f:
    for line in f.readlines():
        word, definition = line.strip().split(" - ")
        words[word] = definition.split(", ")

inv_map = {w: k for k, wds in words.items() for w in wds}
for k, v in sorted(inv_map.items()):
    print(f"{k} - {v}")
