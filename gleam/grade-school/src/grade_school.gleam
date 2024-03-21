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
  let grades = list.sort(dict.keys(school), int.compare)
  list.flat_map(grades, grade(school, _))
}

pub fn add(
  to school: School,
  student student: String,
  grade grade_num: Int,
) -> Result(School, Nil) {
  let all_students =
    school
    |> dict.values
    |> list.flatten

  case list.contains(all_students, student) {
    True -> Error(Nil)
    False ->
      Ok(dict.insert(
        school,
        grade_num,
        list.sort([student, ..grade(school, grade_num)], string.compare),
      ))
  }
}

pub fn grade(school: School, desired_grade: Int) -> List(String) {
  school
  |> dict.get(desired_grade)
  |> result.unwrap([])
}
