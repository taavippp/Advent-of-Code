"""
S1:
After the rearrangement procedure completes,
what crate ends up on top of each stack?
(crates stacked one by one)

S2:
After the rearrangement procedure completes,
what crate ends up on top of each stack?
(crates stacked multiple at once)
"""

filename: str = "05/input.txt"

def read_stack_line(line: str) -> list[str]:
    return list(filter(
        lambda x: x != "",
        # god will not forgive me
        line
            .replace("[", "")
            .replace("]", "")
            .replace("    ", " - ")
            .strip()
            .split(" ")
    ))

def read_instruction_line(line: str) -> list[int]:
    # move X from Y to Z
    instructions: list[str] = line.strip().split(" ")
    return [int(instructions[1]), int(instructions[3]) - 1, int(instructions[5]) - 1]

def solution(lines: list[str], s2: bool = False) -> str:
    stacks: list[str] = []
    reading_stacks: bool = True
    reading_instructions: bool = False
    for line in lines:
        if ("[" not in line):
            reading_stacks = False
        if (reading_stacks):
            chars: list[str] = read_stack_line(line)
            for [index, char] in enumerate(chars):
                if (len(stacks) != len(chars)):
                    stacks = [""] * len(chars)
                if (char == "-"):
                    continue
                stacks[index] += char
        if (reading_instructions):
            [amount, _from, to] = read_instruction_line(line)
            # print("MOVE {0} FROM {1} TO {2}".format(amount, stacks[_from] or "-", stacks[to] or "-"))
            chars_to_move: str = stacks[_from][0 : amount]
            stacks[_from] = stacks[_from].removeprefix(chars_to_move)
            stacks[to] = (chars_to_move[:: -1] if not s2 else chars_to_move) + stacks[to]
            # print("{0}\t{1}".format(
            #     stacks[_from] or "-",
            #     stacks[to] or "-"
            # ))
        if (line == "\n"):
            reading_instructions = True
    return "".join(list(
        map(
            lambda x: x[0],
            stacks
            )
        ))


def main():
    with (open(filename) as file):
        lines = file.readlines()
        print(solution(lines))
        print(solution(lines, True))
        # print(s2(lines))

if __name__ == "__main__":
    main()