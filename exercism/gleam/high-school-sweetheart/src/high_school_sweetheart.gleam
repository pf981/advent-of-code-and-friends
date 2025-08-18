import gleam/list
import gleam/result
import gleam/string

pub fn first_letter(name: String) {
  name
  |> string.trim()
  |> string.first()
  |> result.unwrap("")
}

pub fn initial(name: String) {
  let ch =
    name
    |> first_letter()
    |> string.uppercase()
  ch <> "."
}

pub fn initials(full_name: String) {
  full_name
  |> string.split(" ")
  |> list.map(initial)
  |> list.intersperse(" ")
  |> string.concat()
}

pub fn pair(full_name1: String, full_name2: String) {
  let middle = initials(full_name1) <> "  +  " <> initials(full_name2)
  "
     ******       ******
   **      **   **      **
 **         ** **         **
**            *            **
**                         **
**     " <> middle <> "     **
 **                       **
   **                   **
     **               **
       **           **
         **       **
           **   **
             ***
              *
"
}
