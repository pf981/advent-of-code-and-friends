import gleam/int
import gleam/list
import gleam/string

fn luhn(nums: List(Int)) -> Int {
  nums
  |> list.filter(fn(num) { num >= 0 && num <= 9 })
  |> list.reverse
  |> list.index_map(fn(num, i) {
    case i % 2 == 1 {
      False -> num
      True ->
        case num * 2 {
          val if val > 9 -> val - 9
          val -> val
        }
    }
  })
  |> int.sum
}

pub fn valid(value: String) -> Bool {
  let nums =
    value
    |> string.to_utf_codepoints
    |> list.map(fn(codepoint) { string.utf_codepoint_to_int(codepoint) - 48 })

  !string.starts_with(value, " ")
  && list.length(nums) > 1
  && list.all(nums, fn(num) { { num >= 0 && num <= 9 } || num == -16 })
  && luhn(nums) % 10 == 0
}
