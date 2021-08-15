# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/24

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 24: Lobby Layout ---</h2><p>Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.</p>
# MAGIC <p>As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the <em>new tile floor</em>.</p>
# MAGIC <p>The tiles are all <em>hexagonal</em>; they need to be arranged in a <a href="https://en.wikipedia.org/wiki/Hexagonal_tiling">hex grid</a> with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.</p>
# MAGIC <p>The tiles are all <em>white</em> on one side and <em>black</em> on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.</p>
# MAGIC <p>A member of the renovation crew gives you a <em>list of the tiles that need to be flipped over</em> (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a <em>reference tile</em> in the very center of the room. (Every line starts from the same reference tile.)</p>
# MAGIC <p>Because the tiles are hexagonal, every tile has <em>six neighbors</em>: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as <code>e</code>, <code>se</code>, <code>sw</code>, <code>w</code>, <code>nw</code>, and <code>ne</code>. A tile is identified by a series of these directions with <em>no delimiters</em>; for example, <code>esenee</code> identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.</p>
# MAGIC <p>Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like <code>esew</code> flips a tile immediately adjacent to the reference tile, and a line like <code>nwwswee</code> flips the reference tile itself.</p>
# MAGIC <p>Here is a larger example:</p>
# MAGIC <pre><code>sesenwnenenewseeswwswswwnenewsewsw
# MAGIC neeenesenwnwwswnenewnwwsewnenwseswesw
# MAGIC seswneswswsenwwnwse
# MAGIC nwnwneseeswswnenewneswwnewseswneseene
# MAGIC swweswneswnenwsewnwneneseenw
# MAGIC eesenwseswswnenwswnwnwsewwnwsene
# MAGIC sewnenenenesenwsewnenwwwse
# MAGIC wenwwweseeeweswwwnwwe
# MAGIC wsweesenenewnwwnwsenewsenwwsesesenwne
# MAGIC neeswseenwwswnwswswnw
# MAGIC nenwswwsewswnenenewsenwsenwnesesenew
# MAGIC enewnwewneswsewnwswenweswnenwsenwsw
# MAGIC sweneswneswneneenwnewenewwneswswnese
# MAGIC swwesenesewenwneswnwwneseswwne
# MAGIC enesenwswwswneneswsenwnewswseenwsese
# MAGIC wnwnesenesenenwwnenwsewesewsesesew
# MAGIC nenewswnwewswnenesenwnesewesw
# MAGIC eneswnwswnwsenenwnwnwwseeswneewsenese
# MAGIC neswnwewnwnwseenwseesewsenwsweewe
# MAGIC wseweeenwnesenwwwswnew
# MAGIC </code></pre>
# MAGIC <p>In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of <em><code>10</code></em> tiles are <em>black</em>.</p>
# MAGIC <p>Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, <em>how many tiles are left with the black side up?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "eeeseswneenwnwenwseeeee
swswnwswswneswswneeswswswswseswsww
sweswwnwseswnwewnwseewseeneneswww
swnwsweseneenweeseswseseeswseenese
nwsenwsewnesenenwnenwnwnewnwswwwswne
ewseeeeeswnee
nenwwwwwnwwwnewwwsewnwwswwww
neneeenenwnenwnesweneneeswneneenee
wnewsewwswnwswwsew
seswseseswnwseseseeseseswswswswseswswswnwse
swwweswweswseswseneseseseswseneswse
weeswnwswnenwseenenweswnwwenwnwwsw
seseeseneseeeeseseseewnwseeeesee
seseswseswseswseseeseseswsesewneseswsese
eseeeenenewneeneew
neneswswswnwswenwesewswwswwswswwe
nwnwnwnwnwnwneswnwnenenenwnw
wseseseseweseseweeseenese
wswwwswwwwnwswnwseswwnewwwswsew
eswnweneeesweenweeenweeeswwe
seseseseseseeseswseseseeseeseeneee
swsenwseseeeseseeseneswsewseeseesese
nwneswwnenwneneneneneneneenwsenenwneenenw
swswswsweswswswswswswswswswswswswswwsw
swswnwseswswswwswwwwswswsw
wnewseswwswwwwswwenwwswswwwwwsw
seseswsweseseswseswseswswseenwswsewswswsw
seseneseswseswswseswswsesenwseneneswsew
nwnwnenwnwnenenwsenwnwnwnenwnwenwnwnwnwsw
sweeeeneeneeneneneeneneene
nenenesweeneeeeneeneneneneenwnene
swnwneneneswenenesewnenene
neeneeenenenenenenesweneneeneee
nweesesesesweseseseesesewsesesesesese
seseseneseesesesenwswsesesesesesesesesese
neseswseesesenwseswseneeseseseneseseswsw
nwnwnwwwsenenenwseswnwnwnenwnenwnesenwsese
neswsewswswswswswswswswwswswswswwwsww
nwnwnwnwnwwnwnwswwnwwewnwwwwww
nenwswneswnenenenwneneswnenenenwnesenwnenee
sesesesesewseseswseseseseseseesesesese
eeeneswesenwneseeeneneneneeewne
neseswnesesenwseseswsesewseweseswese
seseseneseswseseseswsesesesesewsesesesenw
seswswnenwseseneseenwsesese
neswwwnwsenenwwnewwnwsenewswnwww
neneswneswnwswnwwswseswswswwswwswswesw
nwnwneenwnwnwnwwwnwswnwnwenenwnenenw
nwwwnwwnwnwseseenwnwwnwnwnwnwwsenw
nwnwnwsenwnwnwnenwnwnwnwnwnwnenenwnenenw
sweseswenwseewnweeeseenesenwsee
nenenenenenenenenwneseneeneneneneswnenene
wswswsweenweenwneswswnwnwnwneseew
swswswnwswsweswwswswswswswseeswswswsww
nwnwnwnwnwnwnwnenenenwnwnwnwwnwnwnwsene
wewwswnwnwswwnwwnwwnenwwewnwnwnw
nweeeeeeeeeeeswneseneeseew
wwwwewwwnwwnwnwnwswnwwwww
wwnwwwwwwwwwwwwwewseww
nenwnenwnenewnwnenwnenenwnenwnenenenwnwse
swswswswseseswnewwnwswswswwneswswnew
ewwwwnwwwwwwwwwwwwswwww
senesesewwswswnwwneeww
wnwswnwewewswwseeswwwwenww
weenenwwwsewneneneseeswneseesenesw
seseswwneswswesewswswwsweswnwnwswnwne
nenenenenenenenenenenenenenenenenwneswne
nwnewnwnwnenwsenenwnenwnwsewnenwnenene
nenwswenwnwwnwwnwneseenwnenwsenenesene
nenwwwnwswnwwseenwnwwsewnwwwwnww
wseswswswseseneswenewenwseseneswswwnw
neneneneswenenenewnenenenwneneeneene
nwnenwnwnenenenenenwnwnwneeneswnw
newnenwnewseneneneeneneseneneneneew
wnwnwwnenwnwswwnwwnwnwnwnwwnesewnww
eneneneenenwwneneeneneneswnenenenenene
sweenwnesenewswwswwswwsewwswnwswsenw
swwswnwwswwseseswwswswnwswswswswnwswse
swseneseeeeesewseesese
swwswswswewsweneswswswseswswwnewseswsw
sesesenwweneseneseswneswwwesesesee
wnwnwnwnwswwwsenwnewnwwnwnwenwwwse
nwnwwnwnwnwnwenwnwnwswnenwnwnwnwnwwse
swseeseseeeeeeeeeenweeeesee
neseneneeenewnenenwswwneseneeswneswnw
neeneeeneneeseneeneewneweneeee
seseswswswseseseswsenew
eeeeseeeeseenweeesweseseenwe
ewenwseswneneeenwseswwnwnwweswe
swwnwnwwsewneswnenwewnwwnwsenwnesw
nwnwnwnweneeneseesewwwswnwswnwneee
swswwwwswswneswseweewwnwwwswwswsw
neneneneneneneneneneneneneneneneneneswne
swseswseswswseseseswswswseswsewsesenenwsw
neswnwswseswswswseswwswwswwneswswswswsw
weneneneneeeeenwneneewneeneeese
nenenenwnwnenwneneneswnenwnwneenwnenwne
sweseweneseswnwnwenesenenwnenwnwwnenene
ewewsweswweswswswnesenwneswnwsew
seseseseseseseseseseseseseneseseseseswsew
nwnwswnwnwnwnenwnenwnwnwnenwnwenwnwnwnwnw
nwnwsesenwnwnwnwnwnwneswnesewnwsenwnww
neenenwnenenwwnwnenenenenwnwnenenwnene
nenwneenwwneseneneswneseseneenewnenese
sewnwswseswnenewwwwseweswwwnww
enwnwneswnwnwnwnwnwnwnwnwnwnwnwwnwnwnwe
neneeneneneewseneeneeneneneenenene
swseseeswseswswswswswseswswswswswswsww
nwseseenwswswwswsenenweswnewswnwswe
wswwwwwwwwswnwswwswwswwwew
eeeneeeenweeneneeenesene
eenwnewswswwswswnwnwswenewnenwnwse
neneeneneneenenewnenenenenenenenee
neesenwnwseswseeeseesesewesesewee
nwnwnwnwenwnenenenenewne
eswnwsenewwnweswwnwsewwwnwwnenew
swswswswswswsewswswseswseswseseswneswswse
seneeneneenwneenwsenenewnenesenenene
swswswswswwswwswswswneeswswswnwseswwwsw
ewwnenwneswswswswneswneenewswse
seswnwnwnwnwnwnwnwswnewnenwnenwenenenwne
nwnwnwnwnwnwnwnweenwnwswwnw
nenenenenenenwneneneseneneenewnenwnew
eeeeeewseeeeeeese
eswsewnewwnwsweneeeeeeenenwe
wnwwwwwnwwnwwwwwsewwwwww
senwseesenesweseenwweeesenewesee
seswswswswsweswswswswneswswweswswnwnw
eeeseweeseeeneeweeeeeeeee
nwnwnenwneswnenenwneenwnwnwnenwnwnwnene
nesenesweeswnenweeneneenenenwseeenw
nwnwnwnwnwnwnwnwnwnenwnwneseewnwnwnwnw
seseeseeeseseseeseeseeswnweseee
neeswwnenewswwnwneseswsewneweseesw
nwwswnewwnwnwnwneswnwnwnwwnwnwnwnwnw
wswwnewswswswnewswwswseneswsw
nwnwnwswnwnwnwnwwnwwnwwnwnwnwseenwnwnw
swewnwwnewwwnwnwwnwnwseeseenw
swswswswseswswswswneswswswswswseswsw
neeneswneneenwswneswnenenwenewseneew
enwnwnwwwnwswenwnwnwnwnwnwnwwswnwnw
nenenwnenenwnwnenenwnwnwnwnwnenwnwnwnwse
nwnwsesenwnewnenenwnwnwnwwnwnweseswnww
swenwwsenwsewewwnwwwwwwneesww
wswnwnwnwnwnwwwwwenww
seseseseseswseeseseswseseseswsesenwswse
wnwsenewwwwnwwwwswwwww
seesweeweeeweeeeeeeneee
nwwnwswwewwwwwnwwwwnwwwww
nenwnwnewnwnwnwsewnwnwsewwnenwnwnwsesesw
neenwsenewnenesenwnwnwsesenenwnenenwnwsw
swswswswswswswseswneswswseswsw
wneenwnwseneeneswnweseswsewsenenwnee
swseswswswswswseswseswswswswswneswswswsw
wswswswnwswseswwswswsw
swswsesweswswswswneswswwse
neswweeneewseneenenewseenenwesenw
swwwweeseseswnwneenwnwwsewwwnwse
neneneeneneeeneneneswneenwnwesweswe
wnwnwnwsewwwnenwwwwnwwew
nwswnesenwseseswseneeswse
nwnwnwnwnwnwnwenwnwnwnwwnwnwwnwswww
nwnenenwswnenwnwswnenenwnesenenenwsenenwe
senwnewseenesweswneseseeesesesesesesesw
eneneeweeneeeeeeeeeeeee
eseeeeseseseseseeweseseseeseee
wwsewwwswwwwwnewswswwwwww
enwsweswsenwnwswswswswnweswswswseswswsw
sesenwseswswsesewseseswseseseswseeneswse
eweenwesweeewnwweewesesee
seswseenwwnwsweswneeseswsesese
seswneswswsewnwsweswnwwneswneswwswwse
nwwnwswwnewnwnwnwnwnwnwnwnwwnwnwnwnw
swswwwneneswwwwww
nwswwsewnwnwswnwnwwswsweneneseenewnwe
senwnwnenenwnwnwenwswnenwewswswswnwsw
swwswswswswwswswswwswswswewswwwsw
swsesewseseseseswseneswsesesesesesesesese
ewseeeeswseseeeeeeeseeenwse
nwnwnwnwnwnenwnwnesenwnenwsenwswnwnwnwnw
nenenwwnenenenwnwnwnwnenwseenwnewnene
wswwswwnwwsesewswswswswswswwwswwswne
seenwweseseswnewenesenenenwswwnwnwe
swswwseswewnewswwwweesenwswwswsw
nwwnwenwwswnwnwnwnwwnwwnwwnwnwnwew
wswswsenewswwswswswswswswwwswswsww
wwwwnwnwnwnwnwnwewwnewwnwnwswwnw
eswnesewseeeesesweenesenwnwseseseenw
eswseseseeneseenwnesewwseeseswwsese
esenesesesesenwswsesweswnwswweswsesese
nwseesweeeewnwnwswewee
nwwnwnenenenenwsenenwnwnwnwnenwnwnenenw
wsenwnenwnwesenewnenwnwsw
swswswneswswwswswswswseswwswswswswswswsw
eeseweseseswseeseseseeesenwsewee
nenenenwseneneneneneswenewsewswnenene
eeneewswseswnenenenwnwswnwnwenwswnwswne
swwnwnwwsweseewswwswnewwwswsesww
swwseseswswswseeswsewswneseswswswsese
neseseswwswsesesenwseseseseseswesesesese
eewesweeeswseeswnweenwwnenwne
swswswswseswnwswwswwswwwswnewsesww
nenwnenesenewnenenenewneneneneneneeswnee
wsweswewwswswseseswewnweseswenw
nwnwwnwwwwsewwsewnwwnewnwnewnw
seneeenwneeeeswneeseneeeenwswe
swnwsenwnwneseseswseseneseseswwseeeswse
nwnwnewewenenwnwnwnenwnenwnwnwnwnwnw
neseneweenewneneeeeenenwneenenene
ewseneneenenenenwneneneseeneswenenw
nwnenenwnwnwnenwnwsenwnwnwnwnwsenwnwnwnw
swwswswwwwswwwnenwswswsweswswwwsw
eeseeeeneeenenwneneeeeenewsww
seseeeeeeeeeeswneseeseseeese
nesenewenwneeneneenenenene
nwsesenwseewwweseseseseseeswswswneene
swneswswwwwseeswwwwwwwsewwnwnw
senwswseenwseswseswswseseswswswseeseswsese
swseswswswseswnesesesweswswseneseswnwsew
eeeweseeneeenweeeneenesenene
eseeseseeseesenweseseeenwswsesee
enwneeneeenenesweneneneenenenenenene
swswswswswewswwswswswseeswswswswswsw
sesewswwnweseswnesesesesesewneswsese
nenenenwswnwenwsweeeeeneneneneese
nwneswenwwwwenesewsenwwnwnwnenwsww
neenwseseeseseseseswewnwnesewseswnee
neneweneneneeswneneneneneneenenenenese
sewneneeneneneneeneneeneneneneeenene
nwnwwwwwsenwnwnwnwwsewenwsene
eswsenwnweeeseseswseeeeweee
seeeseseseeseseseseseeeeeeew
neeeeseeenwneweeneesee
nwswnwwenwnwnwnenwnenenwsenenene
eneneneneenweneneweseneneneseswenene
nesweeseeneseeswweweenenwseese
nwwnwwwnwnwwnwenwswnw
swswswwnenwswwswwwswesweswnwswwsesw
nwsesenwnwnwnwwnwnwwnenwnwnwnwneenww
wnwsewwsenwwwnweeewwewnesww
nwnesenwseenesesesenesenenwwnwsenwwwwse
nwnwnwnwnwnwnwneneenwsenwnwnwwnwnwnwnwnew
sewsewwwnwnwnwnwnwwwnwnwnwnwnwnww
ewnenewweswswwewneweeeneee
swnwnenwnwnwnwnwnwnwnwnwnwnwswnwnwnenwnw
nwsenwnwwseneenenwnwnwnwnwnwnwnwnwnww
senwnwsenesenwnwneneswnenenesewnwswnenwnw
senweenweeeesweseswnwewenesee
wwewwnwwwwnwwnwwwwwwwswee
seswsenwsesesesesesesesese
nwnwwwewwnwwwwnwwwwwwwww
seeeeeeeeeseeeeseswseseeseenw
swwswswswswesweswswswswwswnwswswswe
eneneeeswneeeeneeeeeeeeenw
nenenwneeneneseneseneneneneenenwnwnewsw
neeenwewseneenwneswnesenewswneneeene
ewseseseseseseswneswseswswnwseswsesesese
nwnwnwwnesenwnwnwnwnwnwwnwnwnwwwww
nenweneeesweeeeeswewseswnwswe
weswswswswwwswswwwwswswswswswww
nenwsesesenweesesenwwnweseseswsenwse
seeeeeseeenwseeseswseeeseesesene
wnwnenenwsenwwnwweewnwwee
seeseseseesesesesenwsesesesesesesesee
wewswwwwwneswwww
sesenwseseseseseseseseseseseeseseswsese
seeneewsenweswesewwnwseseswswnwsesw
wnwnwswnwnwenwnwwnwnwnwneneswnwsw
seseseesesenesewesese
ewneeenweseseesesweeseseeseseseese
neneneseneneneneneneneneeeeneswnenenewne
senenwnwnwnwnwenwnwnwnwnwwnwnwnwneswe
wsweenweeseweeeenw
nenweesesesewsweeenwse
neneeneeneneneneneswneeneeeeenee
swenenenwneneneneneneeswnwneneneneneee
neenwneseneeenenewneweswneseenwnesw
swwsenewswneswnwswwwwswswwwwwse
nenwwswnewneseseswwsewwwnwwwwww
nenwswnwnwnwnwnwnesesenwnwnwwnwwnwnwnwne
wwswwwneswwswnwwwnewwwswwwse
neeswseseseseswwseneseeseeseseesesenee
nwnewnwneneneeneseneenenenenenewnene
nwsewsweseweeswwsenwnwwnwneenesw
eeeeseseeeseeseneswsee
nwnwnwnwwnwwnwwnwnwnwnwwwwwswnew
ewenenenenenenenenenenenenenenesenenene
nwnwnwwwnwnwnwwwwwwwewnwnwnww
nenenwneseseneseeswnenwwwwsenesenwnw
eeeneeenweneesenwseesweswseew
wswwneeenwnwnenwsenwswnwwnwwsesew
eeeeesewsesenweeseseeeese
eneesesesenweeneneswwnewnenenw
nenwswewenesenenenwseneneseeeenwnene
nwesenwsenwswnwnwnwnwnwnw
nwnwnwwnwwsenwnwnwnwnwnwwnwnwwnw
swneneswswswswseswswswswswswswswswswsww
neswnewnwnwewwwwwwswwwwnewsese
newwwwswwsewwnwnwwnwnwwwnewnw
seswseseneseswwsewseswseseswsenesesese
swswneenenenenwnenenenenenwnenenenenwnesenw
sesesewseeseseseseswwseseseneseeeneese
eeseneswsenenwwnwnenesewnenwnwnwswnw
wnenwneneneneneneneseneneenenesesenew
nwenwnwnwnwwnwnenenwnwnwnenenwnwnwnwne
nesenewsenenewnenesewnenenwnenenenene
wnwnwnenenwnwsenwwnwnwsenwnwnwnwnwnwnwne
nesewnwswwwwswwewwswew
wneweneeneeneneseewswwnenenewee
wwswwnwseswswweswwwwswwswswnwsesw
swswwswswswswneswswneseswwneseswswwswswsw
wwneseswwwwswe
nwsenwnenwnwnenenwnenene
nenenenwnenenenenwnenwsw
seswnwseswnwswneswswswsesweswswswnwsesw
swneswnesewnewwwswswwwwnwswww
swswnewwswswswswwswswswswswwswswwse
swweswswswswnweswneeswnwseswswswnwsw
swseswnesesesewneswwswneswnwseneswsenw
sewwnwwnwnwwwsenenwnwswwwsenewwwne
neneswneeenenweneswneneneswwneeenenene
swseswsweseseswsenenwnwwswswseswseneesw
nwenesenwsenenenwneswsweswnwnewesenw
swneneenwnwseneeeswneneeneweenene
swswswswwseswswseseseneswsweswseswswseswnw
eesweenesweeeeeeenwweeeee
nwnewneswwseneswswswwswseneswneseswsw
eseeenweeeseseenwnweseeeswese
neenwnwswnenenwenwnenwnenenenewnwnwnwnw
neeeneneeeneenewsenenenweneneesw
seseseseswwswswseseseseswswswswswswnee
senwswsewseswseswseseseswseseesesesenesese
swsweswswswwswwswswswswswswnwswsweswsw
neeewnewneesewseeneneenenwesene
nwnwenweswnwweseeesesweeneeseesenw
sewwwwwwnwwwwww
nwwneenwnwneswwenwnwnwnwneswswnwnwswnw
esesweeeeneeeeneeeewseseeesee
swsewenenenwneeseswwnewsenwneneene
nenenwnwnwnenwnwenenwnenwsenwnenwnwnenenesw
seseeswseneswswseseseswsweswwsesewsw
esesenewnwnwwwswnwnewwnewnwwsew
wnenwwswwswwswswswswwwswswwseesw
senenenwnenenenenenenenenenenenenwnene
swseneswswseseswswsweseswswwnwswsesese
wewwswwnwwwnwewwnwwswwsewsww
swswewsesweswseswseswswnwswnwswenwswse
neeeeeneeeeneeneenesweneenee
swseseseseswswsenwseseswseseseeseseseswse
swnwnwnwwwnwnenwnwesenwnwwnwnwnwnwnwnww
swneswwesesewswwwswwswswwswswwnenwsw
nwswnwsesenweeseswwswseswseswesenwse
swwnwwnwnwwnwnwwnenwnwnwwnwnwwnww
wneeswsenwswseseswwesw
neeenenwsweneseesweenenweeneeee
nwneeswseneswnwsenwnwsenwnwnwnenwnwnenw
sewwwsewswenwswswnwnw
wnwnwnwwenwnwnwnwnwsenwnwnenwwsw
wwswswwswwwwwwswswe
eeeneeeeeeseneeenweenewnee
neeesenenenewneeneeneneneenwnesw
wwwnewseewnwwwewwwwwwnwwse
seseseseseesewsesesesesese
eseeeeweeneeeseesese
swswswswnwwwwwwwwswwnewneswese
seswsesenwsenwnwsweseswswwseseswseese
swswswswseswswnwswswewswswswswswswswsw
eseeseeneewesewenweeeeseeesw
nwenwseneswswwswswnwseswseswwneswsweesw
wnwsewsesenenwneseswnenenwnw
nwnwnwsewswnwnwwwnwwnenwnwwnw
ewwnwnwnweswenwsenwwsesenwnwsenwewnw
eseeeeeweeeswneeseewenwneee
neswswswewswseswnwswseswswsw
wwnwwnwswenwnwwnwnwnwnwnesesewewne
nenenwnwnwnwneweneneneenenenenwnwnww
wneeeneeneneneeneeneeeneenenesee
swwwnwswswwnewswsweswwwswswswswwsw
eeeseseseseseewsewseeseseneewsese
wnwenwnwwenwnwnwwwnwsewwnwse
eswneewseseeseswneeseenww
wwnenwwwswnwnwswwwnwwwwwewww
neswnwswnwwswwwnwneeneswswwnwnewnw
swseneswseswnwwsenwswwnwswseswnesesene
nwswnwnwnwnwswwnwnenesenwnwnenwnwnw
swswnewswwwswswwwwwswswww
nenenenenenenewnenenenesenenenenenenene
wwswnwwneswwswwwwsewswswwwswswsew
eseeweeeeeseeseneeeesesesese
eeeeeseeesweenenwneeenweeee
swsewsesesenwnwseseneseseeneseeseswese
eeeenwseeeeeneenene
eweesenwseewne
nwnenwnewneseenewswsewsenwnwnwneswnesenw
esweeswseseneseeseeeseeeeeene
enwnenwnwnwenwwnenwwnweseswswnwnwnenwne
eenesenwnesenenenenwneneewnenwswsene
seswseseewewseseseseseesewseseswswnw
nwnwwnwenwnwnwnwnwwnweseswnwnwwnwnw
neseswswswswsesenwnwnwwsenwneseswwwsewe
sewwwwwnwwwnenwnwnwwwwwnwnw
wwwewswewswwwwswwwwwwwsw
swseeswseseneeeseeenwneneswewswne
neeswwnwneenenwnenesenwenewnenenewne
swwwwswwseswswwswswswswnewswwswsw
nwnwnwwwnwnwnwewewwswnwnwnwwnww
swswswswswswswswswswswwswswswswwswswne
weswswswnwweswneswswswswseswswenwswswnw
nenenwnenenwnenwnesenwsewnenenwnenenenenw
nwswnwnwsenwnwnwneewwseseswnwnwseneenw
seswneseseswneseswnwseewsewse
senwseeeseeeseseseseeseseseseesesw
enenwsewnwsewwnwnwswnewwwnwnewsw
wwswwwnwwsewnewnwnewww
nwswneseneswnwsweswswwswswswswnweenwesw
swwswweswswswswswswsweseneswneswwww
wewswwwwwwnwwwwwwnwnwwww
neswwwnwwswwseswswwswsewnwswwswwsw
nenwneneneneswnenesenenenenesenenwnwne
wseseseseseeseeeseseeesenew
swseenwnenenwswnwnwwsweenwneneseenenw
eeswsenewneseweeeswsesesesewnwnesese
nwseeeswseswwwnenesenwseswwseesesesesw
nesewnenenenenenene
wnwwnwwnwwnenwewwnwwwnwnwnwnwswse
neneneneswnenenenene
nwnwnwnwnenwnwneeswenwnewnwnwneenewnwne
eeeeneeeeneneneneeenwneswneswenwne
nenwnenwwnenenwenenwnenwenwneneswnene
nwnwnwwnewwwnwwwsewnwwwwwnwwnw
weswswsesweswneswnwswswswswswsweswsww
neneeneewneneneneeneswnenenenenenene
wswwwwnwnewwwwswswnwswsewsewsw
swswsenwseswseswnweswsesesesesesesesesese
nenwnwnwneneenenenenenewnwnwnenenesenene
swseswswwswsenenwseswswseswswseseswswsese
swswsesweswneswswswewnesenwseswnene
nenesweenesenenenenwnwneswnenwswsenwnwnw
wewsewswseswwnewswwnwwnwwswwwsw
nenwnwsenwswnwnwwnesenwnwnwnwnwnwenwne
sesenweseeseseseseneeseseeseseswsese
seweswwwnesenwwnwnwnw
sweseseseswneewsenweseneseeseesee
neneneeeeeneneneenenenenenenenewnew
nwewneswsweenwsesewesenesewneesw
eseseseseenesenwseeseeeew
nwswswseeswswseswseswswswseseseseseswswse
nwnwwnwnenenenwenenenenenenwneenenenenwsw
neseswswseseswswsewseseseseseseneswsesw
seswswswseswswnwseswswswswswswswswswsenese
wseswwnwewnwnwwwwwsweswnewnwenew
sewwswwneswwwwswwwenewwwswew
swseswswseseneseseswswsewseswseswseswsw
wsesesewseseeeseseesesesesesesesesee
nwnwnenenenwnenwnenenenenwnenenenwsenwnw
senenwswnweseswnenweneswwsw
neeeseeeneeneneneneenwnenenesenwe
nwwnwnwneswnwwnwswnwenwnwnwnwnwwnenwe
seseswewseswswnwneneseseneswswsewwsesw
nenewneeneswneeneneneseneneeneenene
neneeeneeeeeeeeneeeeewene
wnwwenewnwnwnwnwwnwnwnwwnwnwswsenwsenw
wwsewwswnwwwwwwswwwwww
swsweseeswsenwseseneweswswswwswswsesese
nwwnwnwnenwnwnwsenwnwnwnenwnwswnwnenw
sweswswswnwswneneneenwswswswswswsesww
neenewnwnwnenwnenenenewnwneneenwnwnw
nwnenwnwnenenwwseenwnewnenenene
nenenesenwswnenenenwnenwneneneenenwne
neeneeneweneeneeeneeenwese
swwneswnwswwsewswneswswseswswwswswnesw
swseseseseseseseeesesesenwseseseesese
nenweswseswswwsewswswnwnewwnwnesesew
swseswseseswswneneswswsenesese
nwseswsesesenwsesenwnwsenweseewwsese
neseeneeneneeeenenenenenenenewnew
nweweenwnwewseseseseesesese
esenwwnwswnenwwseeswswewnwswenesesese
neenwnwneseseseewneenesewnenenenenew
nwnwnwnwnenwnwnwnwnwnwswenwnwnenwswnwnwnwnw
swnwseswseeswnwswsw
wenweeseneswneswnwnwwneswseneneseswsw
nenenewnenenenenenenenenesenwnenenenwnene
seswnenwseeseswwseesenwswseseeeee
eeeneeeeweneneeeeeeeewee
eeeeeeneesweeeeeenweeee
eeneneeneeneeneenwneseeeneeene
wwwwsewwwwwwwnwwswewnwwsww
wwwewswwwnwnwnwnwwwwwnww
senwswsewwneseneswnenewwwenwwe
seeesesweseseneswnwseesewseeseew
swwneewwswswwswwwswswwswnewwww
swswwswswswwseswneswswwwwwwwswswsw
sewnwswwnwewnwwwwnenwnwnwnwewsewne
nenwnwnwnwwnwnwneswnwnwnwnwswnwnwnwnwnw
eweseneenwneenewneeeeneenewse
nwwwwwsewsenwwnwnwwweswnwswnwnee
eeeeeseeseesweenweseeeeeee
eneenesenewnenenenenwenenesenenenene
wwwwwwnwwwwwseewwwwwwww
nwnwwwnwnwwenwwwwwwnwwswwnwww
swnesesesesesewseseseseseseseseseesesesew
nwnwnwnwnweswswnenwnenenenenwnwnwnenwnw
wwwwnwnewnesewwseswwenwsewwnwnw
sewwwwwsewswwwnesewwnwwwwwwne
swswnwswswswnwswwswswswswwseweswswsw
wwnwswwwwwwwwseseewwnwnwnwww
nwnwswnwnwnwnwnenenenwnwnenenwnenenwnesw
eeeeeneeseenwesweneweneene
nenwwnwwwwnwwewwwwwsewseswwnw
nwwswswswnwwwsewwewwwweswwe
seswswwwswswnwwnwswweswweswsenwnw
nwnenenenenenwneneneswnenwnenenenenenene
neeesweeeenesweeeeeeseeee
eswswseseseswswswswswweenewnwswseswsw
eeseseseeseesesesesenwswseseneseesw
seeeeseseeeeeswenwseseesesesesese
neneenenwneneswnenwneneseenwnenesenenene
senwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnw
neeenenenenenenenenweesweenenene
wwwnewwwwwwwwwwwwwwswwse
eeeeseeeeeeneesweseee
seswswnwwswseswswswswswwswnwswwswww
eseseeseeneesweswseseeesesesesenw
seseeseeenweeswesenesesesenesewe
seneseseseseseseswseeesesesesesesenwwenw
seeeeeeeeweseeeeeeeeee
neenwneneneeeneneeeneneneneeneeswne
wwwwwwwwwwwwwwnwwnwwe
seseneseseseswsenwswswswseseswsenwseswsesw
wwswwwnenwwwenwnwsesesweswwwwnw
wwwwwswwwnwwsewnwwnenwnwnwnewse
neneneneeewneneneneeseeneneneswee
nwnwnwnwnwnwnwenwnwwnwnwswwnwnwnw
nwseeneseseeeseeseenweswsweeesese
eswneneenenenwnenenwneneneneneneswswnwswnw
seswseseswswswswswneswswswseswseswsesese
eswnwneeseewenesweneseneeeenwnenw
wnwnwnwnwnwnwwnwwnwnwnwsenwnwnwnwnwnw
swwswwwwswneswwwwwwswwwwnesw
seseewswweswenwswsenwswnenwswswneeene
swswswswseeswseswswswenwswwswewswseew
senwnenwswswswswseewswwnewswswsenesw
eneneneeeeeeweneeeneeesewneee
nwnwnwnwnwnwnwnwnwwwsewwnw
wwsesewsenesweneneseeeseswnwnesew
eeneneesweeeseswwneeseseeeeew
senesewwenwneswsenweeswswsenwswswnesw
nwnwwnwnwnwnwwwnwwnwwnwnwnwwsewne
seswseseswseswswswneseneseswswwseswsese
sesesesesesesesesesesesesesenwsesesesese
seeseeeeeweeeee
sesesenwsesesenenewseswswseseseseseseenw
nwnwwewwwnwswnwnwwnwwwwwnwww
wwnwnwnwnwnwnwwnwnwswenwnwnw
neneneneneneseneneneeneneneenenenwnene
wwnwsenwnwnwnwnwnenwnwnwnwnwnwnwwnww
newnwnesewnwsewsenenwswnwnwnwnwnwnwnwnwnw
senwsenwnwnwnwnenesewnenwnwnwnese
eseseseseseseseesesesesenw
neseesewsenwseseswseseseenwnew
swneswwswseswswswseneswnwseseswwseseswse
wwwewwnwwwwnwwwwnwwwwww
nenenesenenwnenwneneneswnwnenenwnenenenw
"

# COMMAND ----------

tiles <- input %>% read_lines() %>% str_extract_all("(e|se|sw|w|nw|ne)")
tiles

# COMMAND ----------

paths <-
  tiles %>%
  enframe(name = "path_id", value = "direction") %>%
  unnest(direction) %>%
  mutate(
    x = case_when(
      direction == "e"  ~ 2,
      direction == "se" ~ 1,
      direction == "sw" ~ -1,
      direction == "w"  ~ -2,
      direction == "nw" ~ -1,
      direction == "ne" ~ 1,
    ),
    y = case_when(
      direction == "e"  ~ 0,
      direction == "se" ~ -1,
      direction == "sw" ~ -1,
      direction == "w"  ~ 0,
      direction == "nw" ~ 1,
      direction == "ne" ~ 1,
    )
  )
paths

# COMMAND ----------

black_tiles <-
  paths %>%
  group_by(path_id) %>%
  summarise(x = sum(x), y = sum(y)) %>%
  count(x, y) %>%
  filter((n %% 2) == 1) %>%
  select(-n)

answer <- black_tiles %>% nrow()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The tile floor in the lobby is meant to be a <span title="I need one of these!">living art exhibit</span>. Every day, the tiles are all flipped according to the following rules:</p>
# MAGIC <ul>
# MAGIC <li>Any <em>black</em> tile with <em>zero</em> or <em>more than 2</em> black tiles immediately adjacent to it is flipped to <em>white</em>.</li>
# MAGIC <li>Any <em>white</em> tile with <em>exactly 2</em> black tiles immediately adjacent to it is flipped to <em>black</em>.</li>
# MAGIC </ul>
# MAGIC <p>Here, <em>tiles immediately adjacent</em> means the six tiles directly touching the tile in question.</p>
# MAGIC <p>The rules are applied <em>simultaneously</em> to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.</p>
# MAGIC <p>In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:</p>
# MAGIC <pre><code>Day 1: 15
# MAGIC Day 2: 12
# MAGIC Day 3: 25
# MAGIC Day 4: 14
# MAGIC Day 5: 23
# MAGIC Day 6: 28
# MAGIC Day 7: 41
# MAGIC Day 8: 37
# MAGIC Day 9: 49
# MAGIC Day 10: 37
# MAGIC 
# MAGIC Day 20: 132
# MAGIC Day 30: 259
# MAGIC Day 40: 406
# MAGIC Day 50: 566
# MAGIC Day 60: 788
# MAGIC Day 70: 1106
# MAGIC Day 80: 1373
# MAGIC Day 90: 1844
# MAGIC Day 100: 2208
# MAGIC </code></pre>
# MAGIC <p>After executing this process a total of 100 times, there would be <em><code>2208</code></em> black tiles facing up.</p>
# MAGIC <p><em>How many tiles will be black after 100 days?</em></p>
# MAGIC </article>

# COMMAND ----------

adjacent_delta <- tribble(
  ~dx, ~dy,
    2,   0,
   -2,   0,
    1,   1,
   -1,   1,
   -1,   -1,
    1,  -1
)
adjacent_delta

# COMMAND ----------

simulate_impl <- function(black_tiles) {
  neighbor_black_count <-
    black_tiles %>%
    mutate(delta = list(adjacent_delta)) %>%
    unnest(delta) %>%
    transmute(
      x = x + dx,
      y = y + dy
    ) %>%
    count(x, y) %>%
    ungroup() # Unneeded?
  
  new_black <- neighbor_black_count %>% filter(n == 2) %>% select(-n)
  
  new_white <- bind_rows(
    neighbor_black_count %>% filter(n > 2),
    anti_join(black_tiles, neighbor_black_count) # n == 0
  ) %>%
    select(-n)
  
  bind_rows(
    anti_join(black_tiles, new_white),
    anti_join(new_black, black_tiles)
  ) %>%
    distinct()
}

simulate <- function(black_tiles, n_times = 1) {
  for (i in seq_len(n_times)) {
    black_tiles <- simulate_impl(black_tiles)
  }
  black_tiles
}

# COMMAND ----------

plot_tiles <- function(black_tiles) {
  neighbor_black_count <-
    black_tiles %>%
    mutate(delta = list(adjacent_delta)) %>%
    unnest(delta) %>%
    transmute(
      x = x + dx,
      y = y + dy
    ) %>%
    count(x, y) %>%
    ungroup()

  ggplot(mapping = aes(x, y)) +
    geom_label(data = neighbor_black_count, mapping = aes(label = n), size = 2) +
    geom_point(data = black_tiles, size = 5, alpha = 0.3, color = "red") +
    theme_void()
}
plot_tiles(black_tiles)

# COMMAND ----------

answer <- simulate(black_tiles, 100) %>% nrow()
answer
