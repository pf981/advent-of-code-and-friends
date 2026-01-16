// Repeatedly delete the smaller number from the larger until one is zero

// "i" shifts left and spawns "j" which traverses right
// and changes next "o" to "x" on the RHS
jo:x
j|:|j
jx:xj

// RHS is smaller
j:<

// Similarly for </{
x<:<o
x|<:{o|
x{:{
i{:
    

// Consume "o" and spawn "j" from "i"
oi:ixj

// Spawn "i"
o|o:oi|o


// ">" keeps. Ie converts "x" to "o"
// "}" removes. Ie converts "x" to ""
// Flips from >/} when crosses middle. That is, it removes on
// one side and keeps on other
>x:o>
>|:|}
}x:}




// LHS is smaller
i:>



}:
{:
|::