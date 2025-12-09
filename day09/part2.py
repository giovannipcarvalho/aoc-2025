import itertools
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
EXPECTED = 24


def area(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    ds = [abs(x - y) + 1 for x, y in zip(a, b, strict=True)]
    return math.prod(ds)


def minmax(a: int, b: int) -> tuple[int, int]:
    return min(a, b), max(a, b)


def valid(
    a: tuple[int, int],
    b: tuple[int, int],
    perimeter: list[tuple[int, int]],
) -> bool:
    """
    Checks if any perimeter point is inside the rectangle defined by points a,b.
    """
    x1, x2 = minmax(a[0], b[0])
    y1, y2 = minmax(a[1], b[1])

    return not any(x1 < x < x2 and y1 < y < y2 for x, y in perimeter)


def main(s: str) -> int:
    points = [tuple(int(i) for i in p.split(",")) for p in s.splitlines()]
    perimeter: list[tuple[int, int]] = []

    for a, b in itertools.pairwise([*points, points[0]]):
        if a[0] == b[0]:
            r = range(min(a[1], b[1]) + 1, max(a[1], b[1]))
            perimeter.extend((a[0], n) for n in r)
        else:
            r = range(min(a[0], b[0]) + 1, max(a[0], b[0]))
            perimeter.extend((n, a[1]) for n in r)

    areas = [
        (area(points[i], points[j]), points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
        if valid(points[i], points[j], perimeter)  # type: ignore[arg-type]
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
