# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 7: Some Assembly Required ---</h2><p>This year, Santa brought little Bobby Tables a set of wires and <a href="https://en.wikipedia.org/wiki/Bitwise_operation">bitwise logic gates</a>!  Unfortunately, little Bobby is a little under the recommended age range, and he needs help <span title="You had one of these as a kid, right?">assembling the circuit</span>.</p>
# MAGIC <p>Each wire has an identifier (some lowercase letters) and can carry a <a href="https://en.wikipedia.org/wiki/16-bit">16-bit</a> signal (a number from <code>0</code> to <code>65535</code>).  A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations.  A gate provides no signal until all of its inputs have a signal.</p>
# MAGIC <p>The included instructions booklet describes how to connect the parts together: <code>x AND y -&gt; z</code> means to connect wires <code>x</code> and <code>y</code> to an AND gate, and then connect its output to wire <code>z</code>.</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li><code>123 -&gt; x</code> means that the signal <code>123</code> is provided to wire <code>x</code>.</li>
# MAGIC <li><code>x AND y -&gt; z</code> means that the <a href="https://en.wikipedia.org/wiki/Bitwise_operation#AND">bitwise AND</a> of wire <code>x</code> and wire <code>y</code> is provided to wire <code>z</code>.</li>
# MAGIC <li><code>p LSHIFT 2 -&gt; q</code> means that the value from wire <code>p</code> is <a href="https://en.wikipedia.org/wiki/Logical_shift">left-shifted</a> by <code>2</code> and then provided to wire <code>q</code>.</li>
# MAGIC <li><code>NOT e -&gt; f</code> means that the <a href="https://en.wikipedia.org/wiki/Bitwise_operation#NOT">bitwise complement</a> of the value from wire <code>e</code> is provided to wire <code>f</code>.</li>
# MAGIC </ul>
# MAGIC <p>Other possible gates include <code>OR</code> (<a href="https://en.wikipedia.org/wiki/Bitwise_operation#OR">bitwise OR</a>) and <code>RSHIFT</code> (<a href="https://en.wikipedia.org/wiki/Logical_shift">right-shift</a>).  If, for some reason, you'd like to <em>emulate</em> the circuit instead, almost all programming languages (for example, <a href="https://en.wikipedia.org/wiki/Bitwise_operations_in_C">C</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators">JavaScript</a>, or <a href="https://wiki.python.org/moin/BitwiseOperators">Python</a>) provide operators for these gates.</p>
# MAGIC <p>For example, here is a simple circuit:</p>
# MAGIC <pre><code>123 -&gt; x
# MAGIC 456 -&gt; y
# MAGIC x AND y -&gt; d
# MAGIC x OR y -&gt; e
# MAGIC x LSHIFT 2 -&gt; f
# MAGIC y RSHIFT 2 -&gt; g
# MAGIC NOT x -&gt; h
# MAGIC NOT y -&gt; i
# MAGIC </code></pre>
# MAGIC <p>After it is run, these are the signals on the wires:</p>
# MAGIC <pre><code>d: 72
# MAGIC e: 507
# MAGIC f: 492
# MAGIC g: 114
# MAGIC h: 65412
# MAGIC i: 65079
# MAGIC x: 123
# MAGIC y: 456
# MAGIC </code></pre>
# MAGIC <p>In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to <em>wire <code>a</code></em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "lf AND lq -> ls
iu RSHIFT 1 -> jn
bo OR bu -> bv
gj RSHIFT 1 -> hc
et RSHIFT 2 -> eu
bv AND bx -> by
is OR it -> iu
b OR n -> o
gf OR ge -> gg
NOT kt -> ku
ea AND eb -> ed
kl OR kr -> ks
hi AND hk -> hl
au AND av -> ax
lf RSHIFT 2 -> lg
dd RSHIFT 3 -> df
eu AND fa -> fc
df AND dg -> di
ip LSHIFT 15 -> it
NOT el -> em
et OR fe -> ff
fj LSHIFT 15 -> fn
t OR s -> u
ly OR lz -> ma
ko AND kq -> kr
NOT fx -> fy
et RSHIFT 1 -> fm
eu OR fa -> fb
dd RSHIFT 2 -> de
NOT go -> gp
kb AND kd -> ke
hg OR hh -> hi
jm LSHIFT 1 -> kg
NOT cn -> co
jp RSHIFT 2 -> jq
jp RSHIFT 5 -> js
1 AND io -> ip
eo LSHIFT 15 -> es
1 AND jj -> jk
g AND i -> j
ci RSHIFT 3 -> ck
gn AND gp -> gq
fs AND fu -> fv
lj AND ll -> lm
jk LSHIFT 15 -> jo
iu RSHIFT 3 -> iw
NOT ii -> ij
1 AND cc -> cd
bn RSHIFT 3 -> bp
NOT gw -> gx
NOT ft -> fu
jn OR jo -> jp
iv OR jb -> jc
hv OR hu -> hw
19138 -> b
gj RSHIFT 5 -> gm
hq AND hs -> ht
dy RSHIFT 1 -> er
ao OR an -> ap
ld OR le -> lf
bk LSHIFT 1 -> ce
bz AND cb -> cc
bi LSHIFT 15 -> bm
il AND in -> io
af AND ah -> ai
as RSHIFT 1 -> bl
lf RSHIFT 3 -> lh
er OR es -> et
NOT ax -> ay
ci RSHIFT 1 -> db
et AND fe -> fg
lg OR lm -> ln
k AND m -> n
hz RSHIFT 2 -> ia
kh LSHIFT 1 -> lb
NOT ey -> ez
NOT di -> dj
dz OR ef -> eg
lx -> a
NOT iz -> ja
gz LSHIFT 15 -> hd
ce OR cd -> cf
fq AND fr -> ft
at AND az -> bb
ha OR gz -> hb
fp AND fv -> fx
NOT gb -> gc
ia AND ig -> ii
gl OR gm -> gn
0 -> c
NOT ca -> cb
bn RSHIFT 1 -> cg
c LSHIFT 1 -> t
iw OR ix -> iy
kg OR kf -> kh
dy OR ej -> ek
km AND kn -> kp
NOT fc -> fd
hz RSHIFT 3 -> ib
NOT dq -> dr
NOT fg -> fh
dy RSHIFT 2 -> dz
kk RSHIFT 2 -> kl
1 AND fi -> fj
NOT hr -> hs
jp RSHIFT 1 -> ki
bl OR bm -> bn
1 AND gy -> gz
gr AND gt -> gu
db OR dc -> dd
de OR dk -> dl
as RSHIFT 5 -> av
lf RSHIFT 5 -> li
hm AND ho -> hp
cg OR ch -> ci
gj AND gu -> gw
ge LSHIFT 15 -> gi
e OR f -> g
fp OR fv -> fw
fb AND fd -> fe
cd LSHIFT 15 -> ch
b RSHIFT 1 -> v
at OR az -> ba
bn RSHIFT 2 -> bo
lh AND li -> lk
dl AND dn -> do
eg AND ei -> ej
ex AND ez -> fa
NOT kp -> kq
NOT lk -> ll
x AND ai -> ak
jp OR ka -> kb
NOT jd -> je
iy AND ja -> jb
jp RSHIFT 3 -> jr
fo OR fz -> ga
df OR dg -> dh
gj RSHIFT 2 -> gk
gj OR gu -> gv
NOT jh -> ji
ap LSHIFT 1 -> bj
NOT ls -> lt
ir LSHIFT 1 -> jl
bn AND by -> ca
lv LSHIFT 15 -> lz
ba AND bc -> bd
cy LSHIFT 15 -> dc
ln AND lp -> lq
x RSHIFT 1 -> aq
gk OR gq -> gr
NOT kx -> ky
jg AND ji -> jj
bn OR by -> bz
fl LSHIFT 1 -> gf
bp OR bq -> br
he OR hp -> hq
et RSHIFT 5 -> ew
iu RSHIFT 2 -> iv
gl AND gm -> go
x OR ai -> aj
hc OR hd -> he
lg AND lm -> lo
lh OR li -> lj
da LSHIFT 1 -> du
fo RSHIFT 2 -> fp
gk AND gq -> gs
bj OR bi -> bk
lf OR lq -> lr
cj AND cp -> cr
hu LSHIFT 15 -> hy
1 AND bh -> bi
fo RSHIFT 3 -> fq
NOT lo -> lp
hw LSHIFT 1 -> iq
dd RSHIFT 1 -> dw
dt LSHIFT 15 -> dx
dy AND ej -> el
an LSHIFT 15 -> ar
aq OR ar -> as
1 AND r -> s
fw AND fy -> fz
NOT im -> in
et RSHIFT 3 -> ev
1 AND ds -> dt
ec AND ee -> ef
NOT ak -> al
jl OR jk -> jm
1 AND en -> eo
lb OR la -> lc
iu AND jf -> jh
iu RSHIFT 5 -> ix
bo AND bu -> bw
cz OR cy -> da
iv AND jb -> jd
iw AND ix -> iz
lf RSHIFT 1 -> ly
iu OR jf -> jg
NOT dm -> dn
lw OR lv -> lx
gg LSHIFT 1 -> ha
lr AND lt -> lu
fm OR fn -> fo
he RSHIFT 3 -> hg
aj AND al -> am
1 AND kz -> la
dy RSHIFT 5 -> eb
jc AND je -> jf
cm AND co -> cp
gv AND gx -> gy
ev OR ew -> ex
jp AND ka -> kc
fk OR fj -> fl
dy RSHIFT 3 -> ea
NOT bs -> bt
NOT ag -> ah
dz AND ef -> eh
cf LSHIFT 1 -> cz
NOT cv -> cw
1 AND cx -> cy
de AND dk -> dm
ck AND cl -> cn
x RSHIFT 5 -> aa
dv LSHIFT 1 -> ep
he RSHIFT 2 -> hf
NOT bw -> bx
ck OR cl -> cm
bp AND bq -> bs
as OR bd -> be
he AND hp -> hr
ev AND ew -> ey
1 AND lu -> lv
kk RSHIFT 3 -> km
b AND n -> p
NOT kc -> kd
lc LSHIFT 1 -> lw
km OR kn -> ko
id AND if -> ig
ih AND ij -> ik
jr AND js -> ju
ci RSHIFT 5 -> cl
hz RSHIFT 1 -> is
1 AND ke -> kf
NOT gs -> gt
aw AND ay -> az
x RSHIFT 2 -> y
ab AND ad -> ae
ff AND fh -> fi
ci AND ct -> cv
eq LSHIFT 1 -> fk
gj RSHIFT 3 -> gl
u LSHIFT 1 -> ao
NOT bb -> bc
NOT hj -> hk
kw AND ky -> kz
as AND bd -> bf
dw OR dx -> dy
br AND bt -> bu
kk AND kv -> kx
ep OR eo -> eq
he RSHIFT 1 -> hx
ki OR kj -> kk
NOT ju -> jv
ek AND em -> en
kk RSHIFT 5 -> kn
NOT eh -> ei
hx OR hy -> hz
ea OR eb -> ec
s LSHIFT 15 -> w
fo RSHIFT 1 -> gh
kk OR kv -> kw
bn RSHIFT 5 -> bq
NOT ed -> ee
1 AND ht -> hu
cu AND cw -> cx
b RSHIFT 5 -> f
kl AND kr -> kt
iq OR ip -> ir
ci RSHIFT 2 -> cj
cj OR cp -> cq
o AND q -> r
dd RSHIFT 5 -> dg
b RSHIFT 2 -> d
ks AND ku -> kv
b RSHIFT 3 -> e
d OR j -> k
NOT p -> q
NOT cr -> cs
du OR dt -> dv
kf LSHIFT 15 -> kj
NOT ac -> ad
fo RSHIFT 5 -> fr
hz OR ik -> il
jx AND jz -> ka
gh OR gi -> gj
kk RSHIFT 1 -> ld
hz RSHIFT 5 -> ic
as RSHIFT 2 -> at
NOT jy -> jz
1 AND am -> an
ci OR ct -> cu
hg AND hh -> hj
jq OR jw -> jx
v OR w -> x
la LSHIFT 15 -> le
dh AND dj -> dk
dp AND dr -> ds
jq AND jw -> jy
au OR av -> aw
NOT bf -> bg
z OR aa -> ab
ga AND gc -> gd
hz AND ik -> im
jt AND jv -> jw
z AND aa -> ac
jr OR js -> jt
hb LSHIFT 1 -> hv
hf OR hl -> hm
ib OR ic -> id
fq OR fr -> fs
cq AND cs -> ct
ia OR ig -> ih
dd OR do -> dp
d AND j -> l
ib AND ic -> ie
as RSHIFT 3 -> au
be AND bg -> bh
dd AND do -> dq
NOT l -> m
1 AND gd -> ge
y AND ae -> ag
fo AND fz -> gb
NOT ie -> if
e AND f -> h
x RSHIFT 3 -> z
y OR ae -> af
hf AND hl -> hn
NOT h -> i
NOT hn -> ho
he RSHIFT 5 -> hh
"

# COMMAND ----------

# input <- "123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# "

# COMMAND ----------

df <-
  tibble(instruction = read_lines(input)) %>%
  mutate(
    operation = case_when(
      str_detect(instruction, "^\\w+ ->") ~ "SET",
      str_detect(instruction, " AND ") ~ "AND",
      str_detect(instruction, " OR ") ~ "OR",
      str_detect(instruction, " LSHIFT ") ~ "LSHIFT",
      str_detect(instruction, " RSHIFT ") ~ "RSHIFT",
      str_detect(instruction, "^NOT ") ~ "NOT",
    ),
    a = str_extract(instruction, "^\\w+"),
    b = str_extract(instruction, "\\w+(?= ->)"),
    output_wire = str_extract(instruction, "\\w+$")
  )

df

# COMMAND ----------

cache <- list()

v <- function(wire) {
  if (!is.null(cache[[wire]])) {
    return(cache[[wire]])
  }
  value <- parse_number(wire) %>% suppressWarnings()
  if (!is.na(value)) {
    # message(glue::glue("Static: {value}"))
    return(value)
  }
  
  details <- df %>% filter(output_wire == wire)
  
  operation <- details$operation
  a <- details$a
  b <- details$b
  # output_wire <- details$output_wire
  # message(glue::glue("{a} {operation} {b} -> {wire}"))
  
  if (operation == "SET") {
    cache[[wire]] <<- v(b)
  } else if (operation == "AND") {
    cache[[wire]] <<- bitwAnd(v(a), v(b))
  } else if (operation == "OR") {
    cache[[wire]] <<- bitwOr(v(a), v(b))
  } else if (operation == "LSHIFT") {
    cache[[wire]] <<- bitwShiftL(v(a), v(b))
  } else if (operation == "RSHIFT") {
    cache[[wire]] <<- bitwShiftR(v(a), v(b))
  } else if (operation == "NOT") {
    cache[[wire]] <<- 65535 + bitwNot(v(b)) + 1
  }
  cache[[wire]]
}

# COMMAND ----------

answer <- v("a")
answer

# COMMAND ----------

# cache[order(names(cache))]

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, take the signal you got on wire <code>a</code>, override wire <code>b</code> to that signal, and reset the other wires (including wire <code>a</code>).  What new signal is ultimately provided to wire <code>a</code>?</p>
# MAGIC </article>

# COMMAND ----------

cache <- list(b = 16076)

# COMMAND ----------

answer <- v("a")
answer
