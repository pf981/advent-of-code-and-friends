import gleam/bool
import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub type School =
  Dict(Int, List(String))

pub fn create() -> School {
  dict.new()
}

pub fn roster(school: School) -> List(String) {
  school
  |> dict.map_values(fn(_key, value) { list.sort(value, string.compare) })
  |> dict.to_list
  |> list.sort(fn(pair1, pair2) { int.compare(pair1.0, pair2.0) })
  |> list.flat_map(fn(pair) { pair.1 })
}

pub fn add(
  to school: School,
  student student: String,
  grade grade: Int,
) -> Result(School, Nil) {
  let all_students =
    school
    |> dict.values
    |> list.flatten

  use <- bool.guard(list.contains(all_students, student), Error(Nil))

  let grade_students =
    school
    |> dict.get(grade)
    |> result.unwrap([])

  Ok(dict.insert(school, grade, [student, ..grade_students]))
}

pub fn grade(school: School, desired_grade: Int) -> List(String) {
  school
  |> dict.get(desired_grade)
  |> result.unwrap([])
}
