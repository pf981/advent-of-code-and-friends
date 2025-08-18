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
  QuestionMark
}

pub type Error {
  SyntaxError
  UnknownOperation
  ImpossibleOperation
}

fn take_digits(s: String, acc: String) -> #(String, String) {
  case string.pop_grapheme(s) {
    Ok(#(first, rest)) ->
      case string.contains("0123456789-", first) {
        True -> take_digits(rest, acc <> first)
        False -> #(acc, s)
      }
    Error(Nil) -> #(acc, s)
  }
}

fn take_number(s: String) -> Result(#(Token, String), Nil) {
  let #(digits, rest) = take_digits(s, "")

  case int.base_parse(digits, 10) {
    Ok(num) -> Ok(#(Value(num), rest))
    Error(Nil) -> Error(Nil)
  }
}

fn lex(s: String, acc: List(Token)) -> Result(List(Token), Error) {
  let s = string.trim_left(s)

  case take_number(s) {
    Ok(#(value, rest)) -> lex(rest, [value, ..acc])
    Error(Nil) ->
      case s {
        "" -> Ok(acc)
        "?" <> rest -> lex(rest, [QuestionMark, ..acc])
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
    [Value(a), QuestionMark] -> Ok(a)
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
