from typing import NamedTuple

import pytest
import scipy

INPUT = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
EXPECTED = 33


class Machine(NamedTuple):
    joltage: tuple[int, ...]
    buttons: list[tuple[int, ...]]


def parse_ints(s: str) -> tuple[int, ...]:
    """Parse comma-separated ints into int-tuple.

    >>> parse_ints("[1,2,3]")
    (1, 2, 3)

    >>> parse_ints("{1,2,3}")
    (1, 2, 3)
    """
    return tuple(int(n) for n in s[1:-1].split(","))


def solve_machine(machine: Machine) -> int:
    matrix = [[0] * len(machine.buttons) for _ in range(len(machine.joltage))]
    for j, button in enumerate(machine.buttons):
        for affected_led in button:
            matrix[affected_led][j] = 1
    costs = [1] * len(machine.buttons)
    target = machine.joltage
    r = scipy.optimize.linprog(costs, A_eq=matrix, b_eq=target, integrality=1)
    return sum(r.x)


def main(s: str) -> int:
    machines = []
    for machine_spec in s.splitlines():
        _target_str, *buttons_str, joltage_str = machine_spec.split()
        joltage = parse_ints(joltage_str)
        buttons = [parse_ints(b) for b in buttons_str]
        machines.append(Machine(joltage=joltage, buttons=buttons))

    return int(sum(solve_machine(m) for m in machines))


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
