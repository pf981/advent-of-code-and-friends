import gleam/int
import gleam/list

pub type Command {
  Wink
  DoubleBlink
  CloseYourEyes
  Jump
}

fn to_int(command: Command) -> Int {
  case command {
    Wink -> 1
    DoubleBlink -> 2
    CloseYourEyes -> 4
    Jump -> 8
  }
}

fn should_do(command: Command, encoded_message: Int) -> Bool {
  case int.bitwise_and(encoded_message, to_int(command)) {
    0 -> False
    _ -> True
  }
}

pub fn commands(encoded_message: Int) -> List(Command) {
  let command_list =
    [Wink, DoubleBlink, CloseYourEyes, Jump]
    |> list.filter(should_do(_, encoded_message))

  case int.bitwise_and(encoded_message, 16) {
    0 -> command_list
    _ -> list.reverse(command_list)
  }
}
