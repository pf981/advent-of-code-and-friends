// Final conversion to "est"
X}:estX
X::

// Sort
es:se
ts:st
te:et

// Traverse right to find "t" to complete "est"
>e:e>
>t:}

// Collected "est" at the end represented by "}"
}t:t}

// Collect "s" and "e" into ">" and traverse right to find "t"
se:>

// Clear
sno:no
eno:no
nos:no
noe:no
not:no
no}:no
no>:no

// Terminal conditions
e:no
s:no
tt:no
>:no
t}:testX
t::t
}:no
