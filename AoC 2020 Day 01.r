# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/1
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 1: Report Repair ---</h2><p>After saving Christmas <a href="/events">five years in a row</a>, you've decided to take a vacation at a nice resort on a tropical island. <span title="WHAT COULD GO WRONG">Surely</span>, Christmas will go on without you.</p>
# MAGIC <p>The tropical island has its own currency and is entirely cash-only.  The gold coins used there have a little picture of a starfish; the locals just call them <em class="star">stars</em>. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.</p>
# MAGIC <p>To save your vacation, you need to get all <em class="star">fifty stars</em> by December 25th.</p>
# MAGIC <p>Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <em class="star">one star</em>. Good luck!</p>
# MAGIC <p>Before you leave, the Elves in accounting just need you to fix your <em>expense report</em> (your puzzle input); apparently, something isn't quite adding up.</p>
# MAGIC <p>Specifically, they need you to <em>find the two entries that sum to <code>2020</code></em> and then multiply those two numbers together.</p>
# MAGIC <p>For example, suppose your expense report contained the following:</p>
# MAGIC <pre><code>1721
# MAGIC 979
# MAGIC 366
# MAGIC 299
# MAGIC 675
# MAGIC 1456
# MAGIC </code></pre>
# MAGIC <p>In this list, the two entries that sum to <code>2020</code> are <code>1721</code> and <code>299</code>. Multiplying them together produces <code>1721 * 299 = 514579</code>, so the correct answer is <code><em>514579</em></code>.</p>
# MAGIC <p>Of course, your expense report is much larger. <em>Find the two entries that sum to <code>2020</code>; what do you get if you multiply them together?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>388075</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find <em>three</em> numbers in your expense report that meet the same criteria.</p>
# MAGIC <p>Using the above example again, the three entries that sum to <code>2020</code> are <code>979</code>, <code>366</code>, and <code>675</code>. Multiplying them together produces the answer, <code><em>241861950</em></code>.</p>
# MAGIC <p>In your expense report, <em>what is the product of the three entries that sum to <code>2020</code>?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>293450526</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
# MAGIC <p>At this point, you should <a href="/2020">return to your Advent calendar</a> and try another puzzle.</p>
# MAGIC <p>If you still want to see it, you can <a href="1/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Report+Repair%22+%2D+Day+1+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F1&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+%22Report+Repair%22+%2D+Day+1+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F1'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "1728
1954
1850
1825
1732
1536
1759
1877
1400
1579
1708
1047
1810
558
1132
1608
1857
1756
1834
1743
1888
1660
1642
1726
541
1519
1407
1875
1618
1331
1878
1626
1200
1346
1830
1403
1557
1890
1543
823
1435
1903
1377
1931
1885
1422
1411
1563
1818
1643
2004
1364
1446
1071
1699
1140
1617
1974
1758
1537
1980
1709
1812
1178
1822
1648
1517
1477
1935
1848
1534
1734
1484
1985
1485
1963
1329
1809
1380
1552
1895
215
1844
1138
1194
1938
1774
1823
684
1948
1941
1062
1550
1602
1920
1391
1666
1327
1791
1721
1928
1805
1574
1658
1467
1852
1924
1679
2008
1989
1719
1884
1776
1806
1750
1897
1781
1667
1544
1100
1838
1839
1744
1715
1481
1480
1548
1707
1362
1681
1616
1956
1639
1911
1655
1685
1670
1789
1571
1661
1647
1379
1522
1965
1482
1158
1970
1945
1384
1535
1383
1613
1511
1896
1784
1513
841
1619
1645
1125
1932
1873
639
1657
1554
1979
1516
1995
1899
1347
1175
1918
1872
1559
1094
1423
1883
1846
1394
1488
1343
1905
1914
1578
1943
1388
1286
966
1342
1528
1702
1452
1936
2005
1188
1683
1133
447
1072
1893
"

# COMMAND ----------

num <-
  input %>%
  read_lines() %>%
  parse_number()

# COMMAND ----------

result <- num[(2020 - num) %in% num]

# COMMAND ----------

result

# COMMAND ----------

reduce(result, `*`)

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

expand.grid(num, num, num) %>%
  filter(Var1 + Var2 + Var3 == 2020) %>%
  mutate(prod = Var1 * Var2 * Var3)