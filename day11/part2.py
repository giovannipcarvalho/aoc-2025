import functools

import pytest

INPUT = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
EXPECTED = 2


def main(s: str) -> int:
    graph = {}
    for line in s.splitlines():
        src, *dsts = line.replace(":", "").split()
        graph[src] = dsts

    relevant = {"dac", "fft"}

    @functools.cache
    def dfs(n: str, relevant_found: frozenset[str]) -> int:
        if n == "out":
            return relevant_found == relevant

        total = 0
        for c in graph[n]:
            new_rel = relevant_found | {c} & relevant
            total += dfs(c, new_rel)
        return total

    return dfs("svr", frozenset())


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
