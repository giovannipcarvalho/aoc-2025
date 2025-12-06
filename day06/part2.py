import math

import pytest

INPUT = "\
123 328  51 64 \n\
 45 64  387 23 \n\
  6 98  215 314\n\
*   +   *   +  \n\
"
EXPECTED = 3263827


def parse(col: str) -> tuple[int | None, str | None]:
    try:
        num = int("".join(col[:-1]))
    except ValueError:
        return None, None
    op = col[-1] if col[-1] != " " else None
    return num, op


def main(s: str) -> int:
    lines = s.splitlines()

    result = 0
    partial = []

    for col in zip(*(line[::-1] for line in lines), strict=True):
        num, op = parse(col)  # type: ignore[arg-type]

        if num is None:
            continue

        partial.append(num)

        match op:
            case "*":
                result += math.prod(partial)
                partial = []
            case "+":
                result += sum(partial)
                partial = []
            case _:
                pass
    return result


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
