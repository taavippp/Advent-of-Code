"""
S1: 
Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?

S2:
Find the item type that corresponds to the badges of each three-Elf group.
What is the sum of the priorities of those item types?
"""

filename: str = "03/input.txt"

def get_priority(item: str) -> int:
    if (len(item) != 1):
        return -1
    sub = 96
    if (item.isupper()):
        sub = 38
    return ord(item) - sub

def s1() -> int:
    dupe_sum = 0
    with (open(filename) as file):
        for line in file.readlines():
            line = line.strip()
            half_len = int(len(line) / 2)
            half_1 = line[0 : half_len]
            half_2 = line[half_len : (len(line))]
            for char in half_1:
                if char in half_2:
                    dupe_sum += get_priority(char)
                    break
    return dupe_sum

def s2() -> int:
    dupe_sum = 0
    with (open(filename) as file):
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            sacks = [
                lines[i],
                lines[i + 1],
                lines[i + 2],
            ]
            for char in sacks[0]:
                if char in sacks[1] and char in sacks[2]:
                    dupe_sum += get_priority(char)
                    break
    return dupe_sum

def main():
    print(s1())
    print(s2())

if __name__ == "__main__":
    main()