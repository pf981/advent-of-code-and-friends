// Shoot left
w<:<w
i<:<i

// At the far left, traverse right
// ">" takes an extra "w" and places it in the next correct spot
// "}" takes an extra "i" and places it in the next correct spot
<:>
>iw:iw>
>wi:iw
>ww:w>w
>ii:i}i
}ii:i}i
}iw:wi

// An invalid string must contain either "ww" or "ii".
// Shoot an arrow left to find the start of the invalid string
ww:<ww
ii:<ii