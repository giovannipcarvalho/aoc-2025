INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""
EXPECTED = 3121910778619


def argmax(s: str) -> int:
    return max(range(len(s)), key=lambda x: s[x])


def joltage(bank: str, max_batteries: int = 12) -> int:
    batteries = []

    i = 0
    j = max_batteries - 1
    while i < len(bank) and j >= 0:
        sl = slice(i, -j if j else None)

        m = argmax(bank[sl])
        batteries.append(bank[sl][m])

        i += m + 1
        j -= 1

    return int("".join(batteries))


def main(s: str) -> int:
    result = 0
    for bank in s.splitlines():
        result += joltage(bank)
    return result


def test() -> None:
    assert main(INPUT) == EXPECTED


if __name__ == "__main__":
    with open("day03/input2.txt") as f:
        s = f.read()
    print(main(s))
