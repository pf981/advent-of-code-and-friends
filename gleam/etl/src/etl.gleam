import gleam/dict.{type Dict}
import gleam/list
import gleam/string

pub fn transform(legacy: Dict(Int, List(String))) -> Dict(String, Int) {
  dict.fold(legacy, dict.new(), fn(acc, key, values) {
    list.fold(values, acc, fn(acc, value) {
      dict.insert(acc, string.lowercase(value), key)
    })
  })
}
