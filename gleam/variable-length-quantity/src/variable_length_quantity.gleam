import gleam/bit_array
import gleam/bool
import gleam/int
import gleam/list

pub type Error {
  IncompleteSequence
}

fn encode_one(num: Int, acc: BitArray, prefix: Int) -> BitArray {
  use <- bool.guard(num == 0, acc)
  encode_one(
    int.bitwise_shift_right(num, 7),
    <<prefix:size(1), num:size(7), acc:bits>>,
    1,
  )
  // split(int.bitwise_shift_right(num, 7), list.append(acc, [<<num:size(7)>>]))
}

// fn encode_one(num: Int) -> BitArray {
//   num
//   |> split(<<>>, 0)
//   |> io.debug
//   // |> list.intersperse(<<1:size(1)>>)
//   |> io.debug
//   // |> bit_array.concat
//   // |> bit_array.append(<<0:size(1)>>, _)
//   |> io.debug
//   |> io.debug
//   |> io.debug
//   |> io.debug
// }

pub fn encode(integers: List(Int)) -> BitArray {
  integers
  |> list.map(encode_one(_, <<>>, 0))
  |> bit_array.concat
}

pub fn decode(string: BitArray) -> Result(List(Int), Error) {
  todo
}

import gleam/io

pub fn main() {
  // [0x80]
  // |> io.debug

  let x =
    encode([0x80])
    |> io.debug

  // let assert <<y>> = x

  io.debug(x == <<0x81, 0x0>>)
}
