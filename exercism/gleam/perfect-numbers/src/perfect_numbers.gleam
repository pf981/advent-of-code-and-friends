import gleam/int
import gleam/order
import gleam/set.{type Set}

pub type Classification {
  Perfect
  Abundant
  Deficient
}

pub type Error {
  NonPositiveInt
}

pub fn classify(number: Int) -> Result(Classification, Error) {
  case number {
    num if num <= 0 -> Error(NonPositiveInt)
    _ -> {
      let cmp =
        number
        |> get_factors(1, set.new())
        |> set.delete(number)
        |> set.to_list
        |> int.sum
        |> int.compare(number)
      case cmp {
        order.Lt -> Ok(Deficient)
        order.Eq -> Ok(Perfect)
        order.Gt -> Ok(Abundant)
      }
    }
  }
}

fn get_factors(number: Int, i: Int, acc: Set(Int)) -> Set(Int) {
  case i * i <= number, number % i == 0 {
    True, True ->
      get_factors(
        number,
        i + 1,
        acc
          |> set.insert(i)
          |> set.insert(number / i),
      )
    True, False -> get_factors(number, i + 1, acc)
    False, _ -> acc
  }
}
