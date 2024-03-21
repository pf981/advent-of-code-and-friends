import gleam/bool
import gleam/iterator
import gleam/list

fn is_prime(candidate: Int, primes: List(Int)) -> Bool {
  list.all(primes, fn(divisor) { candidate % divisor != 0 })
}

pub fn prime(number: Int) -> Result(Int, Nil) {
  use <- bool.guard(number < 1, Error(Nil))

  iterator.single(2)
  |> iterator.append(iterator.iterate(3, fn(i) { i + 2 }))
  |> iterator.fold_until([], fn(primes, candidate) {
    case is_prime(candidate, primes) {
      True ->
        case list.length(primes) + 1 == number {
          True -> list.Stop([candidate, ..primes])
          False -> list.Continue([candidate, ..primes])
        }
      False -> list.Continue(primes)
    }
  })
  |> list.first
}
