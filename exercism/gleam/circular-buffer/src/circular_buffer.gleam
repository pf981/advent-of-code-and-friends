import gleam/queue.{type Queue}

pub opaque type CircularBuffer(t) {
  CircularBuffer(q: Queue(t), size: Int, capacity: Int)
}

pub fn new(capacity: Int) -> CircularBuffer(t) {
  CircularBuffer(queue.new(), 0, capacity)
}

pub fn read(buffer: CircularBuffer(t)) -> Result(#(t, CircularBuffer(t)), Nil) {
  case queue.pop_front(buffer.q) {
    Ok(#(first, rest)) ->
      Ok(#(first, CircularBuffer(rest, buffer.size - 1, buffer.capacity)))
    Error(Nil) -> Error(Nil)
  }
}

pub fn write(
  buffer: CircularBuffer(t),
  item: t,
) -> Result(CircularBuffer(t), Nil) {
  case buffer.size == buffer.capacity {
    True -> Error(Nil)
    False ->
      Ok(CircularBuffer(
        queue.push_back(buffer.q, item),
        buffer.size + 1,
        buffer.capacity,
      ))
  }
}

pub fn overwrite(buffer: CircularBuffer(t), item: t) -> CircularBuffer(t) {
  case buffer.size == buffer.capacity {
    True ->
      case queue.pop_front(buffer.q) {
        Ok(#(_, rest)) ->
          CircularBuffer(
            queue.push_back(rest, item),
            buffer.size,
            buffer.capacity,
          )
        Error(Nil) -> panic
      }
    False ->
      CircularBuffer(
        queue.push_back(buffer.q, item),
        buffer.size + 1,
        buffer.capacity,
      )
  }
}

pub fn clear(buffer: CircularBuffer(t)) -> CircularBuffer(t) {
  CircularBuffer(queue.new(), 0, buffer.capacity)
}
