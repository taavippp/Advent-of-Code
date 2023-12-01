from pathlib import Path
import re

digits: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

# Part 1
# regex: str = r"\d"
# Part 2
regex: str = r"(?=(\d|{0}))".format("|".join(digits))

p: Path = Path(__file__).with_name("input.txt")
lines: list[str]
with p.open() as file:
    lines = file.readlines()
answer: int = 0
for line in lines:
    found: list[str] = re.findall(regex, line)
    for [index, item] in enumerate(found):
        if (not item.isdigit()):
            found[index] = digits.index(item) + 1 # Zero is missing from the list so +1
    combined: int = int("{0}{1}".format(found[0], found[len(found) - 1]))
    answer += combined
print("Answer: {0}".format(answer))