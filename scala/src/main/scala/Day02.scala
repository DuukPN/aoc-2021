import java.io.File
import scala.io.Source

object Day02 extends App {
  val in = Source.fromFile(new File("../input/day02.txt")).getLines().toList
  println(part1(in))
  println(part2(in))

  def part1(list: List[String]): Int = {
    list.map(s => if (s.startsWith("forward")) s.split(' ')(1).toInt else 0).sum *
      list.map(s => if (!s.startsWith("forward"))
        if (s.startsWith("down")) s.split(' ')(1).toInt else -s.split(' ')(1).toInt else 0).sum
  }

  def part2(list: List[String]): Int = {
    list.foldLeft((0, 0, 0))((acc, s) => s match {
      case s if s.split(' ')(0) == "forward" => (acc._1 + s.split(' ')(1).toInt, acc._2 + s.split(' ')(1).toInt * acc._3, acc._3)
      case s if s.split(' ')(0) == "down" => (acc._1, acc._2, acc._3 + s.split(' ')(1).toInt)
      case s if s.split(' ')(0) == "up" => (acc._1, acc._2, acc._3 - s.split(' ')(1).toInt)
    })._1 *
      list.foldLeft((0, 0, 0))((acc, s) => s match {
        case s if s.split(' ')(0) == "forward" => (acc._1 + s.split(' ')(1).toInt, acc._2 + s.split(' ')(1).toInt * acc._3, acc._3)
        case s if s.split(' ')(0) == "down" => (acc._1, acc._2, acc._3 + s.split(' ')(1).toInt)
        case s if s.split(' ')(0) == "up" => (acc._1, acc._2, acc._3 - s.split(' ')(1).toInt)
      })._2
  }
}
