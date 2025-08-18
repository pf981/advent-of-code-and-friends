import gleam/bool
import gleam/list
import gleam/string

pub type Error {
  EmptySeries
  SliceLengthTooLarge
  SliceLengthZero
  SliceLengthNegative
}

pub fn slices(input: String, size: Int) -> Result(List(String), Error) {
  use <- bool.guard(input == "", Error(EmptySeries))
  use <- bool.guard(size > string.length(input), Error(SliceLengthTooLarge))
  use <- bool.guard(size == 0, Error(SliceLengthZero))
  use <- bool.guard(size < 0, Error(SliceLengthNegative))
  input
  |> string.to_graphemes
  |> list.window(size)
  |> list.map(string.concat)
  |> Ok
}
