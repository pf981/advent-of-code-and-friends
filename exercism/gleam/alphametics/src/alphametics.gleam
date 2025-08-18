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

  fn(mapping) {
    let lhs = eval(mapping, lhs_coefs)
    let rhs = eval(mapping, rhs_coefs)

    case lhs == rhs {
      True -> Ok(mapping)
      False -> Error(Nil)
    }
  }
}

fn find_valid(
  letters: List(String),
  mapping: Dict(String, Int),
  check: fn(Dict(String, Int)) -> Result(Dict(String, Int), Nil),
  non_zeroes: Set(String),
  nums_available: Set(Int),
) -> Result(Dict(String, Int), Nil) {
  case letters {
    [] -> check(mapping)
    [first, ..rest] -> {
      let possible = case set.contains(non_zeroes, first) {
        True -> set.delete(nums_available, 0)
        False -> nums_available
      }

      possible
      |> set.to_list
      |> iterator.from_list
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

  let letters =
    puzzle
    |> string.to_graphemes
    |> list.filter(string.contains("ABCDEFGHIJKLMNOPQRSTUVWXYZ", _))
    |> list.unique

  find_valid(
    letters,
    dict.new(),
    checker(puzzle),
    non_zeroes,
    set.from_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
  )
}
