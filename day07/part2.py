from functools import cache
from typing import Any

import pytest

INPUT = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
EXPECTED = 40


class HDict(dict[Any, Any]):
    def __hash__(self) -> int:  # type: ignore[override]
        return hash(frozenset(self.items()))


@cache
def solve(grid: HDict, pos: tuple[int, int], total: int) -> int:
    if pos not in grid:
        return total + 1
    if grid[pos] == "^":
        a = solve(grid, (pos[0], pos[1] - 1), total)
        b = solve(grid, (pos[0], pos[1] + 1), total)
        return a + b
    else:
        return solve(grid, (pos[0] + 1, pos[1]), total)


def main(s: str) -> int:
    grid = {}

    for i, row in enumerate(s.splitlines()):
        for j, c in enumerate(row):
            grid[(i, j)] = c
            if c == "S":
                start = (i, j)

    return solve(HDict(grid), start, 0)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (INPUT, EXPECTED),
    ],
)
def test(input: str, expected: int) -> None:
    assert main(input) == expected


if __name__ == "__main__":
    with open("day07/input.txt") as f:
        s = f.read()
    print(main(s))
