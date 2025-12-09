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


type Point = tuple[int, int]
type Segment = tuple[Point, Point]


def minmax(a: int, b: int) -> Point:
    return min(a, b), max(a, b)


def valid(
    a: Point,
    b: Point,
    perimeter_segments: list[Segment],
) -> bool:
    x1, x2 = minmax(a[0], b[0])
    y1, y2 = minmax(a[1], b[1])

    for (ax, ay), (bx, by) in perimeter_segments:
        # fully inside
        if x1 < ax < x2 and x1 < bx < x2 and y1 < ay < y2 and y1 < by < y2:
            return False  # pragma: no cover

        # vertical segment
        if ax == bx and x1 < ax < x2 and by > y1 and ay < y2:
            return False

        # horizontal segment
        if ay == by and y1 < ay < y2 and bx > x1 and ax < x2:
            return False

    return True


def main(s: str) -> int:
    points = [tuple(int(i) for i in p.split(",")) for p in s.splitlines()]
    perimeter_segments: list[Segment] = []

    for a, b in itertools.pairwise([*points, points[0]]):
        x1, x2 = minmax(a[0], b[0])
        y1, y2 = minmax(a[1], b[1])
        perimeter_segments.append(((x1, y1), (x2, y2)))

    areas = [
        (area(points[i], points[j]), points[i], points[j])
        for i in range(len(points))
        for j in range(i + 1, len(points))
        if valid(points[i], points[j], perimeter_segments)  # type: ignore[arg-type]
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
