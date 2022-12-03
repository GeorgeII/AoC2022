import math
import string
from typing import List


def part1(lines: List[str]) -> int:
    res = 0
    for line in lines:
        middle_idx = math.ceil(len(line) / 2)
        first, second = line[:middle_idx], line[middle_idx:]
        common: set[str] = set(first) & set(second)

        for el in common:
            res += ord(el) - 38 if el.isupper() else ord(el) - 96

    return res


def part2(lines: List[str]) -> int:
    res = 0
    for idx in range(0, len(lines), 3):
        common: set[str] = set(string.ascii_lowercase + string.ascii_uppercase)
        for elf_num in range(3):
            line = lines[idx + elf_num]
            common &= set(line)

        for el in common:
            res += ord(el) - 38 if el.isupper() else ord(el) - 96

    return res
