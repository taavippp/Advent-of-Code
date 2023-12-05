from pathlib import Path

# Not sure where i went wrong but it ended up saying my answer was too low
# Perhaps starting analysis from the valid gear symbols would have been wiser

p: Path = Path(__file__).with_name("input.txt")
lines: list[str]
with p.open() as file:
    lines = file.readlines()

WIDTH: int = 1
HEIGHT: int = 1

class Index2D:
    index: int = 0
    row: int = 0
    col: int = 0

    def from_index(index: int):
        result: Index2D = Index2D()
        result.index = index
        result.row = index // WIDTH
        result.col = index % WIDTH
        return result

    def from_axis(row: int, col: int):
        result: Index2D = Index2D()
        result.row = row
        result.col = col
        result.index = row * WIDTH + col
        return result

    def __add__(self, other):
        row: int = self.row + other.row
        col: int = self.col + other.col
        if (row > WIDTH or col > HEIGHT):
            return None
        result: Index2D = Index2D.from_axis(row, col)
        return result

part_1_answer: int = 0
part_2_answer: int = 0

surrounding: list[Index2D] = [
    Index2D.from_axis(-1, -1),  # topleft
    Index2D.from_axis(-1, 0),   # top
    Index2D.from_axis(-1, 1),   # topright
    Index2D.from_axis(0, 1),    # right
    Index2D.from_axis(0, -1),   # left
    Index2D.from_axis(1, -1),   # bottomleft
    Index2D.from_axis(1, 0),    # bottom
    Index2D.from_axis(1, 1),    # bottomright
]

p: Path = Path(__file__).with_name("input.txt")
lines: list[str]
with p.open() as file:
    input: str = file.read()
    HEIGHT = input.count("\n") + 1
    WIDTH = len(input) // HEIGHT

skip_chars: int = 0
found: int = 0
for [index, char] in enumerate(input):
    if (skip_chars != 0):
        skip_chars -= 1
        continue
    if (char.isdigit()):
        numstr: str = char
        i: int = 1
        while (True):
            new_char = input[index + i]
            i += 1
            if (new_char.isdigit()):
                skip_chars += 1
                numstr += new_char
            else:
                break
        number: int = int(numstr)
        added: bool = False
        for i in range(3):
            if (added):
                break
            index2d: Index2D = Index2D.from_index(index + i)
            for s in surrounding:
                if (added):
                    break
                s_index2d: Index2D = index2d + s
                if (s_index2d == None):
                    continue
                s_char: str = input[s_index2d.index]
                if (not s_char.isdigit() and s_char not in ("\n", ".")):
                    print("{0}, near {1}".format(number, s_char))
                    found += 1
                    part_1_answer += number
                    added = True
    else:
        continue

print(found)
print(part_1_answer)