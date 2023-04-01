package days

import util.{ PartNumber, PartOne, PartTwo, Solvable }

object Day2 extends Solvable {

  def solve(partNumber: PartNumber, input: String): Int =
    partNumber match {
      case PartOne => part1(input)
      case PartTwo => part2(input)
    }

  protected def part1(input: String): Int = {
    val rounds = input.split("\n").toList

    rounds
      .map(str => str.split(" ").toList)
      .map({
        case List(other, "X") => 1 + (if (other == "A") 3 else if (other == "B") 0 else 6)
        case List(other, "Y") => 2 + (if (other == "A") 6 else if (other == "B") 3 else 0)
        case List(other, "Z") => 3 + (if (other == "A") 0 else if (other == "B") 6 else 3)
      })
      .sum
  }

  protected def part2(input: String): Int = {
    val rounds = input.split("\n").toList

    rounds
      .map(str => str.split(" ").toList)
      .map({
        case List(other, "X") => 0 + (if (other == "A") 3 else if (other == "B") 1 else 2)
        case List(other, "Y") => 3 + (if (other == "A") 1 else if (other == "B") 2 else 3)
        case List(other, "Z") => 6 + (if (other == "A") 2 else if (other == "B") 3 else 1)
      })
      .sum
  }

}
