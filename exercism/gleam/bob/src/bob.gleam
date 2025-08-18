import gleam/string

pub fn hey(remark: String) -> String {
  let remark = string.trim(remark)
  let is_question = string.ends_with(remark, "?")
  let is_yelling =
    remark == string.uppercase(remark) && remark != string.lowercase(remark)

  case remark {
    "" -> "Fine. Be that way!"
    _ if is_question && is_yelling -> "Calm down, I know what I'm doing!"
    _ if is_question -> "Sure."
    _ if is_yelling -> "Whoa, chill out!"
    _ -> "Whatever."
  }
}
