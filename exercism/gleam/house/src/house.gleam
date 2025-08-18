import gleam/list
import gleam/string

fn parts(verse: Int) -> #(String, String) {
  case verse {
    1 -> #("house", "Jack built.")
    2 -> #("malt", "lay in")
    3 -> #("rat", "ate")
    4 -> #("cat", "killed")
    5 -> #("dog", "worried")
    6 -> #("cow with the crumpled horn", "tossed")
    7 -> #("maiden all forlorn", "milked")
    8 -> #("man all tattered and torn", "kissed")
    9 -> #("priest all shaven and shorn", "married")
    10 -> #("rooster that crowed in the morn", "woke")
    11 -> #("farmer sowing his corn", "kept")
    12 -> #("horse and the hound and the horn", "belonged to")
    _ -> #("", "")
  }
}

fn recite_verse(verse: Int) -> String {
  list.range(verse, 1)
  |> list.map(fn(i) {
    let #(object, action) = parts(i)
    "the " <> object <> " that " <> action
  })
  |> list.prepend("This is")
  |> string.join(" ")
}

pub fn recite(start_verse start_verse: Int, end_verse end_verse: Int) -> String {
  list.range(start_verse, end_verse)
  |> list.map(recite_verse)
  |> string.join("\n")
}
