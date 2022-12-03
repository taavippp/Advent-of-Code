"""
A X 1p - rock
B Y 2p - paper
C Z 3p - scissors
X 0p - LOSE
Y 3p - DRAW
Z 6p - WIN
"""

filename: str = "02/input.txt"
beats: list[int] = [
    2,
    0,
    1
]

def rps(opponent: int, player: int) -> int:
    if (opponent == player):
        return 3
    if (beats[player] == opponent):
        return 6
    return 0

def s1() -> int:
    points: int = 0
    with (open(filename) as file):
        for line in file.readlines():
            #Example line: A X\n
            data: list[str] = line.strip().split(" ")
            opponent: int = ord(data[0]) - 65
            player: int = ord(data[1]) - 88
            points += (player + 1) + rps(opponent, player)
    return points

def s2() -> int:
    points: int = 0
    with (open(filename) as file):
        for line in file.readlines():
            #Example line: A X\n
            data: list[str] = line.strip().split(" ")
            opponent: int = ord(data[0]) - 65
            outcome: int = ord(data[1]) - 88
            player: int = 0
            match outcome:
                case 0:
                    player = opponent - 1
                    if (player < 0):
                        player = 2
                case 1:
                    player = opponent
                case 2:
                    player = opponent + 1
                    if (player > 2):
                        player = 0
            points += (outcome * 3) + (player + 1)
    return points

def main():
    print(s1())
    print(s2())

if __name__ == "__main__":
    main()