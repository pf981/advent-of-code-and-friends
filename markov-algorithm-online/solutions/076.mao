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

// "L}ba&bc" the "}ba" registers that "a" is the smaller letter
// converts it to a "X" which gets shot left. Then all the
// "a"s and smaller get deleted left-to-right
}a:a]
}b:b]
}c:c]
}&:&}
]a:X
]b:Y
]c:Z
]&:&}

// Shoot "X" left then replace with "A"
aX:Xa
bX:Xb
cX:Xc
&X:X&
LX:A

aY:Ya
bY:Yb
cY:Yc
&Y:Y&
LY:B

aZ:Za
bZ:Zb
cZ:Zc
&Z:Z&
LZ:C

// "A" means "a" is not the greateset so delete all "a"s
// and anything less than "a"
Aab:A
Aac:A
Aa:A
Ab:bA
Ac:cA
A&:&A

Bba:B
Bbc:B
Bb:B
Ba:aB
Bc:cB
B&:&B

Cca:C
Ccb:C
Cc:C
Ca:aC
Cb:bC
C&:&C

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