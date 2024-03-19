import gleam/list
import gleam/result
import gleam/string

fn char_to_rna(char: String) -> Result(String, Nil) {
  case char {
    "G" -> Ok("C")
    "C" -> Ok("G")
    "T" -> Ok("A")
    "A" -> Ok("U")
    _ -> Error(Nil)
  }
}

pub fn to_rna(dna: String) -> Result(String, Nil) {
  dna
  |> string.to_graphemes
  |> list.try_map(char_to_rna)
  |> result.map(string.concat)
}
