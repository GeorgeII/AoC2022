from code import day1

with open("../../data/day1.txt") as f:
    lines = [line.rstrip("\n") for line in f]

print(day1.part1(lines))
print(day1.part2(lines))
