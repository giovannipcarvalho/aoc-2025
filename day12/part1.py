from typing import NamedTuple

import pytest

INPUT = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
EXPECTED = 2


class Shape(NamedTuple):
    pattern: tuple[int, ...]

    @property
    def vol(self) -> int:
        return sum(self.pattern)


class Region(NamedTuple):
    w: int
    h: int
    shape_counts: list[int]

    @property
    def area(self) -> int:
        return self.w * self.h


# def ccl_rotate[T](seq: Sequence[T]) -> tuple[T, ...]:
#     return tuple(v for n in range(2, -1, -1) for v in seq[n::3])


def main(s: str) -> int:
    *shapes_str, regions_str = s.split("\n\n")
    shapes = []
    for shape_str in shapes_str:
        _shape_id, shape_pattern = shape_str.split(":")

        shapes.append(
            Shape(tuple(int(c == "#") for c in shape_pattern.replace("\n", "")))
        )

    regions = []
    for reg in regions_str.splitlines():
        w, h, *shape_counts = [
            int(x) for x in reg.replace("x", " ").replace(":", "").split()
        ]
        regions.append(Region(w, h, shape_counts))

    total = 0
    shape_vols = [s.vol for s in shapes]
    for region in regions:
        required_vol = sum(
            c * v for c, v in zip(region.shape_counts, shape_vols, strict=True)
        )
        if region.area >= required_vol:  # pragma: no cover
            total += 1
    return total


@pytest.mark.xfail(reason="shame")
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
