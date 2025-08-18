fn sqrt(radicand: Int, left: Int, right: Int) -> Int {
  let mid = { left + right } / 2
  case mid * mid {
    num if num == radicand -> mid
    num if num > radicand -> sqrt(radicand, left, mid)
    _ -> sqrt(radicand, mid, right)
  }
}

pub fn square_root(radicand: Int) -> Int {
  sqrt(radicand, 1, radicand)
}
