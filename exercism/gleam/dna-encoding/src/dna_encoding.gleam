import gleam/list
import gleam/result

pub type Nucleotide {
  Adenine
  Cytosine
  Guanine
  Thymine
}

pub fn encode_nucleotide(nucleotide: Nucleotide) -> Int {
  case nucleotide {
    Adenine -> 0b00
    Cytosine -> 0b01
    Guanine -> 0b10
    Thymine -> 0b11
  }
}

pub fn decode_nucleotide(nucleotide: Int) -> Result(Nucleotide, Nil) {
  case nucleotide {
    0b00 -> Ok(Adenine)
    0b01 -> Ok(Cytosine)
    0b10 -> Ok(Guanine)
    0b11 -> Ok(Thymine)
    _ -> Error(Nil)
  }
}

pub fn encode(dna: List(Nucleotide)) -> BitArray {
  list.fold(dna, <<>>, fn(acc, el) { <<acc:bits, encode_nucleotide(el):2>> })
}

pub fn decode(dna: BitArray) -> Result(List(Nucleotide), Nil) {
  to_nucleotides(dna, [])
}

fn to_nucleotides(
  dna: BitArray,
  acc: List(Int),
) -> Result(List(Nucleotide), Nil) {
  case dna {
    <<>> ->
      list.reverse(acc)
      |> list.map(decode_nucleotide)
      |> result.all()
    <<nucleotide:2, rest:bits>> -> to_nucleotides(rest, [nucleotide, ..acc])
    _ -> Error(Nil)
  }
}
