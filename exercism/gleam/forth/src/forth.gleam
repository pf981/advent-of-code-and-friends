import gleam/dict
import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub type Forth {
  Forth(
    stack: List(Int),
    command_fns: dict.Dict(String, fn(Forth) -> Result(Forth, ForthError)),
  )
}

pub type ForthError {
  DivisionByZero
  StackUnderflow
  InvalidWord
  UnknownWord
}

pub fn new() -> Forth {
  Forth(
    [],
    dict.from_list([
      #("DUP", fn(f: Forth) {
        case f.stack {
          [head, ..rest] -> Ok(Forth(..f, stack: [head, head, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
      #("DROP", fn(f: Forth) {
        case f.stack {
          [_, ..rest] -> Ok(Forth(..f, stack: rest))
          _ -> Error(StackUnderflow)
        }
      }),
      #("SWAP", fn(f: Forth) {
        case f.stack {
          [a, b, ..rest] -> Ok(Forth(..f, stack: [b, a, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
      #("OVER", fn(f: Forth) {
        case f.stack {
          [a, b, ..rest] -> Ok(Forth(..f, stack: [b, a, b, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
      #("+", fn(f: Forth) {
        case f.stack {
          [a, b, ..rest] -> Ok(Forth(..f, stack: [b + a, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
      #("-", fn(f: Forth) {
        case f.stack {
          [a, b, ..rest] -> Ok(Forth(..f, stack: [b - a, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
      #("*", fn(f: Forth) {
        case f.stack {
          [a, b, ..rest] -> Ok(Forth(..f, stack: [b * a, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
      #("/", fn(f: Forth) {
        case f.stack {
          [a, _, ..] if a == 0 -> Error(DivisionByZero)
          [a, b, ..rest] -> Ok(Forth(..f, stack: [b / a, ..rest]))
          _ -> Error(StackUnderflow)
        }
      }),
    ]),
  )
}

pub fn format_stack(f: Forth) -> String {
  f.stack
  |> list.map(int.to_string)
  |> list.reverse()
  |> list.intersperse(" ")
  |> string.concat()
}

fn to_func(
  commands: List(String),
  command_fns: dict.Dict(String, fn(Forth) -> Result(Forth, ForthError)),
  acc: fn(Forth) -> Result(Forth, ForthError),
) -> fn(Forth) -> Result(Forth, ForthError) {
  case commands {
    [] -> acc
    [command, ..rest] ->
      case int.base_parse(command, 10) {
        Ok(num) ->
          to_func(rest, command_fns, fn(f) {
            f
            |> acc()
            |> result.try(fn(f) { Ok(Forth(..f, stack: [num, ..f.stack])) })
          })
        Error(Nil) -> {
          let func = case dict.get(command_fns, command) {
            Ok(func) -> func
            Error(Nil) -> fn(_) { Error(UnknownWord) }
          }

          to_func(rest, command_fns, fn(f) {
            f
            |> acc()
            |> result.try(func)
          })
        }
      }
  }
}

fn update_definition(
  f: Forth,
  definition: List(String),
) -> Result(Forth, ForthError) {
  case definition {
    [name, ..commands] ->
      case int.base_parse(name, 10) {
        Ok(_) -> Error(InvalidWord)
        Error(Nil) ->
          Ok(
            Forth(
              ..f,
              command_fns: dict.insert(
                f.command_fns,
                name,
                to_func(commands, f.command_fns, fn(f) { Ok(f) }),
              ),
            ),
          )
      }

    _ -> Error(InvalidWord)
  }
}

pub fn eval(f: Forth, prog: String) -> Result(Forth, ForthError) {
  let prog = string.uppercase(prog)

  case prog {
    ": " <> definition ->
      update_definition(
        f,
        definition
          |> string.replace(" ;", "")
          |> string.split(" "),
      )
    commands -> {
      let func =
        commands
        |> string.split(" ")
        |> to_func(f.command_fns, fn(f) { Ok(f) })
      func(f)
    }
  }
}
