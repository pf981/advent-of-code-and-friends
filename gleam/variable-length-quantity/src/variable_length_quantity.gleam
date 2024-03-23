import gleam/bit_array
import gleam/bool
import gleam/int
import gleam/list

pub type Error {
  IncompleteSequence
}

pub fn encode(integers: List(Int)) -> BitArray {
  integers
  |> list.map(fn(num) {
    case num {
      0 -> <<0>>
      _ -> encode_one(num, <<>>, 0)
    }
  })
  |> bit_array.concat
}

pub fn decode(string: BitArray) -> Result(List(Int), Error) {
  decode_impl(string, [], 0)
}

fn encode_one(num: Int, acc: BitArray, prefix: Int) -> BitArray {
  use <- bool.guard(num == 0, acc)
  encode_one(
    int.bitwise_shift_right(num, 7),
    <<prefix:size(1), num:size(7), acc:bits>>,
    1,
  )
}

fn decode_impl(
  string: BitArray,
  acc: List(Int),
  current_value: Int,
) -> Result(List(Int), Error) {
  case string {
    <<>> -> Ok(list.reverse(acc))
    <<1:size(1), _:size(7)>> -> Error(IncompleteSequence)
    <<prefix:size(1), seven_bits:size(7), rest:bits>> -> {
      let current_value =
        int.bitwise_or(int.bitwise_shift_left(current_value, 7), seven_bits)
      case prefix {
        0 -> decode_impl(rest, [current_value, ..acc], 0)
        _ -> decode_impl(rest, acc, current_value)
      }
    }
    _ -> Error(IncompleteSequence)
  }
}
