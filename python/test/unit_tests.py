import unittest
from code import day1, day2, day3, day4
from test.test_inputs import TEST_INPUT_BY_DAY


class TestStringMethods(unittest.TestCase):
    def test_day1_part1(self) -> None:
        self.assertEqual(24_000, day1.part1(TEST_INPUT_BY_DAY.get(1).split("\n")))

    def test_day1_part2(self) -> None:
        self.assertEqual(45_000, day1.part2(TEST_INPUT_BY_DAY.get(1).split("\n")))

    def test_day2_part1(self) -> None:
        self.assertEqual(15, day2.part1(TEST_INPUT_BY_DAY.get(2).split("\n")))

    def test_day2_part2(self) -> None:
        self.assertEqual(12, day2.part2(TEST_INPUT_BY_DAY.get(2).split("\n")))

    def test_day3_part1(self) -> None:
        self.assertEqual(157, day3.part1(TEST_INPUT_BY_DAY.get(3).split("\n")))

    def test_day3_part2(self) -> None:
        self.assertEqual(70, day3.part2(TEST_INPUT_BY_DAY.get(3).split("\n")))

    def test_day4_part1(self) -> None:
        self.assertEqual(2, day4.part1(TEST_INPUT_BY_DAY.get(4).split("\n")))

    def test_day4_part2(self) -> None:
        self.assertEqual(4, day4.part2(TEST_INPUT_BY_DAY.get(4).split("\n")))


if __name__ == "__main__":
    unittest.main()
