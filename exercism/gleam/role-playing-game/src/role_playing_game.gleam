import gleam/int
import gleam/option.{type Option, None, Some}

pub type Player {
  Player(name: Option(String), level: Int, health: Int, mana: Option(Int))
}

pub fn introduce(player: Player) -> String {
  option.unwrap(player.name, "Mighty Magician")
}

pub fn revive(player: Player) -> Option(Player) {
  case player {
    Player(health: 0, level: level, ..) if level >= 10 ->
      Some(Player(..player, health: 100, mana: Some(100)))
    Player(health: 0, ..) -> Some(Player(..player, health: 100))
    _ -> None
  }
}

pub fn cast_spell(player: Player, cost: Int) -> #(Player, Int) {
  case player {
    Player(mana: None, health: health, ..) -> #(
      Player(..player, health: int.max(health - cost, 0)),
      0,
    )
    Player(mana: Some(mana), ..) if mana >= cost -> #(
      Player(..player, mana: Some(mana - cost)),
      2 * cost,
    )
    _ -> #(player, 0)
  }
}
