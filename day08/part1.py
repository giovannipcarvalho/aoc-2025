import math

import pytest

INPUT = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
EXPECTED = 40

type Vec3 = tuple[float, float, float]
type Vec = tuple[float, ...]


def dist(a: Vec, b: Vec) -> float:
    return math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b, strict=True)))


def main(s: str, n: int = 10, k: int = 3) -> int:
    points = [tuple(int(i) for i in p.split(",")) for p in s.splitlines()]

    dists = {
        (i, j): dist(points[i], points[j])
        for i in range(len(points))
        for j in range(len(points))
        if j <= i
    }

    shortest_dists = sorted((v, k) for k, v in dists.items() if v)
    circuits: list[set[int]] = []

    for _d, (i, j) in shortest_dists[:n]:
        ci = cj = None
        for idx, c in enumerate(circuits):
            if i in c and not ci:
                ci = idx
            if j in c and not cj:
                cj = idx

        if ci is None and cj is None:
            circuits.append({i, j})
        elif ci is None:
            assert cj is not None
            circuits[cj].add(i)
        elif cj is None:
            assert ci is not None
            circuits[ci].add(j)
        elif ci != cj:
            circuits[ci] |= circuits[cj]
            circuits.pop(cj)

    circuit_sizes = sorted((len(c) for c in circuits), reverse=True)
    return math.prod(circuit_sizes[:k])


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ((0, 0), (0, 0), 0),
        ((0, 0), (1, 1), 1.414213),
        ((0, 0, 0), (0, 0, 0), 0),
        ((0, 0, 0), (1, 0, 0), 1),
        ((0, 0, 0), (0, 2, 0), 2),
        ((0, 0, 0), (0, 0, 3), 3),
        ((-1, -2, -3), (1, 2, 3), math.sqrt(56)),
        ((1, 2, 3), (-1, -2, -3), math.sqrt(56)),
        ((1.5, 2.5, 3.5), (0.5, 1.5, 2.5), math.sqrt(3)),
    ],
)
def test_dist(a: Vec3, b: Vec3, expected: float) -> None:
    assert dist(a, b) == pytest.approx(expected)


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
    print(main(s, n=1000, k=3))
