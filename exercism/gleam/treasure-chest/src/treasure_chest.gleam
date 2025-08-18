// Please define the TreasureChest generic custom type
pub type TreasureChest(a) {
  TreasureChest(password: String, contents: a)
}

pub type UnlockResult(a) {
  Unlocked(contents: a)
  WrongPassword
}

pub fn get_treasure(
  chest: TreasureChest(treasure),
  password: String,
) -> UnlockResult(treasure) {
  case chest {
    TreasureChest(actual, contents) if password == actual -> Unlocked(contents)
    _ -> WrongPassword
  }
}
