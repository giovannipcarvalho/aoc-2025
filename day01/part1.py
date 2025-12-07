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
expected = 3


def main(input: str) -> int:
    lock = 50
    # number of times landed on position 0
    result = 0
    for instruction in input.splitlines():
        direction = 1 if instruction[0] == "R" else -1
        amount = int(instruction[1:])

        lock += direction * amount
        lock = lock % 100

        if lock == 0:
            result += 1

    return result


def test_part1() -> None:
    assert main(input) == expected


if __name__ == "__main__":
    from pathlib import Path

    s = Path(__file__).with_name("input.txt").open().read()
    print(main(s))
