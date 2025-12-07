from collections import deque

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
EXPECTED = 21


def main(s: str) -> int:
    grid = {
        (i, j): c for i, row in enumerate(s.splitlines()) for j, c in enumerate(row)
    }

    beams = deque([pos for pos, val in grid.items() if val == "S"])
    visited = set()
    splitters = set()

    while beams:
        n = beams.popleft()
        n = (n[0] + 1, n[1])

        if grid.get(n) == "^":
            splitters.add(n)
            n1 = (n[0], n[1] - 1)
            n2 = (n[0], n[1] + 1)
            if n1 in grid and n1 not in visited:
                beams.append(n1)
                visited.add(n1)
            if n2 in grid and n2 not in visited:
                beams.append(n2)
                visited.add(n2)
        elif n in grid:
            beams.append(n)

    return len(splitters)


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
