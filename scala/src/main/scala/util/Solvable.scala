package util

trait Solvable {

  def solve(partNumber: PartNumber, input: String): Int

  protected def part1(input: String): Int

  protected def part2(input: String): Int

}
