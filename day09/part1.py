import math

import pytest

INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
EXPECTED = 50


def area(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    ds = [abs(x - y) + 1 for x, y in zip(a, b, strict=True)]
    return math.prod(ds)


def main(s: str) -> int:
    points = [tuple(int(i) for i in p.split(",")) for p in s.splitlines()]

    areas = [
        (area(points[i], points[j]), points[i], points[j])
        for i in range(len(points))
        for j in range(len(points))
        if j <= i
    ]
    max_area, _p1, _p2 = max(areas)
    return max_area


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (INPUT, EXPECTED),
    ],
)
def test(input: str, expected: int) -> None:
    assert main(input) == expected


if __name__ == "__main__":
    from pathlib import Path

    s = Path(__file__).with_name("input.txt").open().read()
    print(main(s))
