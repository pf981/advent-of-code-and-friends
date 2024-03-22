import gleam/bool
import gleam/iterator
import gleam/list
import gleam/result
import gleam/string

pub type Error {
  KeyNotCoprime(Int, Int)
}

fn mod(dividend: Int, by divisor: Int) -> Int {
  case dividend % divisor {
    num if num >= 0 -> num
    num -> num + divisor
  }
}

fn gcd(a: Int, b: Int) -> Int {
  case b == 0 {
    True -> a
    False -> gcd(b, a % b)
  }
}

fn to_ints(text: String) -> List(Int) {
  text
  |> string.lowercase
  |> string.to_utf_codepoints
  |> list.map(string.utf_codepoint_to_int)
  |> list.filter(fn(x) { { x >= 97 && x <= 122 } || { x >= 48 && x <= 57 } })
  |> list.map(fn(x) { x - 97 })
}

fn to_string(ints: List(Int)) -> String {
  ints
  |> list.map(fn(x) { x + 97 })
  |> list.filter_map(string.utf_codepoint)
  |> string.from_utf_codepoints
}

pub fn code(plaintext: String, f: fn(Int) -> Int) -> String {
  plaintext
  |> to_ints
  |> list.map(fn(x) {
    case x >= 0 && x < 26 {
      True -> f(x)
      False -> x
    }
  })
  |> to_string
}

pub fn encode(
  plaintext plaintext: String,
  a a: Int,
  b b: Int,
) -> Result(String, Error) {
  use <- bool.guard(gcd(a, 26) != 1, Error(KeyNotCoprime(a, 26)))
  code(plaintext, fn(x) { { a * x + b } % 26 })
  |> string.to_graphemes
  |> list.sized_chunk(5)
  |> list.intersperse([" "])
  |> list.flatten
  |> string.concat
  |> Ok
}

pub fn decode(
  ciphertext ciphertext: String,
  a a: Int,
  b b: Int,
) -> Result(String, Error) {
  use <- bool.guard(gcd(a, 26) != 1, Error(KeyNotCoprime(a, 26)))

  let a_inv_m =
    iterator.range(1, 25)
    |> iterator.filter(fn(x) { { { a % 26 } * { x % 26 } } % 26 == 1 })
    |> iterator.first
    |> result.unwrap(0)

  Ok(code(ciphertext, fn(x) { mod(a_inv_m * { x - b }, 26) }))
}
