import pytest

INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
EXPECTED = 14


def parse(s: str) -> list[tuple[int, int]]:
    a, _ = s.split("\n\n")
    fresh_ingredients = []
    for r in a.splitlines():
        start, end = r.split("-", maxsplit=1)
        istart = int(start)
        iend = int(end)
        fresh_ingredients.append((istart, iend))
    return fresh_ingredients


def overlaps(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] <= b[0] <= a[1]


def squash_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    new_ranges = []

    new_ranges.append(ranges[0])
    for x in ranges[1:]:
        if overlaps(new_ranges[-1], x):
            new_ranges[-1] = new_ranges[-1][0], max(x[1], new_ranges[-1][1])
        else:
            new_ranges.append(x)

    return new_ranges


def main(s: str) -> int:
    fresh_ingredients = sorted(parse(s))
    fresh_ingredients = squash_ranges(fresh_ingredients)

    result = sum(len(range(r[0], r[1] + 1)) for r in fresh_ingredients)
    return result


def test() -> None:
    assert main(INPUT) == EXPECTED


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ((3, 5), (10, 14), False),
        ((10, 14), (12, 18), True),
        ((10, 18), (16, 20), True),
        ((6, 6), (7, 7), False),
        ((545667226602897, 551595722084447), (551595722084447, 551595722084447), True),
        ((1, 10), (3, 5), True),
    ],
)
def test_overlaps(a: tuple[int, int], b: tuple[int, int], expected: bool) -> None:
    assert overlaps(a, b) == expected


if __name__ == "__main__":
    from pathlib import Path

    s = Path(__file__).with_name("input.txt").open().read()
    print(main(s))
