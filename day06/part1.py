import pytest

INPUT = """\
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
EXPECTED = 4277556


def main(s: str) -> int:
    nums = [int(c) for line in s.splitlines()[:-1] for c in line.split()]
    ops = s.splitlines()[-1].split()
    width = len(ops)

    result = [0 for _ in range(width)]

    for i in range(width):
        for num in nums[i::width]:
            match ops[i]:
                case "+":
                    result[i] += num
                case "*":
                    if result[i] == 0:
                        result[i] = num
                    else:
                        result[i] *= num
                case _:
                    raise ValueError("unknown op")

    return sum(result)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (INPUT, EXPECTED),
    ],
)
def test(input: str, expected: int) -> None:
    assert main(input) == expected


if __name__ == "__main__":
    with open("day06/input.txt") as f:
        s = f.read()
    print(main(s))
