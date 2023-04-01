import days.{ Day1, Day2 }
import util.{ PartOne, PartTwo }
import util.FileReader.readFile

object Main extends App {

  println(
    "Day 1, part 1 = %s".formatted(
      Day1.solve(
        partNumber = PartOne,
        input = readFile("../data/day1.txt")
      )
    )
  )
  println(
    "Day 1, part 2 = %s".formatted(
      Day1.solve(
        partNumber = PartTwo,
        input = readFile("../data/day1.txt")
      )
    )
  )

  println(
    "Day 2, part 1 = %s".formatted(
      Day2.solve(
        partNumber = PartOne,
        input = readFile("../data/day2.txt")
      )
    )
  )
  println(
    "Day 2, part 2 = %s".formatted(
      Day2.solve(
        partNumber = PartTwo,
        input = readFile("../data/day2.txt")
      )
    )
  )

}
