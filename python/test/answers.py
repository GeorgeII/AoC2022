from code import day1, day2
from typing import Callable


def print_results(day: int, part1: Callable = None, part2: Callable = None):
    with open(f"../../data/day{day}.txt") as f:
        lines = [line.rstrip("\n") for line in f]

    if part1:
        print(f"Day {day}, part 1: {part1(lines)}")

    if part2:
        print(f"Day {day}, part 2: {part2(lines)}")


print_results(day=1, part1=day1.part1, part2=day1.part2)

print_results(day=2, part1=day2.part1, part2=day2.part2)
