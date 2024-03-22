import gleam/bit_array
import gleam/list
import gleam/string

fn encode_char(c: String) -> Result(String, Nil) {
  case <<c:utf8>> {
    <<code>> if code >= 48 && code <= 57 -> Ok(c)
    <<code>> if code >= 97 && code <= 122 -> {
      let code2 = 97 + 122 - code
      bit_array.to_string(<<code2>>)
    }
    _ -> Error(Nil)
  }
}

pub fn encode(phrase: String) -> String {
  phrase
  |> string.lowercase
  |> string.to_graphemes
  |> list.filter_map(encode_char)
  |> list.sized_chunk(5)
  |> list.intersperse([" "])
  |> list.flatten
  |> string.concat
}

pub fn decode(phrase: String) -> String {
  phrase
  |> string.lowercase
  |> string.to_graphemes
  |> list.filter_map(encode_char)
  |> string.concat
}
