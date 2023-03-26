from code import day1, day2, day3, day4
from test.test_inputs import TEST_INPUT_BY_DAY

ROUNDS = 30
ITERATIONS = 50


def test_day1_part1(benchmark):
    benchmark.pedantic(
        target=day1.part1,
        args=(TEST_INPUT_BY_DAY.get(1).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day1_part2(benchmark):
    benchmark.pedantic(
        target=day1.part2,
        args=(TEST_INPUT_BY_DAY.get(1).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day2_part1(benchmark):
    benchmark.pedantic(
        target=day2.part1,
        args=(TEST_INPUT_BY_DAY.get(2).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day2_part2(benchmark):
    benchmark.pedantic(
        target=day2.part2,
        args=(TEST_INPUT_BY_DAY.get(2).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day3_part1(benchmark):
    benchmark.pedantic(
        target=day3.part1,
        args=(TEST_INPUT_BY_DAY.get(3).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day3_part2(benchmark):
    benchmark.pedantic(
        target=day3.part2,
        args=(TEST_INPUT_BY_DAY.get(3).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day4_part1(benchmark):
    benchmark.pedantic(
        target=day4.part1,
        args=(TEST_INPUT_BY_DAY.get(4).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )


def test_day4_part2(benchmark):
    benchmark.pedantic(
        target=day4.part2,
        args=(TEST_INPUT_BY_DAY.get(4).split("\n"),),
        iterations=ITERATIONS,
        rounds=ROUNDS,
    )
