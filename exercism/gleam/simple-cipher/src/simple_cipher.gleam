import gleam/bit_array
import gleam/int
import gleam/iterator.{type Iterator}
import gleam/list
import gleam/result
import gleam/string

fn key_to_distances(key: String) -> Iterator(Int) {
  key
  |> string.to_graphemes
  |> list.map(fn(c) {
    case <<c:utf8>> {
      <<num>> -> num - 97
      _ -> 0
    }
  })
  |> iterator.from_list()
  |> iterator.cycle
}

fn mod(dividend: Int, divisor: Int) -> Int {
  case dividend % divisor {
    num if num >= 0 -> num
    num -> num + divisor
  }
}

fn shift(c: String, distance: Int) -> String {
  case <<c:utf8>> {
    <<num>> ->
      <<{ mod(num - 97 + distance, 26) + 97 }>>
      |> bit_array.to_string
    _ -> Error(Nil)
  }
  |> result.unwrap("")
}

fn encode_impl(plaintext: String, distances: Iterator(Int)) -> String {
  plaintext
  |> string.to_graphemes
  |> iterator.from_list
  |> iterator.zip(distances)
  |> iterator.map(fn(pair) { shift(pair.0, pair.1) })
  |> iterator.to_list
  |> string.concat
}

pub fn encode(plaintext plaintext: String, key key: String) -> String {
  encode_impl(plaintext, key_to_distances(key))
}

pub fn decode(ciphertext ciphertext: String, key key: String) -> String {
  let distances =
    key
    |> key_to_distances
    |> iterator.map(fn(num) { -num })
  encode_impl(ciphertext, distances)
}

pub fn generate_key() -> String {
  iterator.repeatedly(fn() {
    <<{ int.random(26) + 97 }>>
    |> bit_array.to_string()
    |> result.unwrap("")
  })
  |> iterator.take(10 + int.random(20))
  |> iterator.to_list
  |> string.concat
}
