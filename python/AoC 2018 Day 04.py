# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/4

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 4: Repose Record ---</h2><p>You've <span title="Yes, 'sneaked'. 'Snuck' didn't appear in English until the 1800s.">sneaked</span> into another supply closet - this time, it's across from the prototype suit manufacturing lab. You need to sneak inside and fix the issues with the suit, but there's a guard stationed outside the lab, so this is as close as you can safely get.</p>
# MAGIC <p>As you search the closet for anything that might help, you discover that you're not the first person to want to sneak in.  Covering the walls, someone has spent an hour starting every midnight for the past few months secretly observing this guard post!  They've been writing down the ID of <em>the one guard on duty that night</em> - the Elves seem to have decided that one guard was enough for the overnight shift - as well as when they fall asleep or wake up while at their post (your puzzle input).</p>
# MAGIC <p>For example, consider the following records, which have already been organized into chronological order:</p>
# MAGIC <pre><code>[1518-11-01 00:00] Guard #10 begins shift
# MAGIC [1518-11-01 00:05] falls asleep
# MAGIC [1518-11-01 00:25] wakes up
# MAGIC [1518-11-01 00:30] falls asleep
# MAGIC [1518-11-01 00:55] wakes up
# MAGIC [1518-11-01 23:58] Guard #99 begins shift
# MAGIC [1518-11-02 00:40] falls asleep
# MAGIC [1518-11-02 00:50] wakes up
# MAGIC [1518-11-03 00:05] Guard #10 begins shift
# MAGIC [1518-11-03 00:24] falls asleep
# MAGIC [1518-11-03 00:29] wakes up
# MAGIC [1518-11-04 00:02] Guard #99 begins shift
# MAGIC [1518-11-04 00:36] falls asleep
# MAGIC [1518-11-04 00:46] wakes up
# MAGIC [1518-11-05 00:03] Guard #99 begins shift
# MAGIC [1518-11-05 00:45] falls asleep
# MAGIC [1518-11-05 00:55] wakes up
# MAGIC </code></pre>
# MAGIC <p>Timestamps are written using <code>year-month-day hour:minute</code> format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (<code>00:00</code> - <code>00:59</code>), only the minute portion (<code>00</code> - <code>59</code>) is relevant for those events.</p>
# MAGIC <p>Visually, these records show that the guards are asleep at these times:</p>
# MAGIC <pre><code>Date   ID   Minute
# MAGIC             000000000011111111112222222222333333333344444444445555555555
# MAGIC             012345678901234567890123456789012345678901234567890123456789
# MAGIC 11-01  #10  .....####################.....#########################.....
# MAGIC 11-02  #99  ........................................##########..........
# MAGIC 11-03  #10  ........................#####...............................
# MAGIC 11-04  #99  ....................................##########..............
# MAGIC 11-05  #99  .............................................##########.....
# MAGIC </code></pre>
# MAGIC <p>The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour.  (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as <code>.</code>, and asleep is shown as <code>#</code>.</p>
# MAGIC <p>Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.</p>
# MAGIC <p>If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in.  You have two strategies for choosing the best guard/minute combination.</p>
# MAGIC <p><em>Strategy 1:</em> Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?</p>
# MAGIC <p>In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #<em>10</em> was asleep most during minute <em>24</em> (on two days, whereas any other minute the guard was asleep was only seen on one day).</p>
# MAGIC <p>While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.</p>
# MAGIC <p><em>What is the ID of the guard you chose multiplied by the minute you chose?</em> (In the above example, the answer would be <code>10 * 24 = 240</code>.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '''[1518-03-30 00:57] wakes up
[1518-04-15 23:56] Guard #2213 begins shift
[1518-10-31 00:36] wakes up
[1518-11-14 00:03] Guard #2129 begins shift
[1518-04-01 00:54] wakes up
[1518-10-03 00:42] falls asleep
[1518-07-01 00:19] falls asleep
[1518-08-02 00:00] Guard #3319 begins shift
[1518-07-03 00:01] falls asleep
[1518-08-28 00:24] falls asleep
[1518-11-02 00:31] falls asleep
[1518-10-15 00:04] falls asleep
[1518-08-07 00:51] wakes up
[1518-05-02 00:14] falls asleep
[1518-05-16 00:38] falls asleep
[1518-08-27 00:37] falls asleep
[1518-09-18 00:47] wakes up
[1518-05-29 00:52] wakes up
[1518-09-07 00:06] falls asleep
[1518-07-14 00:52] wakes up
[1518-05-09 00:59] wakes up
[1518-05-14 00:12] falls asleep
[1518-04-17 23:51] Guard #439 begins shift
[1518-11-20 00:04] Guard #2129 begins shift
[1518-07-21 00:02] Guard #3347 begins shift
[1518-11-16 00:04] Guard #241 begins shift
[1518-04-02 23:48] Guard #1777 begins shift
[1518-07-11 00:00] Guard #241 begins shift
[1518-07-29 00:49] falls asleep
[1518-09-14 00:38] falls asleep
[1518-05-27 00:39] wakes up
[1518-04-09 00:54] wakes up
[1518-11-01 23:56] Guard #103 begins shift
[1518-10-07 00:42] wakes up
[1518-09-26 00:58] wakes up
[1518-09-10 00:54] falls asleep
[1518-08-15 00:48] falls asleep
[1518-06-09 00:01] Guard #2251 begins shift
[1518-11-06 23:58] Guard #103 begins shift
[1518-10-04 00:29] falls asleep
[1518-08-02 00:56] falls asleep
[1518-08-21 00:18] falls asleep
[1518-11-23 00:30] falls asleep
[1518-09-29 23:59] Guard #829 begins shift
[1518-09-17 00:49] falls asleep
[1518-07-25 00:49] wakes up
[1518-08-19 00:58] wakes up
[1518-07-13 00:48] wakes up
[1518-04-11 23:59] Guard #2539 begins shift
[1518-04-30 00:32] wakes up
[1518-07-05 00:27] falls asleep
[1518-09-02 00:29] wakes up
[1518-09-21 00:58] wakes up
[1518-04-26 00:08] falls asleep
[1518-04-23 00:26] wakes up
[1518-05-25 00:55] wakes up
[1518-05-14 23:58] Guard #241 begins shift
[1518-09-09 23:58] Guard #3319 begins shift
[1518-04-23 00:23] falls asleep
[1518-08-08 00:42] wakes up
[1518-06-12 00:03] falls asleep
[1518-03-31 00:03] Guard #103 begins shift
[1518-04-11 00:58] wakes up
[1518-03-28 00:53] falls asleep
[1518-06-29 23:57] Guard #103 begins shift
[1518-05-08 00:36] falls asleep
[1518-11-18 00:00] Guard #2137 begins shift
[1518-03-31 00:21] falls asleep
[1518-05-08 00:57] falls asleep
[1518-06-18 00:50] falls asleep
[1518-05-08 00:06] falls asleep
[1518-05-09 00:23] falls asleep
[1518-08-24 00:00] Guard #1301 begins shift
[1518-07-07 00:57] wakes up
[1518-10-24 00:51] wakes up
[1518-08-29 00:31] falls asleep
[1518-08-27 00:51] falls asleep
[1518-08-19 00:54] falls asleep
[1518-10-05 00:02] Guard #3347 begins shift
[1518-04-04 00:14] falls asleep
[1518-10-17 00:01] Guard #2389 begins shift
[1518-05-07 00:57] wakes up
[1518-11-17 00:01] Guard #1889 begins shift
[1518-07-09 00:54] wakes up
[1518-07-12 00:02] falls asleep
[1518-04-23 00:00] Guard #2137 begins shift
[1518-05-02 00:00] Guard #1283 begins shift
[1518-07-08 23:58] Guard #2389 begins shift
[1518-11-08 00:48] falls asleep
[1518-11-06 00:48] wakes up
[1518-06-25 00:46] wakes up
[1518-06-03 23:57] Guard #3371 begins shift
[1518-05-19 23:50] Guard #3371 begins shift
[1518-06-10 00:04] Guard #3371 begins shift
[1518-11-20 00:36] falls asleep
[1518-10-10 23:58] Guard #2539 begins shift
[1518-07-09 00:42] falls asleep
[1518-09-09 00:21] wakes up
[1518-05-10 00:03] Guard #3347 begins shift
[1518-06-18 00:47] wakes up
[1518-05-16 00:55] wakes up
[1518-06-23 00:41] falls asleep
[1518-08-27 00:39] wakes up
[1518-05-26 00:03] falls asleep
[1518-07-10 00:03] Guard #2389 begins shift
[1518-10-14 00:02] Guard #2389 begins shift
[1518-06-09 00:40] wakes up
[1518-07-01 00:55] wakes up
[1518-04-11 00:15] falls asleep
[1518-10-11 00:55] wakes up
[1518-06-25 00:24] falls asleep
[1518-04-29 00:45] falls asleep
[1518-11-04 00:02] Guard #1889 begins shift
[1518-07-20 00:04] Guard #2129 begins shift
[1518-05-06 00:32] falls asleep
[1518-04-27 00:08] falls asleep
[1518-11-11 00:33] falls asleep
[1518-11-21 00:22] falls asleep
[1518-10-28 00:50] falls asleep
[1518-07-24 00:19] falls asleep
[1518-10-21 00:10] falls asleep
[1518-09-19 00:01] Guard #2389 begins shift
[1518-03-31 00:57] wakes up
[1518-11-20 00:46] wakes up
[1518-05-28 00:41] falls asleep
[1518-11-18 23:56] Guard #439 begins shift
[1518-04-04 00:50] falls asleep
[1518-10-09 00:27] wakes up
[1518-11-16 00:47] falls asleep
[1518-08-03 00:42] wakes up
[1518-10-17 00:57] falls asleep
[1518-10-27 00:22] wakes up
[1518-07-29 00:03] Guard #2251 begins shift
[1518-10-06 00:18] falls asleep
[1518-07-31 00:23] falls asleep
[1518-09-05 00:00] Guard #1283 begins shift
[1518-11-10 23:59] Guard #439 begins shift
[1518-10-16 00:53] wakes up
[1518-10-31 00:57] wakes up
[1518-09-15 00:58] wakes up
[1518-05-30 00:59] wakes up
[1518-08-13 00:38] wakes up
[1518-09-08 00:42] wakes up
[1518-09-05 00:17] falls asleep
[1518-03-28 23:59] Guard #1777 begins shift
[1518-06-11 00:52] falls asleep
[1518-06-16 00:46] falls asleep
[1518-06-22 00:49] wakes up
[1518-06-27 23:58] Guard #2389 begins shift
[1518-10-15 00:42] wakes up
[1518-10-14 00:11] falls asleep
[1518-07-10 00:52] falls asleep
[1518-06-14 00:22] falls asleep
[1518-11-01 00:50] wakes up
[1518-09-21 23:59] Guard #1777 begins shift
[1518-05-23 00:43] wakes up
[1518-05-11 00:47] wakes up
[1518-09-02 23:57] Guard #1889 begins shift
[1518-06-12 00:32] wakes up
[1518-03-31 00:54] falls asleep
[1518-10-18 00:46] falls asleep
[1518-08-24 23:56] Guard #1889 begins shift
[1518-04-10 00:21] wakes up
[1518-07-23 00:01] Guard #3347 begins shift
[1518-10-08 00:08] falls asleep
[1518-09-28 00:00] falls asleep
[1518-04-18 00:57] wakes up
[1518-05-26 00:44] falls asleep
[1518-10-30 00:22] falls asleep
[1518-11-14 00:42] falls asleep
[1518-11-04 00:40] wakes up
[1518-04-09 00:38] falls asleep
[1518-06-24 23:57] Guard #1283 begins shift
[1518-06-02 00:01] Guard #1283 begins shift
[1518-07-16 00:30] wakes up
[1518-07-21 00:57] wakes up
[1518-11-23 00:57] falls asleep
[1518-09-01 00:45] wakes up
[1518-07-17 00:45] falls asleep
[1518-04-01 00:51] falls asleep
[1518-04-24 00:00] Guard #3347 begins shift
[1518-09-18 00:02] Guard #631 begins shift
[1518-05-13 00:23] wakes up
[1518-04-25 00:54] wakes up
[1518-04-14 00:02] Guard #1889 begins shift
[1518-09-12 00:13] falls asleep
[1518-08-26 00:57] falls asleep
[1518-08-13 00:02] Guard #439 begins shift
[1518-10-06 00:56] wakes up
[1518-10-01 00:32] wakes up
[1518-10-17 00:20] wakes up
[1518-07-28 00:01] falls asleep
[1518-10-28 00:59] wakes up
[1518-04-01 00:36] falls asleep
[1518-04-01 00:46] wakes up
[1518-05-24 00:01] Guard #2539 begins shift
[1518-04-24 00:41] wakes up
[1518-10-06 23:59] Guard #2903 begins shift
[1518-10-17 00:52] falls asleep
[1518-10-12 00:17] falls asleep
[1518-10-27 00:49] wakes up
[1518-08-22 00:01] falls asleep
[1518-08-16 00:57] wakes up
[1518-09-06 23:59] Guard #631 begins shift
[1518-04-17 00:01] Guard #103 begins shift
[1518-08-06 00:25] falls asleep
[1518-10-24 00:15] falls asleep
[1518-11-04 00:39] falls asleep
[1518-03-27 00:11] falls asleep
[1518-04-19 23:59] Guard #439 begins shift
[1518-10-29 00:55] wakes up
[1518-05-05 00:20] wakes up
[1518-10-02 00:49] wakes up
[1518-05-30 23:57] Guard #631 begins shift
[1518-09-11 00:41] wakes up
[1518-06-02 00:08] falls asleep
[1518-11-16 00:44] wakes up
[1518-10-27 23:52] Guard #1319 begins shift
[1518-10-10 00:00] Guard #1487 begins shift
[1518-08-16 00:54] falls asleep
[1518-05-20 00:00] falls asleep
[1518-07-29 00:14] wakes up
[1518-08-10 00:19] wakes up
[1518-08-04 00:00] Guard #439 begins shift
[1518-09-22 00:59] wakes up
[1518-11-12 23:57] Guard #1889 begins shift
[1518-11-01 00:38] falls asleep
[1518-08-09 00:56] falls asleep
[1518-07-20 00:47] wakes up
[1518-05-08 00:29] wakes up
[1518-06-12 00:56] falls asleep
[1518-06-15 23:56] Guard #2213 begins shift
[1518-05-13 00:03] Guard #1889 begins shift
[1518-10-18 00:19] falls asleep
[1518-07-10 00:30] wakes up
[1518-09-21 00:50] falls asleep
[1518-07-04 00:58] wakes up
[1518-11-09 00:46] falls asleep
[1518-05-13 00:59] wakes up
[1518-06-05 23:56] Guard #2251 begins shift
[1518-05-25 00:03] Guard #1213 begins shift
[1518-06-19 00:01] Guard #2903 begins shift
[1518-08-16 00:04] Guard #2213 begins shift
[1518-11-06 00:07] falls asleep
[1518-04-30 00:27] falls asleep
[1518-06-24 00:50] wakes up
[1518-05-27 23:58] Guard #3347 begins shift
[1518-10-22 00:22] falls asleep
[1518-05-26 00:29] wakes up
[1518-05-20 00:37] falls asleep
[1518-09-16 23:58] Guard #2903 begins shift
[1518-04-29 00:08] falls asleep
[1518-08-18 00:56] wakes up
[1518-08-22 00:42] wakes up
[1518-04-08 00:40] wakes up
[1518-08-02 00:53] wakes up
[1518-09-14 00:58] wakes up
[1518-10-06 00:07] falls asleep
[1518-04-28 00:49] wakes up
[1518-09-25 23:58] Guard #3319 begins shift
[1518-04-29 00:34] falls asleep
[1518-04-12 00:36] wakes up
[1518-05-19 00:29] wakes up
[1518-06-02 00:59] wakes up
[1518-08-03 00:24] falls asleep
[1518-05-28 00:13] falls asleep
[1518-04-15 00:02] Guard #1301 begins shift
[1518-09-30 00:32] falls asleep
[1518-07-27 23:50] Guard #1777 begins shift
[1518-06-15 00:15] falls asleep
[1518-10-09 00:03] falls asleep
[1518-04-30 00:03] Guard #1889 begins shift
[1518-09-15 00:03] falls asleep
[1518-08-30 00:20] falls asleep
[1518-06-16 00:30] falls asleep
[1518-05-08 00:03] Guard #2213 begins shift
[1518-05-17 00:51] falls asleep
[1518-06-12 00:58] wakes up
[1518-07-21 00:41] falls asleep
[1518-06-08 00:43] falls asleep
[1518-05-17 00:00] falls asleep
[1518-06-07 00:38] wakes up
[1518-05-14 00:26] falls asleep
[1518-04-16 00:26] wakes up
[1518-06-21 00:35] wakes up
[1518-10-27 00:58] wakes up
[1518-11-18 00:49] falls asleep
[1518-10-29 00:23] falls asleep
[1518-05-20 00:53] wakes up
[1518-05-18 00:00] Guard #1777 begins shift
[1518-05-24 00:44] falls asleep
[1518-11-13 00:31] falls asleep
[1518-07-16 00:58] wakes up
[1518-08-29 00:36] wakes up
[1518-10-26 23:51] Guard #2389 begins shift
[1518-07-26 00:53] falls asleep
[1518-07-14 00:56] wakes up
[1518-05-13 00:15] falls asleep
[1518-10-09 00:44] falls asleep
[1518-09-11 00:48] falls asleep
[1518-05-11 00:00] Guard #2903 begins shift
[1518-08-01 00:00] Guard #2129 begins shift
[1518-06-04 00:57] wakes up
[1518-06-19 00:42] wakes up
[1518-05-04 00:10] falls asleep
[1518-05-09 00:24] wakes up
[1518-10-21 00:51] wakes up
[1518-09-01 00:03] Guard #1319 begins shift
[1518-04-18 00:24] falls asleep
[1518-09-16 00:03] Guard #439 begins shift
[1518-07-18 00:50] falls asleep
[1518-07-20 00:06] falls asleep
[1518-05-08 00:46] wakes up
[1518-06-19 00:26] falls asleep
[1518-04-27 00:18] wakes up
[1518-07-30 00:54] falls asleep
[1518-07-31 00:45] wakes up
[1518-07-27 00:42] wakes up
[1518-08-15 00:38] wakes up
[1518-10-30 00:38] wakes up
[1518-08-04 23:57] Guard #1213 begins shift
[1518-08-01 00:41] falls asleep
[1518-08-23 00:03] Guard #829 begins shift
[1518-08-06 00:29] wakes up
[1518-11-08 00:50] wakes up
[1518-08-28 00:47] falls asleep
[1518-06-28 00:50] falls asleep
[1518-05-10 00:53] wakes up
[1518-06-11 00:54] wakes up
[1518-06-06 00:55] wakes up
[1518-10-28 23:56] Guard #103 begins shift
[1518-06-10 00:06] falls asleep
[1518-11-09 00:51] wakes up
[1518-05-16 00:18] falls asleep
[1518-03-28 00:16] falls asleep
[1518-04-19 00:53] wakes up
[1518-08-26 00:59] wakes up
[1518-09-20 00:00] Guard #2777 begins shift
[1518-10-11 00:45] falls asleep
[1518-08-09 00:00] Guard #2389 begins shift
[1518-06-01 00:46] wakes up
[1518-10-14 00:28] falls asleep
[1518-06-11 23:53] Guard #2251 begins shift
[1518-11-20 00:51] falls asleep
[1518-11-07 00:38] falls asleep
[1518-08-20 00:02] falls asleep
[1518-08-01 00:54] falls asleep
[1518-06-11 00:01] falls asleep
[1518-10-01 00:37] falls asleep
[1518-10-31 00:50] falls asleep
[1518-04-09 00:02] Guard #2129 begins shift
[1518-06-01 00:15] wakes up
[1518-04-21 00:02] Guard #2539 begins shift
[1518-07-22 00:00] falls asleep
[1518-09-28 00:58] wakes up
[1518-08-06 00:00] Guard #1319 begins shift
[1518-10-14 23:50] Guard #3319 begins shift
[1518-03-29 00:55] wakes up
[1518-08-10 00:49] wakes up
[1518-06-20 00:55] wakes up
[1518-04-19 00:08] falls asleep
[1518-11-01 00:08] falls asleep
[1518-04-01 00:01] Guard #3371 begins shift
[1518-06-29 00:33] falls asleep
[1518-08-21 00:01] Guard #1213 begins shift
[1518-08-21 23:51] Guard #1319 begins shift
[1518-06-17 00:04] falls asleep
[1518-05-22 00:54] falls asleep
[1518-11-12 00:30] wakes up
[1518-07-17 00:04] Guard #1283 begins shift
[1518-06-05 00:08] falls asleep
[1518-04-04 00:55] wakes up
[1518-07-23 00:53] wakes up
[1518-06-09 00:14] falls asleep
[1518-05-10 00:37] falls asleep
[1518-08-08 00:02] Guard #1213 begins shift
[1518-09-06 00:46] wakes up
[1518-09-07 23:57] Guard #1889 begins shift
[1518-07-18 00:55] wakes up
[1518-07-24 00:59] wakes up
[1518-05-05 00:54] wakes up
[1518-11-22 00:36] falls asleep
[1518-07-18 00:27] wakes up
[1518-10-09 00:58] wakes up
[1518-06-18 00:01] Guard #2137 begins shift
[1518-10-19 00:53] falls asleep
[1518-03-31 00:24] wakes up
[1518-09-27 00:02] falls asleep
[1518-09-12 00:56] wakes up
[1518-11-08 00:57] wakes up
[1518-10-02 00:03] Guard #1213 begins shift
[1518-06-09 00:59] wakes up
[1518-10-20 23:56] Guard #2539 begins shift
[1518-10-12 00:01] Guard #2251 begins shift
[1518-07-06 00:32] falls asleep
[1518-06-05 00:55] wakes up
[1518-10-22 00:12] wakes up
[1518-08-20 00:47] wakes up
[1518-11-17 00:42] wakes up
[1518-07-11 23:52] Guard #1283 begins shift
[1518-10-20 00:29] falls asleep
[1518-04-10 23:58] Guard #103 begins shift
[1518-07-24 00:51] falls asleep
[1518-08-12 00:50] wakes up
[1518-09-27 00:35] wakes up
[1518-10-13 00:02] Guard #103 begins shift
[1518-06-29 00:47] wakes up
[1518-10-28 00:02] falls asleep
[1518-05-10 00:44] wakes up
[1518-10-22 00:01] falls asleep
[1518-05-22 00:48] wakes up
[1518-06-19 00:56] falls asleep
[1518-06-25 00:41] falls asleep
[1518-07-07 00:51] falls asleep
[1518-10-18 00:52] wakes up
[1518-09-18 00:51] falls asleep
[1518-08-25 00:36] wakes up
[1518-06-10 00:49] wakes up
[1518-09-07 00:17] wakes up
[1518-10-01 00:31] falls asleep
[1518-04-18 00:05] falls asleep
[1518-09-23 00:01] Guard #439 begins shift
[1518-06-13 00:46] wakes up
[1518-04-20 00:30] wakes up
[1518-08-23 00:10] falls asleep
[1518-05-29 00:03] Guard #2903 begins shift
[1518-05-24 00:36] wakes up
[1518-09-24 23:57] Guard #1283 begins shift
[1518-05-28 00:46] wakes up
[1518-05-22 00:23] falls asleep
[1518-11-15 00:48] wakes up
[1518-06-01 00:21] falls asleep
[1518-05-17 00:58] wakes up
[1518-07-14 00:55] falls asleep
[1518-09-15 00:51] falls asleep
[1518-11-18 00:59] wakes up
[1518-05-25 00:17] falls asleep
[1518-08-17 00:03] Guard #3371 begins shift
[1518-04-04 00:03] Guard #1777 begins shift
[1518-09-29 00:40] wakes up
[1518-07-22 00:52] wakes up
[1518-05-07 00:04] Guard #2129 begins shift
[1518-09-27 23:54] Guard #1319 begins shift
[1518-04-29 00:09] wakes up
[1518-10-17 00:59] wakes up
[1518-07-06 00:46] wakes up
[1518-07-27 00:04] Guard #241 begins shift
[1518-08-10 00:00] Guard #241 begins shift
[1518-07-29 00:56] wakes up
[1518-07-12 00:17] wakes up
[1518-05-13 00:33] falls asleep
[1518-05-30 00:26] falls asleep
[1518-04-03 00:02] falls asleep
[1518-08-21 00:56] wakes up
[1518-04-21 00:39] wakes up
[1518-11-07 00:41] wakes up
[1518-10-24 00:03] Guard #2129 begins shift
[1518-07-16 00:53] falls asleep
[1518-04-07 00:57] wakes up
[1518-06-22 00:10] falls asleep
[1518-10-25 00:45] wakes up
[1518-09-04 00:04] falls asleep
[1518-04-14 00:58] wakes up
[1518-06-15 00:52] wakes up
[1518-04-13 00:02] Guard #3319 begins shift
[1518-07-15 00:01] Guard #1283 begins shift
[1518-07-22 00:36] wakes up
[1518-06-03 00:00] Guard #439 begins shift
[1518-05-23 00:27] falls asleep
[1518-07-16 00:00] Guard #1777 begins shift
[1518-08-15 00:06] falls asleep
[1518-05-15 00:58] wakes up
[1518-09-11 00:49] wakes up
[1518-11-19 00:55] wakes up
[1518-04-06 00:37] wakes up
[1518-07-15 00:13] falls asleep
[1518-08-28 00:03] Guard #1777 begins shift
[1518-07-21 23:51] Guard #3371 begins shift
[1518-09-08 00:27] falls asleep
[1518-07-08 00:02] Guard #241 begins shift
[1518-08-11 00:52] wakes up
[1518-09-09 00:32] falls asleep
[1518-08-13 23:59] Guard #3371 begins shift
[1518-07-19 00:53] wakes up
[1518-08-05 00:46] wakes up
[1518-07-01 00:53] falls asleep
[1518-09-11 00:03] Guard #241 begins shift
[1518-11-13 00:41] wakes up
[1518-11-11 00:39] wakes up
[1518-08-02 00:59] wakes up
[1518-09-09 00:42] wakes up
[1518-10-05 00:48] falls asleep
[1518-09-29 00:00] Guard #2903 begins shift
[1518-08-01 00:59] wakes up
[1518-04-12 00:54] wakes up
[1518-09-18 00:23] falls asleep
[1518-09-04 00:47] wakes up
[1518-04-02 00:03] Guard #1777 begins shift
[1518-04-05 23:58] Guard #2251 begins shift
[1518-05-16 00:26] wakes up
[1518-04-05 00:00] falls asleep
[1518-05-04 00:31] wakes up
[1518-06-13 00:30] falls asleep
[1518-09-06 00:50] falls asleep
[1518-07-02 00:05] falls asleep
[1518-11-08 00:04] Guard #1213 begins shift
[1518-03-29 00:08] falls asleep
[1518-04-21 00:15] falls asleep
[1518-06-30 00:39] falls asleep
[1518-10-24 23:56] Guard #1319 begins shift
[1518-05-20 00:28] wakes up
[1518-06-12 00:20] wakes up
[1518-09-11 00:29] falls asleep
[1518-05-09 00:57] falls asleep
[1518-06-03 00:33] wakes up
[1518-05-18 00:31] falls asleep
[1518-05-28 00:26] wakes up
[1518-09-26 00:35] falls asleep
[1518-05-09 00:00] Guard #3347 begins shift
[1518-10-27 00:28] falls asleep
[1518-04-25 00:38] falls asleep
[1518-11-01 00:15] wakes up
[1518-10-27 00:05] falls asleep
[1518-05-26 00:48] wakes up
[1518-09-25 00:49] wakes up
[1518-05-21 00:44] falls asleep
[1518-05-11 23:59] Guard #2137 begins shift
[1518-11-02 23:58] Guard #829 begins shift
[1518-04-29 00:37] wakes up
[1518-07-22 00:22] wakes up
[1518-03-29 00:10] wakes up
[1518-06-05 00:02] Guard #2389 begins shift
[1518-10-31 00:43] wakes up
[1518-05-03 00:43] falls asleep
[1518-05-18 00:57] wakes up
[1518-06-14 00:52] wakes up
[1518-07-10 00:27] falls asleep
[1518-05-17 00:13] wakes up
[1518-06-24 00:36] falls asleep
[1518-08-02 00:21] falls asleep
[1518-08-31 00:49] wakes up
[1518-09-09 00:09] falls asleep
[1518-08-23 00:26] wakes up
[1518-06-03 00:56] wakes up
[1518-07-24 23:57] Guard #3371 begins shift
[1518-07-16 00:45] wakes up
[1518-08-17 00:27] falls asleep
[1518-10-22 00:46] wakes up
[1518-04-12 00:22] wakes up
[1518-05-04 00:56] wakes up
[1518-10-17 00:53] wakes up
[1518-04-10 00:45] wakes up
[1518-06-29 00:34] wakes up
[1518-09-05 00:46] wakes up
[1518-04-13 00:18] falls asleep
[1518-07-27 00:24] wakes up
[1518-08-29 00:44] falls asleep
[1518-10-19 00:54] wakes up
[1518-11-02 00:41] wakes up
[1518-07-11 00:33] falls asleep
[1518-09-15 00:57] falls asleep
[1518-07-28 00:49] wakes up
[1518-06-30 23:57] Guard #1283 begins shift
[1518-09-25 00:06] falls asleep
[1518-11-04 00:28] falls asleep
[1518-10-20 00:34] wakes up
[1518-10-24 00:38] wakes up
[1518-04-21 00:57] falls asleep
[1518-06-25 00:29] wakes up
[1518-05-16 23:51] Guard #3371 begins shift
[1518-06-24 00:21] falls asleep
[1518-07-17 00:47] wakes up
[1518-09-09 00:02] Guard #1283 begins shift
[1518-07-11 00:52] wakes up
[1518-07-16 00:28] falls asleep
[1518-09-30 00:52] wakes up
[1518-06-30 00:36] wakes up
[1518-04-20 00:06] falls asleep
[1518-08-14 00:33] falls asleep
[1518-10-18 00:00] Guard #241 begins shift
[1518-09-14 00:48] wakes up
[1518-10-02 00:06] falls asleep
[1518-05-31 00:57] wakes up
[1518-05-31 00:23] falls asleep
[1518-03-28 00:33] wakes up
[1518-11-20 23:56] Guard #1283 begins shift
[1518-03-31 00:50] wakes up
[1518-07-05 00:04] Guard #2213 begins shift
[1518-08-25 00:22] falls asleep
[1518-06-20 00:03] Guard #103 begins shift
[1518-03-29 00:20] falls asleep
[1518-06-27 00:12] falls asleep
[1518-04-09 23:56] Guard #631 begins shift
[1518-06-08 00:45] wakes up
[1518-09-15 00:54] wakes up
[1518-05-22 00:02] Guard #3347 begins shift
[1518-08-09 00:59] wakes up
[1518-04-26 23:58] Guard #829 begins shift
[1518-04-25 23:56] Guard #2251 begins shift
[1518-10-27 00:57] falls asleep
[1518-06-27 00:35] wakes up
[1518-06-03 00:51] falls asleep
[1518-10-06 00:14] wakes up
[1518-10-13 00:23] wakes up
[1518-09-22 00:39] wakes up
[1518-06-02 00:34] wakes up
[1518-09-10 00:34] wakes up
[1518-07-13 00:40] falls asleep
[1518-06-14 00:03] Guard #1283 begins shift
[1518-10-04 00:32] wakes up
[1518-07-23 00:09] falls asleep
[1518-06-27 00:03] Guard #2251 begins shift
[1518-07-27 00:31] falls asleep
[1518-07-03 00:49] wakes up
[1518-10-28 00:37] wakes up
[1518-08-11 00:00] falls asleep
[1518-06-26 00:19] falls asleep
[1518-03-27 00:03] Guard #2251 begins shift
[1518-05-03 00:57] wakes up
[1518-06-28 23:56] Guard #3347 begins shift
[1518-05-05 00:04] Guard #3347 begins shift
[1518-10-14 00:14] wakes up
[1518-09-11 00:57] wakes up
[1518-05-04 00:00] Guard #3319 begins shift
[1518-06-11 00:41] wakes up
[1518-04-29 00:50] wakes up
[1518-09-17 00:41] wakes up
[1518-05-10 00:57] falls asleep
[1518-09-03 00:32] wakes up
[1518-11-01 00:02] Guard #3371 begins shift
[1518-08-01 00:43] wakes up
[1518-04-16 00:23] falls asleep
[1518-05-05 00:27] falls asleep
[1518-07-12 00:52] wakes up
[1518-04-21 00:58] wakes up
[1518-06-05 00:47] falls asleep
[1518-07-30 00:59] wakes up
[1518-08-17 23:57] Guard #631 begins shift
[1518-04-10 00:33] falls asleep
[1518-08-29 00:51] wakes up
[1518-06-02 00:56] falls asleep
[1518-06-28 00:43] wakes up
[1518-07-26 00:55] wakes up
[1518-07-12 23:59] Guard #1283 begins shift
[1518-07-05 00:53] wakes up
[1518-07-04 00:10] falls asleep
[1518-04-06 23:56] Guard #2137 begins shift
[1518-11-22 00:25] wakes up
[1518-08-15 00:52] wakes up
[1518-08-04 00:38] falls asleep
[1518-09-12 00:00] Guard #103 begins shift
[1518-11-10 00:50] wakes up
[1518-07-02 23:52] Guard #631 begins shift
[1518-05-25 23:46] Guard #631 begins shift
[1518-11-03 00:50] wakes up
[1518-06-10 23:50] Guard #439 begins shift
[1518-05-02 23:58] Guard #2539 begins shift
[1518-09-01 00:29] falls asleep
[1518-04-12 00:32] falls asleep
[1518-07-07 00:02] Guard #3371 begins shift
[1518-07-30 00:04] Guard #2129 begins shift
[1518-08-29 00:57] falls asleep
[1518-09-14 00:00] Guard #2213 begins shift
[1518-09-24 00:43] falls asleep
[1518-11-16 00:57] wakes up
[1518-05-04 00:53] falls asleep
[1518-09-29 00:34] falls asleep
[1518-09-03 00:24] falls asleep
[1518-11-16 00:06] falls asleep
[1518-08-04 00:59] wakes up
[1518-04-28 00:07] falls asleep
[1518-10-03 00:54] wakes up
[1518-10-08 00:27] falls asleep
[1518-03-27 00:57] wakes up
[1518-05-01 00:53] wakes up
[1518-06-20 23:59] Guard #1319 begins shift
[1518-04-08 00:02] Guard #1889 begins shift
[1518-06-23 23:59] Guard #241 begins shift
[1518-11-22 00:14] falls asleep
[1518-09-02 00:11] falls asleep
[1518-11-21 00:42] wakes up
[1518-08-19 23:47] Guard #1889 begins shift
[1518-04-07 00:45] falls asleep
[1518-08-25 00:15] wakes up
[1518-08-25 23:57] Guard #829 begins shift
[1518-08-10 23:47] Guard #1213 begins shift
[1518-09-16 00:09] falls asleep
[1518-07-18 00:18] falls asleep
[1518-10-26 00:01] Guard #829 begins shift
[1518-07-14 00:35] falls asleep
[1518-11-03 00:40] falls asleep
[1518-09-18 00:56] wakes up
[1518-10-31 00:10] falls asleep
[1518-08-28 00:56] wakes up
[1518-05-01 00:07] falls asleep
[1518-10-06 00:02] Guard #3347 begins shift
[1518-04-10 00:11] falls asleep
[1518-05-08 00:58] wakes up
[1518-07-24 00:24] wakes up
[1518-08-29 00:59] wakes up
[1518-06-29 00:39] falls asleep
[1518-06-13 00:52] falls asleep
[1518-06-28 00:17] falls asleep
[1518-07-29 00:07] falls asleep
[1518-06-16 00:43] wakes up
[1518-04-22 00:01] Guard #2777 begins shift
[1518-04-08 00:16] falls asleep
[1518-06-13 00:59] wakes up
[1518-06-01 00:35] wakes up
[1518-05-29 00:35] falls asleep
[1518-06-19 00:59] wakes up
[1518-09-13 00:33] falls asleep
[1518-09-28 00:31] wakes up
[1518-06-07 00:00] Guard #3319 begins shift
[1518-06-13 00:00] Guard #3347 begins shift
[1518-05-09 00:48] wakes up
[1518-05-10 00:32] wakes up
[1518-10-23 00:03] Guard #103 begins shift
[1518-10-13 00:17] falls asleep
[1518-07-17 23:59] Guard #1319 begins shift
[1518-06-04 00:38] falls asleep
[1518-09-24 00:53] wakes up
[1518-08-29 00:03] Guard #1889 begins shift
[1518-08-12 00:27] falls asleep
[1518-04-26 00:56] wakes up
[1518-07-02 00:32] wakes up
[1518-10-20 00:56] falls asleep
[1518-09-13 00:50] wakes up
[1518-08-31 00:33] falls asleep
[1518-07-08 00:39] falls asleep
[1518-10-26 00:24] wakes up
[1518-05-27 00:24] falls asleep
[1518-05-15 00:54] falls asleep
[1518-05-10 00:16] falls asleep
[1518-04-19 00:03] Guard #1319 begins shift
[1518-06-09 00:55] falls asleep
[1518-06-26 00:00] Guard #1319 begins shift
[1518-03-28 00:54] wakes up
[1518-05-09 00:46] falls asleep
[1518-11-04 00:33] wakes up
[1518-07-12 00:26] falls asleep
[1518-04-17 00:37] wakes up
[1518-05-06 00:56] wakes up
[1518-05-03 00:34] wakes up
[1518-04-02 00:10] wakes up
[1518-06-10 00:54] wakes up
[1518-03-31 00:29] falls asleep
[1518-07-22 00:39] falls asleep
[1518-09-14 00:52] falls asleep
[1518-05-05 00:17] falls asleep
[1518-06-08 00:00] Guard #2389 begins shift
[1518-07-13 00:59] wakes up
[1518-10-08 00:03] Guard #2251 begins shift
[1518-07-08 00:40] wakes up
[1518-05-14 00:39] wakes up
[1518-07-25 00:33] falls asleep
[1518-08-09 00:48] wakes up
[1518-11-12 00:01] falls asleep
[1518-08-11 00:26] wakes up
[1518-05-27 00:02] Guard #1283 begins shift
[1518-10-29 00:36] wakes up
[1518-11-14 00:43] wakes up
[1518-08-08 00:21] falls asleep
[1518-10-01 00:04] Guard #829 begins shift
[1518-11-12 00:56] falls asleep
[1518-05-12 00:52] falls asleep
[1518-04-29 00:01] Guard #1777 begins shift
[1518-08-13 00:31] falls asleep
[1518-05-07 00:48] falls asleep
[1518-04-05 00:59] wakes up
[1518-10-31 00:04] Guard #3319 begins shift
[1518-10-13 00:49] wakes up
[1518-05-14 00:19] wakes up
[1518-10-20 00:57] wakes up
[1518-09-27 00:57] wakes up
[1518-09-11 00:56] falls asleep
[1518-05-03 00:23] falls asleep
[1518-05-12 00:58] wakes up
[1518-10-08 00:54] wakes up
[1518-09-26 23:48] Guard #1213 begins shift
[1518-08-14 00:48] wakes up
[1518-05-21 00:50] wakes up
[1518-10-19 00:01] Guard #3371 begins shift
[1518-11-09 23:58] Guard #241 begins shift
[1518-10-18 00:42] wakes up
[1518-11-05 23:59] Guard #3347 begins shift
[1518-07-13 23:59] Guard #2137 begins shift
[1518-11-22 00:46] wakes up
[1518-11-17 00:31] falls asleep
[1518-06-15 00:40] falls asleep
[1518-11-09 00:09] falls asleep
[1518-09-10 00:07] falls asleep
[1518-05-15 00:19] falls asleep
[1518-09-23 00:50] wakes up
[1518-06-10 00:52] falls asleep
[1518-10-07 00:39] falls asleep
[1518-09-22 00:36] falls asleep
[1518-05-24 00:12] falls asleep
[1518-08-03 00:00] Guard #1319 begins shift
[1518-06-30 00:24] falls asleep
[1518-04-17 00:31] falls asleep
[1518-06-15 00:00] Guard #1777 begins shift
[1518-05-10 00:51] falls asleep
[1518-06-07 00:32] falls asleep
[1518-07-31 00:04] Guard #1213 begins shift
[1518-10-30 00:03] Guard #2251 begins shift
[1518-09-28 00:46] falls asleep
[1518-08-10 00:41] falls asleep
[1518-06-23 00:49] wakes up
[1518-04-13 00:47] wakes up
[1518-05-21 00:04] Guard #241 begins shift
[1518-05-19 00:19] falls asleep
[1518-04-24 00:39] falls asleep
[1518-05-15 23:56] Guard #1777 begins shift
[1518-08-09 00:15] falls asleep
[1518-04-03 00:10] wakes up
[1518-06-03 00:07] falls asleep
[1518-08-31 00:01] Guard #1213 begins shift
[1518-09-06 00:00] Guard #631 begins shift
[1518-11-05 00:01] Guard #439 begins shift
[1518-09-19 00:53] falls asleep
[1518-06-17 00:39] wakes up
[1518-08-27 00:55] wakes up
[1518-10-23 00:12] falls asleep
[1518-08-05 00:40] falls asleep
[1518-10-13 00:26] falls asleep
[1518-04-28 00:03] Guard #1889 begins shift
[1518-08-19 00:01] Guard #2903 begins shift
[1518-05-15 00:26] wakes up
[1518-06-05 00:37] wakes up
[1518-07-15 00:55] wakes up
[1518-09-17 00:56] wakes up
[1518-06-21 00:29] falls asleep
[1518-09-20 23:59] Guard #241 begins shift
[1518-04-04 00:26] wakes up
[1518-10-21 23:49] Guard #241 begins shift
[1518-09-06 00:15] falls asleep
[1518-09-19 00:33] wakes up
[1518-09-23 00:37] falls asleep
[1518-09-19 00:55] wakes up
[1518-04-02 00:08] falls asleep
[1518-07-06 00:00] Guard #2903 begins shift
[1518-07-13 00:57] falls asleep
[1518-05-23 00:00] Guard #3371 begins shift
[1518-10-02 23:58] Guard #2389 begins shift
[1518-06-24 00:30] wakes up
[1518-10-16 00:07] falls asleep
[1518-09-17 00:30] falls asleep
[1518-08-28 00:34] wakes up
[1518-07-19 00:24] falls asleep
[1518-05-31 23:57] Guard #3319 begins shift
[1518-05-01 00:00] Guard #1889 begins shift
[1518-03-30 00:56] falls asleep
[1518-10-19 23:57] Guard #1889 begins shift
[1518-08-26 23:56] Guard #2389 begins shift
[1518-07-26 00:00] Guard #2389 begins shift
[1518-07-19 00:00] Guard #2903 begins shift
[1518-11-08 00:53] falls asleep
[1518-09-14 23:48] Guard #3319 begins shift
[1518-10-03 23:58] Guard #829 begins shift
[1518-11-22 00:02] Guard #3347 begins shift
[1518-10-21 00:42] falls asleep
[1518-11-15 00:04] falls asleep
[1518-08-25 00:11] falls asleep
[1518-05-02 00:35] wakes up
[1518-10-25 00:37] falls asleep
[1518-11-11 23:48] Guard #103 begins shift
[1518-10-08 23:53] Guard #631 begins shift
[1518-10-23 00:38] falls asleep
[1518-07-16 00:34] falls asleep
[1518-11-05 00:41] falls asleep
[1518-10-31 00:41] falls asleep
[1518-11-09 00:04] Guard #1777 begins shift
[1518-06-18 00:55] wakes up
[1518-04-14 00:18] falls asleep
[1518-06-21 23:58] Guard #1777 begins shift
[1518-04-18 00:17] wakes up
[1518-04-06 00:21] falls asleep
[1518-10-05 00:57] wakes up
[1518-05-29 23:58] Guard #2389 begins shift
[1518-06-18 00:46] falls asleep
[1518-07-27 00:18] falls asleep
[1518-08-04 00:25] wakes up
[1518-06-12 00:25] falls asleep
[1518-04-16 00:55] wakes up
[1518-06-01 00:42] falls asleep
[1518-04-16 00:33] falls asleep
[1518-04-24 23:57] Guard #2389 begins shift
[1518-09-19 00:09] falls asleep
[1518-10-14 00:58] wakes up
[1518-09-16 00:53] wakes up
[1518-06-20 00:26] falls asleep
[1518-09-10 00:57] wakes up
[1518-06-16 23:50] Guard #829 begins shift
[1518-10-11 00:33] falls asleep
[1518-08-17 00:53] wakes up
[1518-08-12 00:03] Guard #1889 begins shift
[1518-05-05 23:59] Guard #2129 begins shift
[1518-10-23 00:49] wakes up
[1518-10-24 00:43] falls asleep
[1518-05-10 00:59] wakes up
[1518-04-11 00:57] falls asleep
[1518-06-15 00:35] wakes up
[1518-08-15 00:00] Guard #1777 begins shift
[1518-08-10 00:12] falls asleep
[1518-07-01 23:52] Guard #439 begins shift
[1518-06-26 00:57] wakes up
[1518-11-23 00:35] wakes up
[1518-11-05 00:51] wakes up
[1518-04-04 23:54] Guard #2389 begins shift
[1518-11-14 23:47] Guard #2903 begins shift
[1518-04-11 00:50] wakes up
[1518-10-26 00:11] falls asleep
[1518-09-06 00:56] wakes up
[1518-05-22 00:55] wakes up
[1518-06-28 00:56] wakes up
[1518-05-24 00:56] wakes up
[1518-08-11 00:46] falls asleep
[1518-06-30 00:56] wakes up
[1518-06-16 00:57] wakes up
[1518-09-27 00:46] falls asleep
[1518-06-01 00:11] falls asleep
[1518-04-12 00:07] falls asleep
[1518-08-04 00:14] falls asleep
[1518-07-22 00:34] falls asleep
[1518-08-07 00:47] falls asleep
[1518-08-29 23:59] Guard #829 begins shift
[1518-11-19 00:19] falls asleep
[1518-03-30 00:01] Guard #3347 begins shift
[1518-09-15 00:19] wakes up
[1518-08-18 00:55] falls asleep
[1518-10-01 00:45] wakes up
[1518-10-29 00:48] falls asleep
[1518-10-21 00:27] wakes up
[1518-07-03 23:56] Guard #1777 begins shift
[1518-08-06 23:59] Guard #241 begins shift
[1518-10-08 00:22] wakes up
[1518-09-22 00:52] falls asleep
[1518-06-23 00:03] Guard #241 begins shift
[1518-11-20 00:57] wakes up
[1518-03-27 23:58] Guard #3319 begins shift
[1518-09-25 00:56] falls asleep
[1518-06-06 00:52] falls asleep
[1518-09-03 23:49] Guard #2137 begins shift
[1518-08-30 00:39] wakes up
[1518-11-12 00:59] wakes up
[1518-10-23 00:25] wakes up
[1518-07-24 00:01] Guard #439 begins shift
[1518-04-12 00:52] falls asleep
[1518-11-23 00:59] wakes up
[1518-11-09 00:37] wakes up
[1518-11-22 23:57] Guard #1889 begins shift
[1518-05-11 00:27] falls asleep
[1518-09-02 00:03] Guard #3371 begins shift
[1518-10-16 00:03] Guard #3319 begins shift
[1518-05-18 23:56] Guard #3319 begins shift
[1518-09-13 00:02] Guard #1319 begins shift
[1518-11-10 00:40] falls asleep
[1518-05-13 23:56] Guard #1213 begins shift
[1518-09-25 00:59] wakes up
[1518-07-01 00:47] wakes up
[1518-10-17 00:13] falls asleep
[1518-10-12 00:31] wakes up
[1518-09-24 00:03] Guard #2137 begins shift
[1518-10-11 00:35] wakes up
[1518-07-10 00:59] wakes up'''

# COMMAND ----------

import collections
import datetime as dt
import re

def inclusive_datetime_range(start, end, delta=dt.timedelta(minutes=1)):
    while start <= end:
        yield start
        start += delta

def get_sleep_minutes(events):
  sleep_minutes = collections.defaultdict(lambda: collections.defaultdict(int))

  # for timestamp in sorted(events):
  for timestamp in inclusive_datetime_range(min(events), max(events)):
    if events[timestamp].startswith('Guard'):
      guard = int(re.findall(r'\d+', events[timestamp])[0])
      is_sleeping = False
    elif events[timestamp] == 'wakes up':
      is_sleeping = False
    elif events[timestamp] == 'falls asleep':
      is_sleeping = True
    
    if is_sleeping:
      sleep_minutes[guard][timestamp.minute] += 1

  return sleep_minutes

events = collections.defaultdict(
  str,
  {dt.datetime.fromisoformat(timestamp): event for timestamp, event in [re.findall(r'\[(.+)\] (.+)', line)[0] for line in inp.splitlines()]}
)

sleep_minutes = get_sleep_minutes(events)
laziest_guard, laziest_guard_minutes = max(sleep_minutes.items(), key=lambda x: sum(x[1].values()))
laziest_guard_minute, _ = max(laziest_guard_minutes.items(), key=lambda x: x[1])

answer = laziest_guard * laziest_guard_minute
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>Strategy 2:</em> Of all guards, which guard is most frequently asleep on the same minute?</p>
# MAGIC <p>In the example above, Guard #<em>99</em> spent minute <em>45</em> asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)</p>
# MAGIC <p><em>What is the ID of the guard you chose multiplied by the minute you chose?</em> (In the above example, the answer would be <code>99 * 45 = 4455</code>.)</p>
# MAGIC </article>

# COMMAND ----------

laziest_guard2, laziest_guard_minutes2 = max(sleep_minutes.items(), key=lambda x: max(x[1].values()))
laziest_guard_minute2, _ = max(laziest_guard_minutes2.items(), key=lambda x: x[1])

answer = laziest_guard2 * laziest_guard_minute2
print(answer)
