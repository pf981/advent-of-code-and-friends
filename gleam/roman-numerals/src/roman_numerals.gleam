fn convert_impl(number: Int, result: String) -> String {
  case number {
    0 -> result
    i if i >= 1000 -> convert_impl(number - 1000, result <> "M")
    i if i >= 900 -> convert_impl(number - 900, result <> "CM")
    i if i >= 500 -> convert_impl(number - 500, result <> "D")
    i if i >= 400 -> convert_impl(number - 400, result <> "CD")
    i if i >= 100 -> convert_impl(number - 100, result <> "C")
    i if i >= 90 -> convert_impl(number - 90, result <> "XC")
    i if i >= 50 -> convert_impl(number - 50, result <> "L")
    i if i >= 40 -> convert_impl(number - 40, result <> "XL")
    i if i >= 10 -> convert_impl(number - 10, result <> "X")
    i if i >= 9 -> convert_impl(number - 9, result <> "IX")
    i if i >= 5 -> convert_impl(number - 5, result <> "V")
    i if i >= 4 -> convert_impl(number - 4, result <> "IV")
    i if i >= 1 -> convert_impl(number - 1, result <> "I")
    _ -> panic
  }
}

pub fn convert(number: Int) -> String {
  convert_impl(number, "")
}
