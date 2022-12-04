"""
S1: 
In how many assignment pairs does one range fully contain the other?

S2:
In how many assignment pairs do the ranges overlap?
"""

from time import perf_counter

filename: str = "04/input.txt"

def get_range(range_data: str) -> list[int]:
    [x_str, y_str] = range_data.split("-")
    [x, y] = [int(x_str), int(y_str)]
    return [x, y + 1]

def get_pair_ranges(line: str) -> list[list[int]]:
    [r1, r2] = line.strip().split(",")
    return [get_range(r1), get_range(r2)]

def flip(x: int) -> int:
    return int(not bool(x))

def s1(lines: list[str]) -> int:
    count: int = 0
    for line in lines:
        ranges = get_pair_ranges(line)
        for [index, r1] in enumerate(ranges):
            r2 = ranges[flip(index)]
            if (r1[0] in range(r2[0], r2[1] + 1) and r1[1] in range(r2[0], r2[1] + 1)):
                count += 1
                break
    return count

def s2(lines: list[str]) -> int:
    count: int = 0
    for line in lines:
        ranges = get_pair_ranges(line)
        for [index, r1] in enumerate(ranges):
            r2 = ranges[flip(index)]
            if (r2[0] in range(r1[0], r1[1] + 1) or r2[1] in range(r1[0], r1[1] + 1)):
                count += 1
                break
    return count

def main():
    with (open(filename) as file):
        lines = file.readlines()
        t1 = perf_counter()
        print(s1(lines))
        t2 = perf_counter()
        print(s2(lines))
        t3 = perf_counter()
        print("S1 took {0}, S2 took {1}".format(t2 - t1, t3 - t2))

if __name__ == "__main__":
    main()