// a<b&c>b&b>a
// ba&cb&ba
//
// Get the first available second (smaller) element.
// Pull it to the far left and iterate from left to right.
// Delete all elements <= that element.
// Continue until only one element is remaining.

// Swap "a<b" and "b>a" to "ba"
a<b:ba
a<c:ca
b<a:ab
b<c:cb
c<a:ac
c<b:bc
>:

// Shoot "x" left then replace with "A"
ax:xa
bx:xb
cx:xc
&x:x&
Lx:A

ay:ya
by:yb
cy:yc
&y:y&
Ly:B

az:za
bz:zb
cz:zc
&z:z&
Lz:C

// "A" means "a" is not the greateset so delete all "a"s
// and anything less than "a"
}a:a]
}b:b]
}c:c]
}&:&}
]a:x
]b:y
]c:z
]&:&}


// "X" means delete everything until "&" then return to "A"
// "X" -> "A"
// "Y" -> "B"
// "Z" -> "C"
Aa:X
Ab:bA
Ac:cA
A&:&A

Ba:aB
Bb:Y
Bc:cB
B&:&B

Ca:aC
Cb:bC
Cc:Z
C&:&C

Xa:X
Xb:X
Xc:X
X&:&A

Ya:Y
Yb:Y
Yc:Y
Y&:&B

Za:Z
Zb:Z
Zc:Z
Z&:&C

X:
Y:
Z:
L:D

// Clear
aa:a
bb:b
cc:c
Da:aD
Db:bD
Dc:cD
D&:D
D}:D
D]:D
DA:D
DB:D
DC:D
D::

:L}