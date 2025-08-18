import gleam/list
import gleam/string

type Sound {
  Vowel(text: String)
  Consonant(text: String)
}

fn lex_rest(letters: String) -> List(Sound) {
  letters
  |> string.to_graphemes
  |> list.prepend("")
  |> list.window_by_2()
  |> list.map(fn(pair) {
    case pair.1 {
      "u" if pair.0 == "q" -> Consonant("u")
      "a" as c | "e" as c | "i" as c | "o" as c | "u" as c | "y" as c ->
        Vowel(c)
      c -> Consonant(c)
    }
  })
}

fn lex(letters: String) -> List(Sound) {
  case letters {
    "xr" <> rest -> [Vowel("xr"), ..lex_rest(rest)]
    "yt" <> rest -> [Vowel("yt"), ..lex_rest(rest)]
    "y" <> rest -> [Consonant("y"), ..lex_rest(rest)]
    rest -> lex_rest(rest)
  }
}

fn reorder(sounds: List(Sound)) -> List(Sound) {
  let #(consonants, rest) =
    list.split_while(sounds, fn(sound) {
      case sound {
        Consonant(_) -> True
        _ -> False
      }
    })

  list.append(rest, consonants)
}

fn pig(word: String) -> String {
  word
  |> lex
  |> reorder
  |> list.map(fn(sound) { sound.text })
  |> string.concat
  |> string.append("ay")
}

pub fn translate(phrase: String) -> String {
  phrase
  |> string.split(" ")
  |> list.map(pig)
  |> string.join(" ")
}
