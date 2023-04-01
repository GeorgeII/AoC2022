package util

object FileReader {

  def readFile(path: String): String = {
    val source = scala.io.Source.fromFile(path)

    try source.mkString
    finally source.close()
  }

}
