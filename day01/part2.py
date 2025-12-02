input = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
expected = 6


def main(input: str) -> int:
    lock = 50
    # number of times going through pos 0
    result = 0

    for instruction in input.splitlines():
        direction = 1 if instruction[0] == "R" else -1
        amount = int(instruction[1:])

        for _ in range(amount):
            lock += direction
            lock = lock % 100
            if lock == 0:
                result += 1

    return result


def test_part2() -> None:
    assert main(input) == expected


if __name__ == "__main__":
    with open("day01/input2.txt") as f:
        s = f.read()
        print(main(s))
