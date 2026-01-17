// Patience sort
// {piles}|{cards}
// 321|4567

// Replace pile with card if the card is smaller.
// Otherwise, continue left to next pile.
1a:1
2a:1
3a:1
4a:1
5a:1
6a:1
7a:1
8a:1
9a:1

1b:b1
2b:2
3b:2
4b:2
5b:2
6b:2
7b:2
8b:2
9b:2

1c:c1
2c:c2
3c:3
4c:3
5c:3
6c:3
7c:3
8c:3
9c:3

1d:d1
2d:d2
3d:d3
4d:4
5d:4
6d:4
7d:4
8d:4
9d:4

1e:e1
2e:e2
3e:e3
4e:e4
5e:5
6e:5
7e:5
8e:5
9e:5

1f:f1
2f:f2
3f:f3
4f:f4
5f:f5
6f:6
7f:6
8f:6
9f:6

1g:g1
2g:g2
3g:g3
4g:g4
5g:g5
6g:g6
7g:7
8g:7
9g:7

1h:h1
2h:h2
3h:h3
4h:h4
5h:h5
6h:h6
7h:h7
8h:8
9h:8

1i:i1
2i:i2
3i:i3
4i:i4
5i:i5
6i:i6
7i:i7
8i:i8
9i:9

// If card reaches left, create new pile
a:1
b:2
c:3
d:4
e:5
f:6
g:7
h:8
i:9

// Pop card. Represent as lowercase letter.
|1:a|
|2:b|
|3:c|
|4:d|
|5:e|
|6:f|
|7:g|
|8:h|
|9:i|

// Count piles
1|:|o
2|:|o
3|:|o
4|:|o
5|:|o
6|:|o
7|:|o
8|:|o
9|:|o
|ooooooooo::9
|oooooooo::8
|ooooooo::7
|oooooo::6
|ooooo::5
|oooo::4
|ooo::3
|oo::2
|o::1

:|