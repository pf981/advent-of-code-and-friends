// 1. Add even-positioned digits and subtract odd
// 2. Repeat until you get 1 digit
// 3. If and only if that digit is 0, then the number is divisible by 11
//
// 132968
// }>132968
// }>132968
// }Xv>32968
// }Xv>32968
// }XvXXXv>2968
// }XvXXXv>2968
// }XxvXXv>2968
// }XxvXXv>2968
// }vXXv>2968
// }vXXv>2968
// }xvXv>2968
// }xvXv>2968
// }xxvv>2968
// }xxvv>2968
// }xx>2968
// ...
// }xxxxxxxxxxx>
// ...
// xxxxxxxxxxx}>
// yes

xX:
Xx:

vX:xv
vv:

>0:v>
>1:Xv>
>2:XXv>
>3:XXXv>
>4:XXXXv>
>5:XXXXXv>
>6:XXXXXXv>
>7:XXXXXXXv>
>8:XXXXXXXXv>
>9:XXXXXXXXXv>

// "}" converts "X" to "x"
}X:x}
}x:x}

// Chop off groups of 11
xxxxxxxxxxx}>:}>
v:
x}>:no
}>:yes
xyes:no
yes::yes
xno:no
no::no

:}>