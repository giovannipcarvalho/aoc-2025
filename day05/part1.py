INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
EXPECTED = 3


def parse(s: str) -> tuple[list[range], list[int]]:
    a, b = s.split("\n\n")
    fresh_ingredients: list[range] = []
    for r in a.splitlines():
        start, end = r.split("-", maxsplit=1)
        istart = int(start)
        iend = int(end)
        fresh_ingredients.append(range(istart, iend + 1))
    available_ingredients = [int(x) for x in b.splitlines()]
    return fresh_ingredients, available_ingredients


def is_fresh(ingredient: int, fresh_ingredients: list[range]) -> bool:
    return any(ingredient in fresh for fresh in fresh_ingredients)


def main(s: str) -> int:
    fresh_ingredients, available_ingredients = parse(s)

    result = 0
    for ingredient in available_ingredients:
        if is_fresh(ingredient, fresh_ingredients):
            result += 1
    return result


def test() -> None:
    assert main(INPUT) == EXPECTED


if __name__ == "__main__":
    with open(0) as f:
        s = f.read()
    print(main(s))
