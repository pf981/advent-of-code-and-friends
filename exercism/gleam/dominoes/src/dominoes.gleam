import gleam/bool
import gleam/list
import gleam/queue.{type Queue}

fn can_chain_impl(
  chain: Queue(#(Int, Int)),
  start: Int,
  end: Int,
  attempt: Int,
  limit: Int,
) -> Bool {
  use <- bool.guard(attempt == limit, False)

  let try_next = fn(q, first) {
    can_chain_impl(queue.push_back(q, first), start, end, attempt + 1, limit)
  }

  case queue.pop_front(chain) {
    Ok(#(first, q)) if first.0 == start ->
      can_chain_impl(q, first.1, end, 0, limit) || try_next(q, first)
    Ok(#(first, q)) if first.1 == start ->
      can_chain_impl(q, first.0, end, 0, limit) || try_next(q, first)
    Ok(#(first, q)) -> try_next(q, first)
    Error(Nil) -> start == end
  }
}

pub fn can_chain(chain: List(#(Int, Int))) -> Bool {
  case chain {
    [] -> True
    [first, ..rest] ->
      can_chain_impl(
        queue.from_list(rest),
        first.0,
        first.1,
        0,
        list.length(chain),
      )
  }
}
