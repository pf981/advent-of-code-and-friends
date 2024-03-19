fn egg_count_impl(number: Int, result: Int) -> Int {
  case number {
    0 -> result
    _ -> egg_count_impl(number / 2, result + {number % 2})
  }
}

pub fn egg_count(number: Int) -> Int {
  egg_count_impl(number, 0)
}
