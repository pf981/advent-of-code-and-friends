import gleam/dict.{type Dict}
import gleam/int
import gleam/iterator
import gleam/list
import gleam/result
import gleam/set.{type Set}
import gleam/string

fn eval(mapping: Dict(String, Int), coef_map: Dict(String, Int)) -> Int {
  dict.map_values(coef_map, fn(letter, coef) {
    coef * result.unwrap(dict.get(mapping, letter), 0)
  })
  |> dict.values
  |> int.sum
}

fn sum_dicts(dicts: List(Dict(String, Int))) -> Dict(String, Int) {
  dicts
  |> list.map(dict.to_list)
  |> list.flatten
  |> list.fold(dict.new(), fn(acc, l) {
    let #(digit, value) = l
    case dict.get(acc, digit) {
      Ok(current) -> dict.insert(acc, digit, current + value)
      Error(Nil) -> dict.insert(acc, digit, value)
    }
  })
}

fn to_coefs(letters: String) -> Dict(String, Int) {
  letters
  |> string.to_graphemes
  |> list.reverse
  |> list.index_map(fn(letter, i) {
    let tens_coef =
      list.repeat(10, i)
      |> list.fold(1, fn(acc, el) { acc * el })
    dict.from_list([#(letter, tens_coef)])
  })
  |> sum_dicts
}

fn checker(
  puzzle: String,
) -> fn(Dict(String, Int)) -> Result(Dict(String, Int), Nil) {
  let assert Ok(#(lhs, rhs)) = string.split_once(puzzle, " == ")

  let lhs_coefs =
    string.split(lhs, " + ")
    |> list.map(to_coefs)
    |> sum_dicts
  let rhs_coefs = to_coefs(rhs)

  io.debug([lhs_coefs, rhs_coefs])

  fn(mapping) {
    let lhs = eval(mapping, lhs_coefs)
    let rhs = eval(mapping, rhs_coefs)

    case lhs == rhs {
      True -> Ok(mapping)
      False -> Error(Nil)
    }
  }
}

// fn is_valid(
//   mapping: Dict(String, Int),
//   puzzle: String,
// ) -> Result(Dict(String, Int), Nil) {
//   let equation =
//     mapping
//     |> dict.to_list
//     |> list.fold(puzzle, fn(acc, pair) {
//       string.replace(acc, pair.0, int.to_string(pair.1))
//     })

//   let assert Ok(#(lhs, rhs)) = string.split_once(equation, " == ")
//   let lhs =
//     lhs
//     |> string.split(" + ")
//     |> list.map(int.base_parse(_, 10))
//     |> result.values
//     |> int.sum

//   let rhs =
//     rhs
//     |> int.base_parse(10)
//     |> result.unwrap(0)

//   case lhs == rhs {
//     True -> Ok(mapping)
//     False -> Error(Nil)
//   }
// }

fn find_valid(
  letters: List(String),
  mapping: Dict(String, Int),
  check: fn(Dict(String, Int)) -> Result(Dict(String, Int), Nil),
  non_zeroes: Set(String),
  nums_available: Set(Int),
) -> Result(Dict(String, Int), Nil) {
  // io.debug(mapping)
  case letters {
    [] -> check(mapping)
    [first, ..rest] -> {
      let possible = case set.contains(non_zeroes, first) {
        True -> set.delete(nums_available, 0)
        False -> nums_available
      }
      nums_available
      |> set.to_list
      |> iterator.from_list
      |> iterator.filter(fn(el) {
        !{ set.contains(non_zeroes, first) && el == 0 }
        && !list.contains(dict.values(mapping), el)
      })
      |> iterator.map(fn(el) {
        find_valid(
          rest,
          dict.insert(mapping, first, el),
          check,
          non_zeroes,
          set.delete(nums_available, el),
        )
      })
      |> iterator.filter(result.is_ok)
      |> iterator.first
      |> result.flatten
    }
  }
}

pub fn solve(puzzle: String) -> Result(Dict(String, Int), Nil) {
  let non_zeroes =
    puzzle
    |> string.split(" ")
    |> list.map(string.slice(_, 0, 1))
    |> set.from_list
    |> io.debug
  puzzle
  |> string.to_graphemes
  |> list.filter(string.contains("ABCDEFGHIJKLMNOPQRSTUVWXYZ", _))
  |> list.unique
  |> io.debug
  // |> fn(_) { panic }
  // |> find_valid(dict.new(), is_valid(_, puzzle))
  |> find_valid(
    dict.new(),
    checker(puzzle),
    non_zeroes,
    set.from_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
  )
}

import gleam/io

pub fn main() {
  // solve("I + BB == ILL")
  // solve("A == B")
  // solve("A + A + A + A + A + A + A + A + A + A + A + B == BCC")
  // solve("AND + A + STRONG + OFFENSE + AS + A + GOOD == DEFENSE")
  solve(
    "THIS + A + FIRE + THEREFORE + FOR + ALL + HISTORIES + I + TELL + A + TALE + THAT + FALSIFIES + ITS + TITLE + TIS + A + LIE + THE + TALE + OF + THE + LAST + FIRE + HORSES + LATE + AFTER + THE + FIRST + FATHERS + FORESEE + THE + HORRORS + THE + LAST + FREE + TROLL + TERRIFIES + THE + HORSES + OF + FIRE + THE + TROLL + RESTS + AT + THE + HOLE + OF + LOSSES + IT + IS + THERE + THAT + SHE + STORES + ROLES + OF + LEATHERS + AFTER + SHE + SATISFIES + HER + HATE + OFF + THOSE + FEARS + A + TASTE + RISES + AS + SHE + HEARS + THE + LEAST + FAR + HORSE + THOSE + FAST + HORSES + THAT + FIRST + HEAR + THE + TROLL + FLEE + OFF + TO + THE + FOREST + THE + HORSES + THAT + ALERTS + RAISE + THE + STARES + OF + THE + OTHERS + AS + THE + TROLL + ASSAILS + AT + THE + TOTAL + SHIFT + HER + TEETH + TEAR + HOOF + OFF + TORSO + AS + THE + LAST + HORSE + FORFEITS + ITS + LIFE + THE + FIRST + FATHERS + HEAR + OF + THE + HORRORS + THEIR + FEARS + THAT + THE + FIRES + FOR + THEIR + FEASTS + ARREST + AS + THE + FIRST + FATHERS + RESETTLE + THE + LAST + OF + THE + FIRE + HORSES + THE + LAST + TROLL + HARASSES + THE + FOREST + HEART + FREE + AT + LAST + OF + THE + LAST + TROLL + ALL + OFFER + THEIR + FIRE + HEAT + TO + THE + ASSISTERS + FAR + OFF + THE + TROLL + FASTS + ITS + LIFE + SHORTER + AS + STARS + RISE + THE + HORSES + REST + SAFE + AFTER + ALL + SHARE + HOT + FISH + AS + THEIR + AFFILIATES + TAILOR + A + ROOFS + FOR + THEIR + SAFE == FORTRESSES",
  )
  |> io.debug
}
