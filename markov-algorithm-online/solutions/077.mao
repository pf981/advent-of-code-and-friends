// "1st" if xor is non-zero, "2nd" otherwise

// Clear
0<:<
1<:<
2<:<
3<:<
4<:<
o<:<

>0:>
>1:>
>2:>
>3:>
>4:>
>o:>

<:
>::


// Sort and cancel
00:

10:01
11:

20:02
21:12
22:

30:03
31:13
32:23
33:

40:04
41:14
42:24
43:34
44:


// Get powers of 2
oooooooooooooooooooooooooooooooo:<1st>
oooooooooooooooo:4
oooooooo:3
oooo:2
oo:1
o:0

|:

// Remaining means xor is non-zero so 1st wins
0:<1st>
1:<1st>
2:<1st>
3:<1st>
4:<1st>

// Nothing left means xor is 0 so 2nd wins
::2nd