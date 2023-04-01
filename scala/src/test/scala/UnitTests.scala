import days.{ Day1, Day2 }
import org.scalatest.flatspec.AnyFlatSpec
import util.{ PartOne, PartTwo }

class UnitTests extends AnyFlatSpec {

  "Day1 part1" should "be 24000" in {
    val res = Day1.solve(
      partNumber = PartOne,
      input = TestInput.getDayN(1)
    )
    assert(res == 24000)
  }

  "Day1 part2" should "be 45000" in {
    val res = Day1.solve(
      partNumber = PartTwo,
      input = TestInput.getDayN(1)
    )
    assert(res == 45000)
  }

  "Day2 part1" should "be 15" in {
    val res = Day2.solve(
      partNumber = PartOne,
      input = TestInput.getDayN(2)
    )
    assert(res == 15)
  }

  "Day2 part2" should "be 12" in {
    val res = Day2.solve(
      partNumber = PartTwo,
      input = TestInput.getDayN(2)
    )
    assert(res == 12)
  }

}
