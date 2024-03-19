import gleam/list
import gleam/result
import gleam/string

pub type Student {
  Alice
  Bob
  Charlie
  David
  Eve
  Fred
  Ginny
  Harriet
  Ileana
  Joseph
  Kincaid
  Larry
}

pub type Plant {
  Radishes
  Clover
  Violets
  Grass
}

fn to_int(student: Student) -> Int {
  case student {
    Alice -> 0
    Bob -> 1
    Charlie -> 2
    David -> 3
    Eve -> 4
    Fred -> 5
    Ginny -> 6
    Harriet -> 7
    Ileana -> 8
    Joseph -> 9
    Kincaid -> 10
    Larry -> 11
  }
}

fn to_plants(plant: String) -> Result(Plant, Nil) {
  case plant {
    "R" -> Ok(Radishes)
    "C" -> Ok(Clover)
    "V" -> Ok(Violets)
    "G" -> Ok(Grass)
    _ -> Error(Nil)
  }
}

fn extract_nth(line: String, n: Int) -> List(String) {
  line
  |> string.to_graphemes
  |> list.sized_chunk(2)
  |> list.at(n)
  |> result.unwrap([])
}

pub fn plants(diagram: String, student: Student) -> List(Plant) {
  diagram
  |> string.split("\n")
  |> list.map(extract_nth(_, to_int(student)))
  |> list.flatten
  |> list.map(to_plants)
  |> result.values
}
