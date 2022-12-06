"""
S1:
How many characters need to be processed before the first start-of-packet marker is detected? (3 chars)

S2:
How many characters need to be processed before the first start-of-message marker is detected? (14 chars)
"""

filename: str = "06/input.txt"

def solution(line: str, amt: int) -> int:
    for i in range(0, len(line) - (amt - 1)):
        chars: set[str] = set()
        for j in range(amt):
            chars.add(line[i + j])
        if (len(chars) == amt):
            return i + amt
    return -1

def main():
    with (open(filename) as file):
        line = file.readline()
        print(solution(line, 4)) #S1
        print(solution(line, 14)) #S2

if __name__ == "__main__":
    main()