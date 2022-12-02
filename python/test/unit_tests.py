import unittest
from code import day1, day2
from test.test_inputs import day1_inp, day2_inp


class TestStringMethods(unittest.TestCase):
    def test_day1_part1(self) -> None:
        self.assertEqual(day1.part1(day1_inp.split("\n")), 24_000)

    def test_day1_part2(self) -> None:
        self.assertEqual(day1.part2(day1_inp.split("\n")), 45_000)

    def test_day2_part1(self) -> None:
        self.assertEqual(day2.part1(day2_inp.split("\n")), 15)


if __name__ == "__main__":
    unittest.main()
