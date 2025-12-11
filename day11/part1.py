from collections import deque

import pytest

INPUT = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
EXPECTED = 5


def main(s: str) -> int:
    graph = {}
    for line in s.splitlines():
        src, *dsts = line.replace(":", "").split()
        graph[src] = dsts

    result = 0

    todo = deque(graph["you"])

    while todo:
        n = todo.popleft()

        if n == "out":
            result += 1
            continue

        for c in graph[n]:
            todo.append(c)

    return result


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
