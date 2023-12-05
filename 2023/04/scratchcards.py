from pathlib import Path
import re

p: Path = Path(__file__).with_name("input.txt")
lines: list[str]
with p.open() as file:
    lines = file.readlines()

def part_1() -> None:
    answer: int = 0
    for line in lines:
        data: list[str] = line.split("|")
        win_list: list[int] = [int(d) for d in re.findall("\d+", data[0])]
        index: int = win_list.pop(0)
        card_list: list[int] = [int(d) for d in re.findall("\d+", data[1])]
        win: set[int] = set(win_list)
        card: set[int] = set(card_list)
        matching: set[int] = win.intersection(card)
        length: int = len(matching)
        answer += (2 ** (length - 1)) if length > 0 else 0
    return answer

def part_2() -> None:
    answer: int = 0
    card_count: dict = {}
    for i in range(len(lines)):
        card_count[i + 1] = 1
    for line in lines:
        data: list[str] = line.split("|")
        win_list: list[int] = [int(d) for d in re.findall("\d+", data[0])]
        index: int = win_list.pop(0)
        card_list: list[int] = [int(d) for d in re.findall("\d+", data[1])]
        win: set[int] = set(win_list)
        card: set[int] = set(card_list)
        matching: set[int] = win.intersection(card)
        length: int = len(matching)
        print("Card {0}, {1} instances, {2} matching".format(index, card_count[index], length))
        for i in range(length):
            card_count[index + i + 1] += card_count[index]
    for key in card_count:
        answer += card_count[key]
    return answer

print(part_1())
print(part_2())