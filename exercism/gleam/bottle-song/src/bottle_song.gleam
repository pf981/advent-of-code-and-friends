import gleam/list
import gleam/string

const template = "{cur} green bottle{cur_plural} hanging on the wall,
{cur} green bottle{cur_plural} hanging on the wall,
And if one green bottle should accidentally fall,
There'll be {next} green bottle{next_plural} hanging on the wall."

fn verse(bottles: Int) -> String {
  let cur =
    bottles
    |> word
    |> string.capitalise()
  let #(cur_plural, next_plural) = case bottles {
    2 -> #("s", "")
    1 -> #("", "s")
    _ -> #("s", "s")
  }
  let next = word(bottles - 1)

  template
  |> string.replace("{cur}", cur)
  |> string.replace("{next}", next)
  |> string.replace("{cur_plural}", cur_plural)
  |> string.replace("{next_plural}", next_plural)
}

fn recite_impl(start_bottles: Int, take_down: Int, acc: List(String)) -> String {
  case take_down {
    0 ->
      acc
      |> list.reverse
      |> list.intersperse("\n\n")
      |> string.concat
    _ ->
      recite_impl(start_bottles - 1, take_down - 1, [
        verse(start_bottles),
        ..acc
      ])
  }
}

pub fn recite(
  start_bottles start_bottles: Int,
  take_down take_down: Int,
) -> String {
  recite_impl(start_bottles, take_down, [])
}

fn word(num: Int) -> String {
  case num {
    10 -> "ten"
    9 -> "nine"
    8 -> "eight"
    7 -> "seven"
    6 -> "six"
    5 -> "five"
    4 -> "four"
    3 -> "three"
    2 -> "two"
    1 -> "one"
    0 -> "no"
    _ -> panic
  }
}
