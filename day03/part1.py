INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""
EXPECTED = 357


def joltage(bank: str) -> int:
    m1 = max(bank[:-1])
    m2 = max(bank[bank.index(m1) + 1 :])
    return int(m1 + m2)


def main(s: str) -> int:
    result = 0
    for bank in s.splitlines():
        result += joltage(bank)
    return result


def test() -> None:
    assert main(INPUT) == EXPECTED


if __name__ == "__main__":
    from pathlib import Path

    s = Path(__file__).with_name("input.txt").open().read()
    print(main(s))
