import heapq
from typing import List


def part1(lines: List[str]) -> int:
    max_calories = 0

    current_elf_calories = 0
    for line in lines + [""]:
        if not line:
            if current_elf_calories > max_calories:
                max_calories = current_elf_calories
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

    return max_calories


def part2(lines: List[str]) -> int:
    k = 3
    heap = []
    heapq.heappush(heap, 0)

    current_elf_calories = 0
    for line in lines + [""]:
        if not line:
            if current_elf_calories > heap[0]:
                if len(heap) == k:
                    heapq.heappop(heap)
                heapq.heappush(heap, current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

    res = 0
    while heap:
        res += heapq.heappop(heap)

    return res
