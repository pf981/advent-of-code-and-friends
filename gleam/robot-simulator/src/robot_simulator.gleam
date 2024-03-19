import gleam/list
import gleam/result
import gleam/string

pub type Robot {
  Robot(direction: Direction, position: Position)
}

pub type Direction {
  North
  East
  South
  West
}

pub type Position {
  Position(x: Int, y: Int)
}

type Instruction {
  Right
  Left
  Advance
}

pub fn create(direction: Direction, position: Position) -> Robot {
  Robot(direction, position)
}

fn to_instruction(char: String) -> Result(Instruction, Nil) {
  case char {
    "R" -> Ok(Right)
    "L" -> Ok(Left)
    "A" -> Ok(Advance)
    _ -> Error(Nil)
  }
}

fn handle_instruction(robot: Robot, instruction: Instruction) -> Robot {
  let Robot(direction, position) = robot

  case instruction, direction {
    Right, North -> Robot(East, position)
    Right, East -> Robot(South, position)
    Right, South -> Robot(West, position)
    Right, West -> Robot(North, position)
    Left, North -> Robot(West, position)
    Left, East -> Robot(North, position)
    Left, South -> Robot(East, position)
    Left, West -> Robot(South, position)
    Advance, North -> Robot(direction, Position(position.x, position.y + 1))
    Advance, East -> Robot(direction, Position(position.x + 1, position.y))
    Advance, South -> Robot(direction, Position(position.x, position.y - 1))
    Advance, West -> Robot(direction, Position(position.x - 1, position.y))
  }
}

pub fn move(
  direction: Direction,
  position: Position,
  instructions: String,
) -> Robot {
  instructions
  |> string.to_graphemes
  |> list.map(to_instruction)
  |> result.values
  |> list.fold(Robot(direction, position), handle_instruction)
}
