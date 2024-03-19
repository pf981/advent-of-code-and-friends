import gleam/list

pub type Triplet {
  Triplet(Int, Int, Int)
}

fn find_bc(a: Int, sum: Int) -> List(Triplet) {
  list.range(a + 1, sum)
  |> list.filter_map(fn(b) {
    let c = sum - a - b
    case b < c && a * a + b * b == c * c {
      True -> Ok(Triplet(a, b, c))
      False -> Error(Nil)
    }
  })
}

pub fn triplets_with_sum(sum: Int) {
  list.range(1, sum)
  |> list.flat_map(find_bc(_, sum))
}
