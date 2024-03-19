pub opaque type Set(t) {
  Set(l: List(t))
}

pub fn new(members: List(t)) -> Set(t) {
  Set(members)
}

pub fn is_empty(set: Set(t)) -> Bool {
  case set {
    Set([]) -> True
    _ -> False
  }
}

pub fn contains(in set: Set(t), this member: t) -> Bool {
  case set {
    Set([]) -> False
    Set([first, ..rest]) -> first == member || contains(Set(rest), member)
  }
}

pub fn is_subset(first: Set(t), of second: Set(t)) -> Bool {
  case first {
    Set([]) -> True
    Set([head, ..rest]) ->
      contains(second, head) && is_subset(Set(rest), second)
  }
}

pub fn disjoint(first: Set(t), second: Set(t)) -> Bool {
  intersection(first, second)
  |> is_empty
}

pub fn is_equal(first: Set(t), to second: Set(t)) -> Bool {
  is_subset(first, second) && is_subset(second, first)
}

pub fn add(to set: Set(t), this member: t) -> Set(t) {
  case contains(set, member) {
    True -> set
    False -> Set([member, ..set.l])
  }
}

pub fn intersection(of first: Set(t), and second: Set(t)) -> Set(t) {
  case first {
    Set([]) -> Set([])
    Set([head, ..rest]) ->
      case contains(second, head) {
        False -> intersection(Set(rest), second)
        True -> union(Set([head]), intersection(Set(rest), second))
      }
  }
}

pub fn difference(between first: Set(t), and second: Set(t)) -> Set(t) {
  case first {
    Set([]) -> Set([])
    Set([head, ..rest]) ->
      case contains(second, head) {
        True -> difference(Set(rest), second)
        False -> union(Set([head]), difference(Set(rest), second))
      }
  }
}

// pub fn difference(between first: Set(t), and second: Set(t)) -> Set(t) {
//   case second {
//     Set([]) -> Set([])
//     Set([head, ..rest]) ->
//       case contains(first, head) {
//         True -> intersection(Set(rest), first)
//         False -> union(Set([head]), intersection(Set(rest), first))
//       }
//   }
// }

pub fn union(of first: Set(t), and second: Set(t)) -> Set(t) {
  case first {
    Set([]) -> second
    Set([head, ..rest]) ->
      case contains(second, head) {
        True -> union(Set(rest), second)
        False -> union(Set(rest), Set([head, ..second.l]))
      }
  }
}
