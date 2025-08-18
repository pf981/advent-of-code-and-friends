import gleam/list
import gleam/string

fn standardise(s: String) -> List(String) {
  s
  |> string.lowercase
  |> string.to_graphemes
  |> list.sort(string.compare)
}

fn is_anagram(candidate: String, word: String) -> Bool {
  standardise(candidate) == standardise(word)
  && string.lowercase(candidate) != string.lowercase(word)
}

pub fn find_anagrams(word: String, candidates: List(String)) -> List(String) {
  candidates
  |> list.filter(is_anagram(_, word))
}
