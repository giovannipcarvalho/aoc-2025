import itertools
from collections.abc import Generator

INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
EXPECTED = 13


def neighbors(grid: dict[tuple[int, int], str], x: int, y: int) -> Generator[str]:
    directions = [-1, 0, 1]
    for xd, yd in itertools.product(directions, directions):
        # self is not neighbor
        if xd == yd == 0:
            continue

        neighbor_pos = (x + xd, y + yd)
        if neighbor_pos in grid:
            yield grid[neighbor_pos]


def main(s: str) -> int:
    grid = {}
    for i, row in enumerate(s.splitlines()):
        for j, val in enumerate(row):
            grid[(i, j)] = val

    max_occupied_neighbors = 4
    result = 0
    for (x, y), val in grid.items():
        occupied_neighbors = sum(neighbor == "@" for neighbor in neighbors(grid, x, y))
        if val == "@" and occupied_neighbors < max_occupied_neighbors:
            result += 1
    return result


def test() -> None:
    assert main(INPUT) == EXPECTED


if __name__ == "__main__":
    # stdin
    with open(0) as f:
        s = f.read()
    print(main(s))
