pub fn today(days: List(Int)) -> Int {
  case days {
    [] -> 0
    [day, ..] -> day
  }
}

pub fn increment_day_count(days: List(Int)) -> List(Int) {
  case days {
    [] -> [1]
    [head, ..tail] -> [head + 1, ..tail]
  }
}

pub fn has_day_without_birds(days: List(Int)) -> Bool {
  case days {
    [] -> False
    [head, ..] if head == 0 -> True
    [_, ..tail] -> has_day_without_birds(tail)
  }
}

fn total_impl(days: List(Int), result: Int) -> Int {
  case days {
    [] -> result
    [head, ..tail] -> total_impl(tail, result + head)
  }
}

pub fn total(days: List(Int)) -> Int {
  total_impl(days, 0)
}

fn busy_days_impl(days: List(Int), result: Int) -> Int {
  case days {
    [] -> result
    [head, ..tail] if head >= 5 -> busy_days_impl(tail, result + 1)
    [_, ..tail] -> busy_days_impl(tail, result)
  }
}

pub fn busy_days(days: List(Int)) -> Int {
  busy_days_impl(days, 0)
}
