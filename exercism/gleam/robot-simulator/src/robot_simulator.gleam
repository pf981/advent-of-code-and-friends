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

fn right(robot: Robot) -> Robot {
  let direction = case robot.direction {
    North -> East
    East -> South
    South -> West
    West -> North
  }
  Robot(..robot, direction: direction)
}

fn left(robot: Robot) -> Robot {
  let direction = case robot.direction {
    North -> West
    East -> North
    South -> East
    West -> South
  }
  Robot(..robot, direction: direction)
}

fn advance(robot: Robot) -> Robot {
  let Position(x, y) = robot.position

  let position = case robot.direction {
    North -> Position(x, y + 1)
    East -> Position(x + 1, y)
    South -> Position(x, y - 1)
    West -> Position(x - 1, y)
  }
  Robot(..robot, position: position)
}

fn handle_instruction(robot: Robot, instruction: Instruction) -> Robot {
  case instruction {
    Right -> right(robot)
    Left -> left(robot)
    Advance -> advance(robot)
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
