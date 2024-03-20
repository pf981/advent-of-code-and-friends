import gleam/dict.{type Dict}
import gleam/list
import gleam/result
import gleam/string

fn count(
  counter: Dict(String, Int),
  char: String,
) -> Result(Dict(String, Int), Nil) {
  case char {
    "A" | "C" | "G" | "T" ->
      case dict.get(counter, char) {
        Ok(num) -> Ok(dict.insert(counter, char, num + 1))
        Error(Nil) -> Error(Nil)
      }
    _ -> Error(Nil)
  }
}

pub fn nucleotide_count(dna: String) -> Result(Dict(String, Int), Nil) {
  dna
  |> string.to_graphemes
  |> list.fold(
    Ok(dict.from_list([#("A", 0), #("C", 0), #("G", 0), #("T", 0)])),
    fn(acc, char) { result.try(acc, count(_, char)) },
  )
}
