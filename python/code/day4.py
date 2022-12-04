from typing import List


def part1(lines: List[str]) -> int:
    count = 0

    for line in lines:
        sections = line.split(",")
        first_elf = [int(number) for number in sections[0].split("-")]
        second_elf = [int(number) for number in sections[1].split("-")]

        if (first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]) or (
            first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]
        ):
            count += 1

    return count


def part2(lines: List[str]) -> int:
    count = 0

    for line in lines:
        sections = line.split(",")
        first_elf = [int(number) for number in sections[0].split("-")]
        second_elf = [int(number) for number in sections[1].split("-")]

        if (
            second_elf[0] <= first_elf[0] <= second_elf[1]
            or second_elf[0] <= first_elf[1] <= second_elf[1]
            or first_elf[0] <= second_elf[0] <= first_elf[1]
            or first_elf[0] <= second_elf[1] <= first_elf[1]
        ):
            count += 1

    return count
