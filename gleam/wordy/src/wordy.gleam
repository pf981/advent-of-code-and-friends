import gleam/int
import gleam/list
import gleam/result
import gleam/string

type Token {
  Value(Int)
  Plus
  Minus
  Multiply
  Divide
}

pub type Error {
  SyntaxError
  UnknownOperation
  ImpossibleOperation
}

fn take_number(s: String) -> Result(#(Token, String), Nil) {
  let #(left, right) =
    s
    |> string.split_once(" ")
    |> result.unwrap(#(s, ""))

  let #(left, right) = case string.ends_with(left, "?") {
    True -> #(string.drop_right(left, 1), "?" <> right)
    False -> #(left, right)
  }

  case int.base_parse(left, 10) {
    Ok(num) -> Ok(#(Value(num), right))
    Error(Nil) -> Error(Nil)
  }
}

fn lex(s: String, acc: List(Token)) -> Result(List(Token), Error) {
  let s = string.trim(s)

  case take_number(s) {
    Ok(#(value, rest)) -> lex(rest, [value, ..acc])
    Error(Nil) ->
      case s {
        "?" -> Ok(acc)
        "What is" <> rest if acc == [] -> lex(rest, acc)
        "plus" <> rest -> lex(rest, [Plus, ..acc])
        "minus" <> rest -> lex(rest, [Minus, ..acc])
        "multiplied by" <> rest -> lex(rest, [Multiply, ..acc])
        "divided by" <> rest -> lex(rest, [Divide, ..acc])
        _ -> Error(UnknownOperation)
      }
  }
}

fn parse(tokens: List(Token)) -> Result(Int, Error) {
  case tokens {
    [Value(a)] -> Ok(a)
    [Value(a), Plus, Value(b), ..rest] -> parse([Value(a + b), ..rest])
    [Value(a), Minus, Value(b), ..rest] -> parse([Value(a - b), ..rest])
    [Value(a), Multiply, Value(b), ..rest] -> parse([Value(a * b), ..rest])
    [Value(_), Divide, Value(b), ..] if b == 0 -> Error(ImpossibleOperation)
    [Value(a), Divide, Value(b), ..rest] -> parse([Value(a / b), ..rest])
    _ -> Error(SyntaxError)
  }
}

pub fn answer(question: String) -> Result(Int, Error) {
  question
  |> lex([])
  |> result.map(list.reverse)
  |> result.try(parse)
}
