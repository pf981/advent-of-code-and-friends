// Repeatedly delete the smaller number from the larger until one is zero

// "i" shifts left and spawns "j" which traverses right
// and changes next "o" to "x" on the RHS
jo:x
j|:|j
jx:xj

// RHS is smaller
j:<

// "<" keeps by converting "x" to "o" and shifting left
// "{" removes by converting "x" to "" and shifting left
// Flips from "<" to "{" when crosses middle
x<:<o
x|<:{o|
x{:{
i{:

// Consume "o" and spawn "j" from "i"
oi:ixj

// Spawn "i"
o|o:oi|o

// ">"/"}" similar to "<","{"
>x:o>
>|:|}
}x:}

// LHS is smaller
i:>

}:
{:
|::