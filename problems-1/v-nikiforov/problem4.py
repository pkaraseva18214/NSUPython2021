numbers = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]

base = """{first} green bottle{s1} hanging on the wall,
{first} green bottle{s1} hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be {second} green bottle{s2} hanging on the wall."""

for i in range(10, 0, -1):
    print(
        base.format(
            first=numbers[i].capitalize(),
            s1="s" if i != 1 else "",
            second=numbers[i - 1],
            s2="s" if i - 1 != 1 else "",
        )
    )
