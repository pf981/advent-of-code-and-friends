val answer1 =
  input
    .split("\n")
    .map(s =>
      s.length() - raw"""\\\\|\\"|\\x..|.""".r.findAllIn(s.replaceAll("^\"|\"$", "")).length
    )
    .sum
println(answer1)

val answer2 =
  input
    .split("\n")
    .map(s => "\"".r.findAllIn(s).length + raw"\\".r.findAllIn(s).length + 2)
    .sum
println(answer2)
