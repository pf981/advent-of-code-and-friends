import gleam/list
import gleam/int

pub type Pizza {
  Margherita
  Caprese
  Formaggio
  ExtraSauce(Pizza)
  ExtraToppings(Pizza)
}

fn pizza_price_impl(pizza: Pizza, acc: Int) -> Int {
  case pizza {
    Margherita -> acc + 7
    Caprese -> acc + 9
    Formaggio -> acc + 10
    ExtraSauce(p) -> pizza_price_impl(p, acc + 1)
    ExtraToppings(p) -> pizza_price_impl(p, acc + 2)
  }
}

pub fn pizza_price(pizza: Pizza) -> Int {
  pizza_price_impl(pizza, 0)
}

pub fn order_price(order: List(Pizza)) -> Int {
  let price =
    order
    |> list.map(pizza_price)
    |> int.sum()

  case list.length(order) {
    1 -> price + 3
    2 -> price + 2
    _ -> price
  }
}
