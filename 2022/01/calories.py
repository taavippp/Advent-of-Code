"""
S1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
S2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

filename: str = "01/input.txt"

def get_max_calories() -> list[int]:
    with (open(filename) as file):
        top1: int = 3
        top2: int = 2
        top3: int = 1
        sum: int = 0
        for line in file.readlines():
            if (line == "\n"):
                if sum > top1:
                    top3 = top2
                    top2 = top1
                    top1 = sum
                elif sum > top2:
                    top3 = top2
                    top2 = sum
                elif sum > top3:
                    top3 = sum
                sum = 0
                continue
            sum += int(line)
    return [top1, top2, top3]

def main():
    max: list[int] = get_max_calories()
    print("S1:", max[0])
    print("S2:", sum(max))

if __name__ == "__main__":
    main()