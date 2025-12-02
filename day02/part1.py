input = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"""

expected = 1227775554


def test() -> None:
    assert main(input) == expected


def valid(id: int) -> bool:
    id_str = str(id)
    mid = len(id_str) // 2
    return id_str[:mid] != id_str[mid:]


def main(s: str) -> int:
    ranges = s.split(",")
    result = 0
    for r in ranges:
        start, end = r.split("-")
        for num in range(int(start), int(end) + 1):
            if not valid(num):
                result += num

    return result


if __name__ == "__main__":
    with open("day02/input1.txt") as f:
        s = f.read()
    print(main(s))
