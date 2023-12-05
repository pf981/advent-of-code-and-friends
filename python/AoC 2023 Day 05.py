# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/5/input

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 5: If You Give A Seed A Fertilizer ---</h2><p>You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.</p>
# MAGIC <p>"A water source? Island Island <em>is</em> the water source!" You point out that Snow Island isn't receiving any water.</p>
# MAGIC <p>"Oh, we had to stop the water because we <em>ran out of sand</em> to <a href="https://en.wikipedia.org/wiki/Sand_filter" target="_blank">filter</a> it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.</p>
# MAGIC <p>"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"</p>
# MAGIC <p>You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our <em>food production problem</em>. The latest Island Island <a href="https://en.wikipedia.org/wiki/Almanac" target="_blank">Almanac</a> just arrived and we're having trouble making sense of it."</p>
# MAGIC <p>The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil <code>123</code> and fertilizer <code>123</code> aren't necessarily related to each other.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>seeds: 79 14 55 13
# MAGIC
# MAGIC seed-to-soil map:
# MAGIC 50 98 2
# MAGIC 52 50 48
# MAGIC
# MAGIC soil-to-fertilizer map:
# MAGIC 0 15 37
# MAGIC 37 52 2
# MAGIC 39 0 15
# MAGIC
# MAGIC fertilizer-to-water map:
# MAGIC 49 53 8
# MAGIC 0 11 42
# MAGIC 42 0 7
# MAGIC 57 7 4
# MAGIC
# MAGIC water-to-light map:
# MAGIC 88 18 7
# MAGIC 18 25 70
# MAGIC
# MAGIC light-to-temperature map:
# MAGIC 45 77 23
# MAGIC 81 45 19
# MAGIC 68 64 13
# MAGIC
# MAGIC temperature-to-humidity map:
# MAGIC 0 69 1
# MAGIC 1 0 69
# MAGIC
# MAGIC humidity-to-location map:
# MAGIC 60 56 37
# MAGIC 56 93 4
# MAGIC </code></pre>
# MAGIC <p>The almanac starts by listing which seeds need to be planted: seeds <code>79</code>, <code>14</code>, <code>55</code>, and <code>13</code>.</p>
# MAGIC <p>The rest of the almanac contains a list of <em>maps</em> which describe how to convert numbers from a <em>source category</em> into numbers in a <em>destination category</em>. That is, the section that starts with <code>seed-to-soil map:</code> describes how to convert a <em>seed number</em> (the source) to a <em>soil number</em> (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.</p>
# MAGIC <p>Rather than list every source number and its corresponding destination number one by one, the maps describe entire <em>ranges</em> of numbers that can be converted. Each line within a map contains <span title="Don't blame me for the weird order. Blame LXC container.conf UID mappings.">three numbers</span>: the <em>destination range start</em>, the <em>source range start</em>, and the <em>range length</em>.</p>
# MAGIC <p>Consider again the example <code>seed-to-soil map</code>:</p>
# MAGIC <pre><code>50 98 2
# MAGIC 52 50 48
# MAGIC </code></pre>
# MAGIC <p>The first line has a <em>destination range start</em> of <code>50</code>, a <em>source range start</em> of <code>98</code>, and a <em>range length</em> of <code>2</code>. This line means that the source range starts at <code>98</code> and contains two values: <code>98</code> and <code>99</code>. The destination range is the same length, but it starts at <code>50</code>, so its two values are <code>50</code> and <code>51</code>. With this information, you know that seed number <code>98</code> corresponds to soil number <code>50</code> and that seed number <code>99</code> corresponds to soil number <code>51</code>.</p>
# MAGIC <p>The second line means that the source range starts at <code>50</code> and contains <code>48</code> values: <code>50</code>, <code>51</code>, ..., <code>96</code>, <code>97</code>. This corresponds to a destination range starting at <code>52</code> and also containing <code>48</code> values: <code>52</code>, <code>53</code>, ..., <code>98</code>, <code>99</code>. So, seed number <code>53</code> corresponds to soil number <code>55</code>.</p>
# MAGIC <p>Any source numbers that <em>aren't mapped</em> correspond to the <em>same</em> destination number. So, seed number <code>10</code> corresponds to soil number <code>10</code>.</p>
# MAGIC <p>So, the entire list of seed numbers and their corresponding soil numbers looks like this:</p>
# MAGIC <pre><code>seed  soil
# MAGIC 0     0
# MAGIC 1     1
# MAGIC ...   ...
# MAGIC 48    48
# MAGIC 49    49
# MAGIC 50    52
# MAGIC 51    53
# MAGIC ...   ...
# MAGIC 96    98
# MAGIC 97    99
# MAGIC 98    50
# MAGIC 99    51
# MAGIC </code></pre>
# MAGIC <p>With this map, you can look up the soil number required for each initial seed number:</p>
# MAGIC <ul>
# MAGIC <li>Seed number <code>79</code> corresponds to soil number <code>81</code>.</li>
# MAGIC <li>Seed number <code>14</code> corresponds to soil number <code>14</code>.</li>
# MAGIC <li>Seed number <code>55</code> corresponds to soil number <code>57</code>.</li>
# MAGIC <li>Seed number <code>13</code> corresponds to soil number <code>13</code>.</li>
# MAGIC </ul>
# MAGIC <p>The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find <em>the lowest location number that corresponds to any of the initial seeds</em>. To do this, you'll need to convert each seed number through other categories until you can find its corresponding <em>location number</em>. In this example, the corresponding types are:</p>
# MAGIC <ul>
# MAGIC <li>Seed <code>79</code>, soil <code>81</code>, fertilizer <code>81</code>, water <code>81</code>, light <code>74</code>, temperature <code>78</code>, humidity <code>78</code>, <em>location <code>82</code></em>.</li>
# MAGIC <li>Seed <code>14</code>, soil <code>14</code>, fertilizer <code>53</code>, water <code>49</code>, light <code>42</code>, temperature <code>42</code>, humidity <code>43</code>, <em>location <code>43</code></em>.</li>
# MAGIC <li>Seed <code>55</code>, soil <code>57</code>, fertilizer <code>57</code>, water <code>53</code>, light <code>46</code>, temperature <code>82</code>, humidity <code>82</code>, <em>location <code>86</code></em>.</li>
# MAGIC <li>Seed <code>13</code>, soil <code>13</code>, fertilizer <code>52</code>, water <code>41</code>, light <code>34</code>, temperature <code>34</code>, humidity <code>35</code>, <em>location <code>35</code></em>.</li>
# MAGIC </ul>
# MAGIC <p>So, the lowest location number in this example is <code><em>35</em></code>.</p>
# MAGIC <p><em>What is the lowest location number that corresponds to any of the initial seed numbers?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''seeds: 304740406 53203352 1080760686 52608146 1670978447 367043978 1445830299 58442414 4012995194 104364808 4123691336 167638723 2284615844 178205532 3164519436 564398605 90744016 147784453 577905361 122056749

seed-to-soil map:
0 699677807 922644641
4174180469 3833727510 120786827
1525682201 2566557266 229511566
3280624601 3954514337 340452959
2228029508 2796068832 310221139
3621077560 3280624601 553102909
2120836342 592484641 107193166
1982514669 227320902 138321673
1755193767 0 227320902
922644641 1622322448 603037560
2538250647 365642575 226842066
2765092713 2225360008 341197258

soil-to-fertilizer map:
1916776044 145070025 3464138
1920240182 0 145070025
706160141 2208005933 115191764
2898492924 830275742 87027483
3489083348 3344594558 103871907
2985520407 148534163 415139950
821351905 917303225 327392865
1148744770 1517236949 182706102
295069722 3448466465 411090419
1816984891 3244803405 99791153
4282585972 4292886644 2080652
3592955255 563674113 266601629
4266462972 4158154511 16123000
1331450872 1244696090 272540859
2715943131 3062253612 182549793
4284666624 4174277511 10300672
4158154511 4184578183 108308461
1603991731 1995012773 212993160
2065310207 2411620688 650632924
0 1699943051 295069722
3400660357 2323197697 88422991

fertilizer-to-water map:
3585244197 3493316345 482900943
2871272496 878061687 456215665
3477664135 4187387234 107580062
845559238 15587711 56716031
121711204 2918313406 409174755
1639718746 0 15587711
530885959 2603640127 314673279
902275269 2435903232 167736895
2635221133 72303742 236051363
1070012164 308355105 569706582
1699846244 1334277352 935374889
4279315086 3477664135 15652210
1655306457 2269652241 44539787
109056711 2423248739 12654493
0 2314192028 109056711
4068145140 3976217288 211169946

water-to-light map:
3841742547 3016842841 17384315
2875021919 2637593760 185450069
3413635232 3588265685 87508205
1311241677 236307150 54007684
3349161906 4276682782 18284514
896790030 1355845673 34430118
3060471988 3835573209 145836645
2741184131 3675773890 133837788
1387754847 947687177 15489861
3785944618 2057196631 55797929
2006585491 2931426646 85416195
3873217816 3809611678 25961531
1667765627 643929130 34884144
2092001686 2434956599 202637161
1001898651 158618769 77688381
3899179347 2253048950 181907649
1786416461 377140410 101956748
0 833901414 113785763
1403244708 479097158 56815029
3859126862 3034227156 14090954
747996464 678813274 31450438
869173795 963177038 27616235
3268502638 2006585491 50611140
113785763 0 148879571
262665334 1511505797 386606610
1187603975 710263712 123637702
3319113778 3987361499 30048128
3367446420 2885237834 46188812
931220148 990793273 15913032
1460059737 1006706305 120880314
1079587032 535912187 108016943
3645890228 2112994560 140054390
3206308633 2823043829 62194005
1888373209 148879571 9739198
3501143437 3443518894 144746791
779446902 1127586619 89726893
947133180 1217313512 54765471
2481910976 4017409627 259273155
1365249361 1390275791 22505486
4087038641 3048318110 207928655
1702649771 1272078983 83766690
649271944 1412781277 98724520
2294638847 3256246765 187272129
4081086996 3981409854 5951645
1580940051 290314834 86825576

light-to-temperature map:
2659452899 3773423191 23529065
1010417677 1830019321 229964714
1506263997 1764304095 65715226
3017023682 3993999178 103632805
3758361154 3931294907 62704271
2513441862 2529586713 106552791
3821065425 3163657189 7959671
3410504451 3191697730 271334719
2500616406 3150831733 12825456
2065874786 2636139504 257698620
4142272690 2382216135 108163002
1377732678 1378901025 61208694
91217027 248578952 8927711
2463617376 3879075083 36999030
3982807123 2315058258 67157877
2323573406 2065874786 97274446
958870382 916323074 51547295
3868386197 3579887474 114420926
931392999 1351423642 27477383
2942753127 3694308400 74270555
1812734437 168620508 79958444
3301364949 2163149232 3197696
2420847852 2166346928 42769524
3829025096 3111470632 39361101
2619994653 2490379137 39207576
1571979223 1523548881 240755214
2927532333 3916074113 15220794
3125500723 4097631983 175864226
1438941372 10080856 67322625
2049903179 0 10080856
3304562645 2209116452 105941806
1976132043 1277652506 73771136
2659202229 3171616860 250670
4256036535 3463032449 38930761
1240382391 257506663 137350287
0 77403481 91217027
3120656487 3768578955 4844236
100144738 967870369 309782137
409926875 394856950 521466124
2682981964 4273496209 21471087
2704453051 3501963210 77924264
2802207515 2893838124 125324818
3681839170 3796952256 76521984
4250435692 3873474240 5600843
1892692881 1440109719 83439162
4049965000 3019162942 92307690
2782377315 3171867530 19830200

temperature-to-humidity map:
1281293605 2434144353 57731817
3534843655 3623804479 36539813
1516028925 367078655 499627624
3340374639 3427302148 25514722
1176213912 2491876170 105079693
3872645852 3827818849 188531931
508302359 1375008638 300832898
0 866706279 508302359
4146417618 3475254801 148549678
4083438506 3660344292 62979112
3365889361 3745584127 82234722
4061177783 3723323404 22260723
2015656549 1675841536 348405327
1056134836 246999579 120079076
3448124083 3452816870 22437931
3321587434 3408514943 18787205
3470562014 4016350780 64281641
3571383468 3321587434 86927509
1339025422 2024246863 177003503
809135257 0 246999579
2364061876 2596955863 115651453
3658310977 4080632421 214334875
2479713329 2201250366 232893987

humidity-to-location map:
2408792839 708984436 12070437
3916327360 4103567762 90492800
2136669394 2902458135 226099404
1414655297 721054873 722014097
2462136308 3514619416 2467233
1254861475 3327498132 98562162
2362768798 569836962 46024041
4185175199 3916327360 8885363
421054090 234463197 201173738
2497827912 1550759989 35404865
849065671 0 224309687
37059832 615861003 93123433
4006820160 3925212723 178355039
2863253575 1705311678 653833074
622227828 1443068970 107691019
2464603541 2869233764 33224371
1353423637 3128557539 61231660
1073375358 3426060294 47286090
2725544642 3189789199 137708933
26906322 224309687 10153510
2420863276 3473346384 41273032
729918847 1586164854 119146824
2533232777 2676921899 192311865
0 2359144752 26906322
1120661448 435636935 134200027
130183265 2386051074 290870825
'''

# COMMAND ----------

import re


seeds, *maps_list = inp.split('\n\n')
seeds = [int(x) for x in re.findall('\d+', seeds)]
maps_list = [[[int(x) for x in re.findall('\d+', line)] for line in maps.splitlines()[1:]] for maps in maps_list]

locations = []
for seed in seeds:
    for maps in maps_list:
        for dest_start, source_start, range_len in maps:
            if source_start <= seed < source_start + range_len:
                seed = dest_start + (seed - source_start)
                break
    locations.append(seed)

answer = min(locations)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the <code>seeds:</code> line actually describes <em>ranges of seed numbers</em>.</p>
# MAGIC <p>The values on the initial <code>seeds:</code> line come in pairs. Within each pair, the first value is the <em>start</em> of the range and the second value is the <em>length</em> of the range. So, in the first line of the example above:</p>
# MAGIC <pre><code>seeds: 79 14 55 13</code></pre>
# MAGIC <p>This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number <code>79</code> and contains <code>14</code> values: <code>79</code>, <code>80</code>, ..., <code>91</code>, <code>92</code>. The second range starts with seed number <code>55</code> and contains <code>13</code> values: <code>55</code>, <code>56</code>, ..., <code>66</code>, <code>67</code>.</p>
# MAGIC <p>Now, rather than considering four seed numbers, you need to consider a total of <em>27</em> seed numbers.</p>
# MAGIC <p>In the above example, the lowest location number can be obtained from seed number <code>82</code>, which corresponds to soil <code>84</code>, fertilizer <code>84</code>, water <code>84</code>, light <code>77</code>, temperature <code>45</code>, humidity <code>46</code>, and <em>location <code>46</code></em>. So, the lowest location number is <code><em>46</em></code>.</p>
# MAGIC <p>Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. <em>What is the lowest location number that corresponds to any of the initial seed numbers?</em></p>
# MAGIC </article>

# COMMAND ----------

def insert_missing_ranges(maps):
    maps.sort(key=lambda e: e[1])
    first_val = maps[0][1]
    if first_val != 0:
        maps.insert(0, [0, 0, first_val])
    
    last_val = maps[-1][1] + maps[-1][2]
    maps.append([last_val, last_val, 10_000_000_000])

    for i in range(len(maps) - 1):
        end = maps[i][1] + maps[i][2]
        start = maps[i+1][1]
        if end != start:
            maps.append((end, end, start - end))

    maps.sort(key=lambda e: e[1])


def get_smallest_range(i, in_start, in_range_len):
    if i == len(maps_list):
        return in_start

    output_ranges = [] # (out_start, out_range_len) pairs
    for dest_start, source_start, range_len in maps_list[i]:
        # No overlap
        if source_start + range_len <= in_start or source_start >= in_start + in_range_len:
            continue
        
        # Assume overlap
        if source_start == in_start: # Source starts at input start
            overlap_start = in_start
            overlap_range_len = min(range_len, in_range_len)
        elif source_start < in_start: # Source starts to left
            overlap_start = in_start
            overlap_end = min(source_start + range_len, in_start + in_range_len)
            overlap_range_len = overlap_end - in_start
        else: # Source starts to right of input start
            overlap_start = source_start
            overlap_end = min(source_start + range_len, in_start + in_range_len)
            overlap_range_len = overlap_end - source_start # overlap_range_len = overlap_end - in_start

        overlap_start = overlap_start - source_start +  dest_start
        output_ranges.append((overlap_start, overlap_range_len))

    outputs = [get_smallest_range(i + 1, out_start, out_range_len) for out_start, out_range_len in output_ranges]
    return min(outputs) if outputs else float('inf')



for maps in maps_list:
    insert_missing_ranges(maps)

starting_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
answer = min(get_smallest_range(0, in_start, in_range_len) for in_start, in_range_len in starting_ranges)
print(answer)
