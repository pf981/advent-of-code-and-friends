import gleam/float
import gleam/list
import gleam/order.{type Order}

pub type City {
  City(name: String, temperature: Temperature)
}

pub type Temperature {
  Celsius(Float)
  Fahrenheit(Float)
}

pub fn fahrenheit_to_celsius(f: Float) -> Float {
  { f -. 32.0 } /. 1.8
}

pub fn compare_temperature(left: Temperature, right: Temperature) -> Order {
  let l_celcius = case left {
    Fahrenheit(f) -> fahrenheit_to_celsius(f)
    Celsius(c) -> c
  }
  let r_celcius = case right {
    Fahrenheit(f) -> fahrenheit_to_celsius(f)
    Celsius(c) -> c
  }
  float.compare(l_celcius, r_celcius)
}

pub fn sort_cities_by_temperature(cities: List(City)) -> List(City) {
  list.sort(cities, by: fn(a, b) {
    compare_temperature(a.temperature, b.temperature)
  })
}
