import itertools
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Sequence
from typing import NamedTuple

import pytest

INPUT = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
EXPECTED = 7


class Machine(NamedTuple):
    target: str
    factors: list[str]


def parse_target(s: str) -> str:
    """Parse string into target bin string.

    > parse_target([...#.])
    '00010'
    """
    return "".join("0" if c == "." else "1" for c in s[1:-1])


def parse_factor(s: str, bits: int) -> str:
    """Parse factor string into target bin string.

    > parse_factor("(0,2,4)", bits=5)
    '10101'
    """
    bits_on = s[1:-1].split(",")
    return "".join("0" if str(b) not in bits_on else "1" for b in range(bits))


def powerset[T](it: Iterable[T]) -> Iterator[tuple[T, ...]]:
    """Return all subsets of a set of elements.

    e.g.
    > list(powerset([1,2,3]))
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    s = list(it)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


def xorduce(factors: Sequence[int]) -> int:
    t = 0
    for factor in factors:
        t ^= factor
    return t


def solve_machine(machine: Machine) -> int:
    """
    Find fewest number of presses on each button (factors) to reach the target number.
    """
    target = int(machine.target, base=2)
    factors = [int(f, base=2) for f in machine.factors]

    # fmt: off
    return min(
        len(subset)
        for subset in powerset(factors)
        if xorduce(subset) == target
    )
    # fmt: on


def main(s: str) -> int:
    machines = []
    for machine_spec in s.splitlines():
        target_str, *factors_str, _joltage = machine_spec.split()
        target = parse_target(target_str)
        factors = [parse_factor(f, bits=len(target)) for f in factors_str]
        machines.append(Machine(target=target, factors=factors))

    return sum(solve_machine(m) for m in machines)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (INPUT, EXPECTED),
    ],
)
def test(input: str, expected: int) -> None:
    assert main(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("[.##.]", "0110"),
    ],
)
def test_parse_target(input: str, expected: str) -> None:
    assert parse_target(input) == expected


@pytest.mark.parametrize(
    ("input", "bits", "expected"),
    [
        ("(3)", 4, "0001"),
        ("(1,3)", 4, "0101"),
        ("(0,2,3,4)", 5, "10111"),
    ],
)
def test_parse_factor(input: str, bits: int, expected: str) -> None:
    assert parse_factor(input, bits) == expected


@pytest.mark.parametrize(
    ("machine", "expected"),
    [
        (
            Machine(
                target="0110",
                factors=[
                    "0001",
                    "0101",
                    "0010",
                    "0011",
                    "1010",
                    "1100",
                ],
            ),
            2,
        ),
    ],
)
def test_solve_machine(machine: Machine, expected: int) -> None:
    assert solve_machine(machine) == expected


if __name__ == "__main__":
    from pathlib import Path

    s = Path(__file__).with_name("input.txt").open().read()
    print(main(s))
