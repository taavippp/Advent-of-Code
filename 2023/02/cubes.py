from pathlib import Path
import re

MAXIMUM: dict = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

regex: str = r"(\d+ (red|green|blue))"

p: Path = Path(__file__).with_name("input.txt")
lines: list[str]
with p.open() as file:
    lines = file.readlines()

part_1_answer: int = 0
part_2_answer: int = 0

for [i, line] in enumerate(lines):
    valid_game: bool = True
    rounds: list[str] = line.split(";")
    largest_amt: dict = {
        "red": 1,
        "green": 1,
        "blue": 1,
    }
    for rnd in rounds:
        for found in re.finditer(regex, rnd):
            cubes: str = found.group()
            index: int = cubes.find(" ")
            amt: int = int(cubes[0 : index])
            color: str = cubes[(index + 1) :]
            # Part 1
            if (valid_game and amt > MAXIMUM[color]):
                valid_game = False
            # Part 2
            if (amt > largest_amt[color]):
                largest_amt[color] = amt
    # Part 1
    if (valid_game):
        part_1_answer += (i + 1)
    # Part 2
    product: int = 1
    for color in largest_amt:
        product *= largest_amt[color]
    part_2_answer += product

print(part_1_answer)
print(part_2_answer)