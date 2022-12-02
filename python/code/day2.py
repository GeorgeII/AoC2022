from enum import Enum
from typing import List


class Shape(Enum):
    rock = 1
    paper = 2
    scissors = 3


def _calculate_match_points(opponent_shape: Shape, my_shape: Shape) -> int:
    if opponent_shape == my_shape:
        return 3 + my_shape.value
    elif (
        my_shape == Shape.scissors
        and opponent_shape == Shape.paper
        or my_shape == Shape.paper
        and opponent_shape == Shape.rock
        or my_shape == Shape.rock
        and opponent_shape == Shape.scissors
    ):
        return 6 + my_shape.value
    else:
        return my_shape.value


def part1(lines: List[str]) -> int:
    score = 0

    for line in lines:
        shapes = line.split(" ")

        if shapes[0] == "A":
            opponent_shape = Shape.rock
        elif shapes[0] == "B":
            opponent_shape = Shape.paper
        else:
            opponent_shape = Shape.scissors

        if shapes[1] == "X":
            my_shape = Shape.rock
        elif shapes[1] == "Y":
            my_shape = Shape.paper
        else:
            my_shape = Shape.scissors

        score += _calculate_match_points(opponent_shape, my_shape)

    return score


def part2(lines: List[str]) -> int:
    pass
