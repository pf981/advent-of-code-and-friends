import gleam/bool
import gleam/list
import gleam/result

type MiddleState {
  Strike
  Spare(roll1: Int)
  Open(roll1: Int, roll2: Int)
}

type LastState {
  LastStrike(bonus1: Int, bonus2: Int)
  LastSpare(roll1: Int, bonus: Int)
  LastOpen(roll1: Int, roll2: Int)
}

type PendingState {
  PendingMiddle(roll1: Int)
  PendingLast(roll1: Int)
  PendingLastSpare(roll1: Int)
  PendingLastStrike
  PendingLastStrike2(bonus1: Int)
}

pub opaque type Frame {
  Middle(state: MiddleState)
  Last(state: LastState)
  Pending(state: PendingState)
}

pub type Game {
  Game(frames: List(Frame))
}

pub type Error {
  InvalidPinCount
  GameComplete
  GameNotComplete
}

fn new_frame(game: Game, knocked_pins: Int) -> Game {
  case list.length(game.frames), knocked_pins == 10 {
    9, True -> Game([Pending(PendingLastStrike), ..game.frames])
    9, False -> Game([Pending(PendingLast(knocked_pins)), ..game.frames])
    _, True -> Game([Middle(Strike), ..game.frames])
    _, False -> Game([Pending(PendingMiddle(knocked_pins)), ..game.frames])
  }
}

fn update_frame(
  game: Game,
  frame: PendingState,
  knocked_pins: Int,
) -> Result(Game, Error) {
  let new_frame: Result(Frame, Error) = case frame {
    PendingMiddle(roll1) ->
      case roll1 + knocked_pins {
        10 -> Ok(Middle(Spare(roll1)))
        total if total > 10 -> Error(InvalidPinCount)
        _ -> Ok(Middle(Open(roll1, knocked_pins)))
      }
    PendingLast(roll1) ->
      case roll1 + knocked_pins {
        10 -> Ok(Pending(PendingLastSpare(roll1)))
        total if total > 10 -> Error(InvalidPinCount)
        _ -> Ok(Last(LastOpen(roll1, knocked_pins)))
      }
    PendingLastSpare(roll1) -> Ok(Last(LastSpare(roll1, knocked_pins)))
    PendingLastStrike -> Ok(Pending(PendingLastStrike2(knocked_pins)))
    PendingLastStrike2(bonus1) ->
      case bonus1 == 10 || bonus1 + knocked_pins <= 10 {
        True -> Ok(Last(LastStrike(bonus1, knocked_pins)))
        False -> Error(InvalidPinCount)
      }
  }

  new_frame
  |> result.map(fn(f) { Game([f, ..game.frames]) })
}

pub fn roll(game: Game, knocked_pins: Int) -> Result(Game, Error) {
  use <- bool.guard(
    knocked_pins < 0 || knocked_pins > 10,
    Error(InvalidPinCount),
  )

  case game.frames {
    [Last(..), ..] -> Error(GameComplete)
    [Middle(..), ..] | [] -> Ok(new_frame(game, knocked_pins))
    [Pending(pending_state), ..rest] ->
      update_frame(Game(rest), pending_state, knocked_pins)
  }
}

fn score_impl(
  frames: List(Frame),
  next_roll: Int,
  next_roll2: Int,
  acc: Int,
) -> Int {
  case frames {
    [] -> acc
    [frame, ..rest] -> {
      case frame {
        Middle(Strike) ->
          score_impl(rest, 10, next_roll, acc + 10 + next_roll + next_roll2)
        Middle(Spare(roll1)) ->
          score_impl(rest, roll1, 10 - roll1, acc + 10 + next_roll)
        Middle(Open(roll1, roll2)) | Last(LastOpen(roll1, roll2)) ->
          score_impl(rest, roll1, roll2, acc + roll1 + roll2)
        Last(LastStrike(bonus1, bonus2)) ->
          score_impl(rest, 10, bonus1, acc + 10 + bonus1 + bonus2)
        Last(LastSpare(roll1, bonus)) ->
          score_impl(rest, roll1, bonus, acc + 10 + bonus)
        _ -> panic
      }
    }
  }
}

pub fn score(game: Game) -> Result(Int, Error) {
  case game.frames {
    [Last(..), ..] -> Ok(score_impl(game.frames, 0, 0, 0))
    _ -> Error(GameNotComplete)
  }
}
