// Clear
xBINGO!:BINGO!
oBINGO!:BINGO!
BINGO!x:BINGO!
BINGO!o:BINGO!
OBINGO!:BINGO!
XBINGO!:BINGO!
[BINGO!:BINGO!
#BINGO!:BINGO!
*BINGO!:BINGO!
BINGO!#:BINGO!
BINGO!*:BINGO!
BINGO![:BINGO!
BINGO!|:BINGO!
|BINGO!:BINGO!

// Horizontal
|ooooo:BINGO!
ooooo|:BINGO!

|:

// Mismatch template
#x:<x
X<:<x
O<:<o
*<:<
#<:<
[<:

// Match template
*x:X
*o:O
#o:O
// Pass through elements already used by current template (capitals)
*X:X*
*O:O*
#X:X#
#O:O#
[X:X[
[O:O[

// Template reaches the end
[:BINGO!

// Terminal states
LBINGO!::BINGO!
Lo:L
Lx:L
L::;_;

// Prefix with template where
//   "#" - o
//   "*" - "o" or "x"
//   "[" - Start of template

:L[#*****#*****#*****#*****#[****#***#***#***#***#****[#****#****#****#****#****[*#****#****#****#****#***[**#****#****#****#****#**[***#****#****#****#****#*[****#****#****#****#****#
