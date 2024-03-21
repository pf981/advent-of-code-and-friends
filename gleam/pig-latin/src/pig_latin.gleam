import gleam/list
import gleam/string

type Sound {
  Vowel(text: String)
  Consonant(text: String)
}

fn to_sound(letter: String) -> Sound {
  case string.contains("aeiouy", letter) {
    True -> Vowel(letter)
    False -> Consonant(letter)
  }
}

fn lex_rest(letters: List(String)) -> List(Sound) {
  letters
  |> list.prepend("")
  |> list.window_by_2()
  |> list.map(fn(pair) {
    case pair {
      #("q", "u") -> Consonant("u")
      #(_, letter) -> to_sound(letter)
    }
  })
}

fn lex(letters: List(String)) -> List(Sound) {
  case letters {
    [] -> []
    ["x", "r", ..rest] -> [Vowel("xr"), ..lex_rest(rest)]
    ["y", "t", ..rest] -> [Vowel("yt"), ..lex_rest(rest)]
    ["y", ..rest] -> [Consonant("y"), ..lex_rest(rest)]
    [first, "y", ..rest] -> [to_sound(first), Vowel("y"), ..lex_rest(rest)]
    rest -> lex_rest(rest)
  }
}

fn reorder(sounds: List(Sound), acc: List(Sound)) -> List(Sound) {
  case sounds {
    [] -> acc
    [Vowel(_), ..] -> list.append(sounds, acc)
    [Consonant(_) as first, ..rest] -> reorder(rest, list.append(acc, [first]))
  }
}

fn to_string(sounds: List(Sound)) -> String {
  sounds
  |> list.map(fn(sound) { sound.text })
  |> string.concat
  |> string.append("ay")
}

fn pig(word: String) -> String {
  word
  |> string.to_graphemes
  |> lex
  |> reorder([])
  |> to_string
}

pub fn translate(phrase: String) -> String {
  phrase
  |> string.split(" ")
  |> list.map(pig)
  |> string.join(" ")
}
