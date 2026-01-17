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

// Collected all characters, so append test
}t:t}

// Collect "s" and "e" into ">" and traverse right to find "tt"
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
t:no
