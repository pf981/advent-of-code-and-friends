import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/result
import gleam/string

const header = "Team                           | MP |  W |  D |  L |  P"

type Stats {
  Stats(matches: Int, wins: Int, draws: Int, losses: Int, points: Int)
}

fn update_stats(stats: Stats, outcome: String) -> Stats {
  let Stats(matches, wins, draws, losses, points) = stats
  case outcome {
    "win" -> Stats(matches + 1, wins + 1, draws, losses, points + 3)
    "loss" -> Stats(matches + 1, wins, draws, losses + 1, points)
    "draw" -> Stats(matches + 1, wins, draws + 1, losses, points + 1)
    _ -> panic
  }
}

fn parse_line(stats: Dict(String, Stats), line: String) -> Dict(String, Stats) {
  case string.split(line, ";") {
    [team1, team2, outcome] -> {
      string.split(line, ";")

      let team1_stats =
        stats
        |> dict.get(team1)
        |> result.unwrap(Stats(0, 0, 0, 0, 0))
        |> update_stats(outcome)

      let team2_stats =
        stats
        |> dict.get(team2)
        |> result.unwrap(Stats(0, 0, 0, 0, 0))
        |> update_stats(case outcome {
          "win" -> "loss"
          "loss" -> "win"
          outcome -> outcome
        })

      stats
      |> dict.insert(team1, team1_stats)
      |> dict.insert(team2, team2_stats)
    }
    _ -> stats
  }
}

fn to_string(team_name: String, stats: Stats) -> String {
  let stats_str =
    [stats.matches, stats.wins, stats.draws, stats.losses, stats.points]
    |> list.map(int.to_string)
    |> list.map(string.pad_left(_, 3, " "))
  string.join([string.pad_right(team_name, 30, " "), ..stats_str], " |")
}

pub fn tally(input: String) -> String {
  input
  |> string.split("\n")
  |> list.fold(dict.new(), parse_line)
  |> dict.to_list()
  |> list.sort(fn(a, b) {
    case a, b {
      #(_, Stats(_, _, _, _, points1)), #(_, Stats(_, _, _, _, points2))
        if points1 != points2
      -> int.compare(points2, points1)
      #(name1, Stats(..)), #(name2, Stats(..)) -> string.compare(name1, name2)
    }
  })
  |> list.map(fn(tuple) { to_string(tuple.0, tuple.1) })
  |> fn(l) { [header, ..l] }
  |> string.join("\n")
}
