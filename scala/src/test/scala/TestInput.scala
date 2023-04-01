object TestInput {

  def getDayN(dayNumber: Int): String =
    dayNumber match {

      case 1 => "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"

      case 2 => "A Y\nB X\nC Z"

    }

}
