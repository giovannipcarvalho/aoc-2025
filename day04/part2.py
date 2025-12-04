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
EXPECTED = 43


type Position = tuple[int, int]
type Value = str


def neighbors(
    grid: dict[Position, Value], x: int, y: int
) -> Generator[tuple[Position, Value]]:
    directions = [-1, 0, 1]
    for xd, yd in itertools.product(directions, directions):
        # self is not neighbor
        if xd == yd == 0:
            continue

        neighbor_pos = (x + xd, y + yd)
        if neighbor_pos in grid:
            yield neighbor_pos, grid[neighbor_pos]


def removable(grid: dict[Position, Value], x: int, y: int) -> bool:
    """
    Check if position for roll is accessible for removal
    aka a) contains a roll and b) is surrounded by fewer than 4 other rolls.
    """
    max_occupied_neighbors = 4
    occupied_neighbors = sum(
        neighbor_val == "@" for _, neighbor_val in neighbors(grid, x, y)
    )
    return grid[(x, y)] == "@" and occupied_neighbors < max_occupied_neighbors


def main(s: str) -> int:
    grid = {}
    for i, row in enumerate(s.splitlines()):
        for j, val in enumerate(row):
            grid[(i, j)] = val

    result = 0

    while True:
        partial = 0
        removable_coords = []

        # count and keep track of removable rolls
        for x, y in grid:
            if removable(grid, x, y):
                partial += 1
                removable_coords.append((x, y))

        # actually remove
        for x, y in removable_coords:
            grid[(x, y)] = "."

        # tally
        result += partial

        if len(removable_coords) == 0:
            break

    return result


def test() -> None:
    assert main(INPUT) == EXPECTED


if __name__ == "__main__":
    # stdin
    with open(0) as f:
        s = f.read()
    print(main(s))
