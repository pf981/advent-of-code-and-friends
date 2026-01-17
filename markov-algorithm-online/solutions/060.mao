// 101011n111110n110010n
// |>n101011n111110n110010n
// 1|Bn>01011n111110n110010n
// ...
// 1|n01011>n111110n110010n
// 1|n01011Bn>11110n110010n
// ...
// 1|Bn01011n>11110n110010n
// 11|n01011n>11110n110010n
// ...
// 111|n01011n>11110n10010>n
// 111|n01011n>11110n10010Nn
// ...
// 111|Nn01011n>11110n10010n
// 111n|n01011n>11110n10010n

// Shoot popped element back
nA:An
0A:A0
1A:A1
|A:0|

nB:Bn
0B:B0
1B:B1
|B:1|

nN:Nn
0N:N0
1N:N1
|N:n|

// Pop first element of row
>n0:An>
>n1:Bn>

// When reached end, shoot n back
>n:Nn

>0:0>
>1:1>

// Terminate
nn|n:nn|
nn|::n

|:|>

:|>n