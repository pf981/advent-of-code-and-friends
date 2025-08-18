import gleam/int
import gleam/result
import gleam/string

pub type Clock {
  Clock(minutes: Int)
}

fn creat_clock(minutes: Int) -> Clock {
  minutes
  |> int.modulo(1440)
  |> result.unwrap(0)
  |> Clock
}

pub fn create(hour hour: Int, minute minute: Int) -> Clock {
  creat_clock(hour * 60 + minute)
}

pub fn add(clock: Clock, minutes minutes: Int) -> Clock {
  creat_clock(clock.minutes + minutes)
}

pub fn subtract(clock: Clock, minutes minutes: Int) -> Clock {
  creat_clock(clock.minutes - minutes)
}

pub fn display(clock: Clock) -> String {
  let print = fn(i) {
    i
    |> int.to_string
    |> string.pad_left(2, "0")
  }

  let hour = clock.minutes / 60 % 24
  let minute = clock.minutes % 60

  print(hour) <> ":" <> print(minute)
}
