import gleam/result

pub fn with_retry(experiment: fn() -> Result(t, e)) -> Result(t, e) {
  case experiment() {
    Ok(value) -> Ok(value)
    Error(_) -> experiment()
  }
}

pub fn record_timing(
  time_logger: fn() -> Nil,
  experiment: fn() -> Result(t, e),
) -> Result(t, e) {
  time_logger()
  let output = experiment()
  time_logger()
  output
}

pub fn run_experiment(
  name: String,
  setup: fn() -> Result(t, e),
  action: fn(t) -> Result(u, e),
  record: fn(t, u) -> Result(v, e),
) -> Result(#(String, v), e) {
  // result.try(setup(), fn(a) {
  //   result.try(action(a), fn(b) {
  //     result.try(record(a, b), fn(c) { Ok(#(name, c)) })
  //   })
  // })
  use a <- result.try(setup())
  use b <- result.try(action(a))
  use c <- result.try(record(a, b))
  Ok(#(name, c))
}
