import gleam/dict.{type Dict}
import gleam/function
import gleam/int
import gleam/list
import gleam/result

pub type Category {
  Ones
  Twos
  Threes
  Fours
  Fives
  Sixes
  FullHouse
  FourOfAKind
  LittleStraight
  BigStraight
  Choice
  Yacht
}

fn ns(n: Int) -> fn(Dict(Int, Int)) -> Int {
  fn(counts) {
    let occurances =
      counts
      |> dict.get(n)
      |> result.unwrap(0)

    n * occurances
  }
}

fn full_house(counts: Dict(Int, Int)) -> Int {
  case dict.to_list(counts) {
    [#(a, 2), #(b, 3)] | [#(b, 3), #(a, 2)] -> a * 2 + b * 3
    _ -> 0
  }
}

fn four_of_a_kind(counts: Dict(Int, Int)) -> Int {
  case dict.to_list(counts) {
    [#(a, 4), _] | [_, #(a, 4)] | [#(a, 5)] -> a * 4
    _ -> 0
  }
}

fn little_straight(counts: Dict(Int, Int)) -> Int {
  case dict.size(counts) == 5 && !dict.has_key(counts, 6) {
    True -> 30
    False -> 0
  }
}

fn big_straight(counts: Dict(Int, Int)) -> Int {
  case dict.size(counts) == 5 && !dict.has_key(counts, 1) {
    True -> 30
    False -> 0
  }
}

fn choice(counts: Dict(Int, Int)) -> Int {
  counts
  |> dict.map_values(fn(key, count) { key * count })
  |> dict.values
  |> int.sum
}

fn yacht(counts: Dict(Int, Int)) -> Int {
  case dict.size(counts) == 1 {
    True -> 50
    False -> 0
  }
}

pub fn score(category: Category, dice: List(Int)) -> Int {
  let counts =
    dice
    |> list.group(function.identity)
    |> dict.map_values(fn(_, l) { list.length(l) })

  let f = case category {
    Ones -> ns(1)
    Twos -> ns(2)
    Threes -> ns(3)
    Fours -> ns(4)
    Fives -> ns(5)
    Sixes -> ns(6)
    FullHouse -> full_house
    FourOfAKind -> four_of_a_kind
    LittleStraight -> little_straight
    BigStraight -> big_straight
    Choice -> choice
    Yacht -> yacht
  }

  f(counts)
}
