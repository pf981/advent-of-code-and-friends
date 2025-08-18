import gleam/float
import gleam/int
import gleam/iterator
import gleam/pair

pub type Character {
  Character(
    charisma: Int,
    constitution: Int,
    dexterity: Int,
    hitpoints: Int,
    intelligence: Int,
    strength: Int,
    wisdom: Int,
  )
}

pub fn generate_character() -> Character {
  let constitution = ability()

  Character(
    charisma: ability(),
    constitution: constitution,
    dexterity: ability(),
    hitpoints: 10 + modifier(constitution),
    intelligence: ability(),
    strength: ability(),
    wisdom: ability(),
  )
}

pub fn modifier(score: Int) -> Int {
  float.floor({ int.to_float(score) -. 10.0 } /. 2.0)
  |> float.truncate
}

pub fn ability() -> Int {
  iterator.repeatedly(fn() { 1 + int.random(6) })
  |> iterator.take(4)
  |> iterator.fold(#(0, 7), fn(pair, roll) {
    let #(acc, lowest) = pair
    case roll < lowest {
      True if lowest == 7 -> #(acc, roll)
      True -> #(acc + lowest, roll)
      False -> #(acc + roll, lowest)
    }
  })
  |> pair.first
}
