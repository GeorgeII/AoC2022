package days

import util.{ PartNumber, PartOne, PartTwo, Solvable }

object Day1 extends Solvable {

  def solve(partNumber: PartNumber, input: String): Int =
    partNumber match {
      case PartOne => part1(input)
      case PartTwo => part2(input)
    }

  protected def part1(input: String): Int = {
    val byElf = input.split("\n\n").toList

    byElf
      .map(cargos => cargos.split("\n").map(_.toInt).sum)
      .max
  }

  protected def part2(input: String): Int = {
    val byElf = input.split("\n\n").toList

    byElf
      .map(cargos => cargos.split("\n").map(_.toInt).sum)
      .sorted(Ordering[Int].reverse)
      .take(3)
      .sum
  }

}
