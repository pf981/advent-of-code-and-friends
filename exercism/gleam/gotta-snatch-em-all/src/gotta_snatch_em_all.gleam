import gleam/list
import gleam/result
import gleam/set.{type Set}
import gleam/string

pub fn new_collection(card: String) -> Set(String) {
  set.new()
  |> set.insert(card)
}

pub fn add_card(collection: Set(String), card: String) -> #(Bool, Set(String)) {
  case set.contains(collection, card) {
    True -> #(True, collection)
    False -> #(False, set.insert(collection, card))
  }
}

pub fn trade_card(
  my_card: String,
  their_card: String,
  collection: Set(String),
) -> #(Bool, Set(String)) {
  let worth_doing =
    set.contains(collection, my_card) && !set.contains(collection, their_card)
  #(
    worth_doing,
    collection
      |> set.delete(my_card)
      |> set.insert(their_card),
  )
}

pub fn boring_cards(collections: List(Set(String))) -> List(String) {
  collections
  |> list.reduce(fn(acc, collection) { set.intersection(acc, collection) })
  |> result.unwrap(set.new())
  |> set.to_list()
  |> list.sort(string.compare)
}

pub fn total_cards(collections: List(Set(String))) -> Int {
  collections
  |> list.fold(set.new(), fn(acc, collection) { set.union(acc, collection) })
  |> set.size()
}

pub fn shiny_cards(collection: Set(String)) -> Set(String) {
  set.filter(collection, string.starts_with(_, "Shiny"))
}
