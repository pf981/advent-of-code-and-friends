import gleam/list
import gleam/result

fn parse(rna: String, acc: List(String)) -> Result(List(String), Nil) {
  case rna {
    "AUG" <> rest -> parse(rest, ["Methionine", ..acc])
    "UUU" <> rest | "UUC" <> rest -> parse(rest, ["Phenylalanine", ..acc])
    "UUA" <> rest | "UUG" <> rest -> parse(rest, ["Leucine", ..acc])
    "UCU" <> rest | "UCC" <> rest | "UCA" <> rest | "UCG" <> rest ->
      parse(rest, ["Serine", ..acc])
    "UAU" <> rest | "UAC" <> rest -> parse(rest, ["Tyrosine", ..acc])
    "UGU" <> rest | "UGC" <> rest -> parse(rest, ["Cysteine", ..acc])
    "UGG" <> rest -> parse(rest, ["Tryptophan", ..acc])
    "UAA" <> _ | "UAG" <> _ | "UGA" <> _ | "" -> Ok(acc)
    _ -> Error(Nil)
  }
}

pub fn proteins(rna: String) -> Result(List(String), Nil) {
  parse(rna, [])
  |> result.map(list.reverse)
}
