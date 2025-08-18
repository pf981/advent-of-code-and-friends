

def md5(s: String): String =
  java
    .security
    .MessageDigest
    .getInstance("MD5")
    .digest(s.getBytes)
    .map("%02X".format(_))
    .mkString

def solve(prefix: String): Int =
  Stream // LazyList
    .from(1)
    .find(i => md5(input + i).startsWith(prefix))
    .get

val answer1: Int = solve("00000")
println(answer1)

val answer2: Int = solve("000000")
println(answer2)
