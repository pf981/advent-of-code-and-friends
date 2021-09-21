# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/11

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 11: Chronal Charge ---</h2><p>You watch the Elves and their sleigh fade into the distance as they head toward the North Pole.</p>
# MAGIC <p>Actually, you're the one fading. The <span title="wheeeeeeeeeeeeeeeeee">falling sensation</span> returns.</p>
# MAGIC <p>The low fuel warning light is illuminated on your wrist-mounted device. Tapping it once causes it to project a hologram of the situation: a <em>300x300</em> grid of fuel cells and their current power levels, some negative. You're not sure what negative power means in the context of time travel, but it can't be good.</p>
# MAGIC <p>Each fuel cell has a coordinate ranging <em>from 1 to 300</em> in both the X (horizontal) and Y (vertical) direction.  In <code>X,Y</code> notation, the top-left cell is <code>1,1</code>, and the top-right cell is <code>300,1</code>.</p>
# MAGIC <p>The interface lets you select <em>any 3x3 square</em> of fuel cells. To increase your chances of getting to your destination, you decide to choose the 3x3 square with the <em>largest total power</em>.</p>
# MAGIC <p>The power level in a given fuel cell can be found through the following process:</p>
# MAGIC <ul>
# MAGIC <li>Find the fuel cell's <em>rack ID</em>, which is its <em>X coordinate plus 10</em>.</li>
# MAGIC <li>Begin with a power level of the <em>rack ID</em> times the <em>Y coordinate</em>.</li>
# MAGIC <li>Increase the power level by the value of the <em>grid serial number</em> (your puzzle input).</li>
# MAGIC <li>Set the power level to itself multiplied by the <em>rack ID</em>.</li>
# MAGIC <li>Keep only the <em>hundreds digit</em> of the power level (so <code>12<em>3</em>45</code> becomes <code>3</code>; numbers with no hundreds digit become <code>0</code>).</li>
# MAGIC <li><em>Subtract 5</em> from the power level.</li>
# MAGIC </ul>
# MAGIC <p>For example, to find the power level of the fuel cell at <code>3,5</code> in a grid with serial number <code>8</code>:</p>
# MAGIC <ul>
# MAGIC <li>The rack ID is <code>3 + 10 = <em>13</em></code>.</li>
# MAGIC <li>The power level starts at <code>13 * 5 = <em>65</em></code>.</li>
# MAGIC <li>Adding the serial number produces <code>65 + 8 = <em>73</em></code>.</li>
# MAGIC <li>Multiplying by the rack ID produces <code>73 * 13 = <em>949</em></code>.</li>
# MAGIC <li>The hundreds digit of <code><em>9</em>49</code> is <code><em>9</em></code>.</li>
# MAGIC <li>Subtracting 5 produces <code>9 - 5 = <em>4</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>So, the power level of this fuel cell is <code><em>4</em></code>.</p>
# MAGIC <p>Here are some more example power levels:</p>
# MAGIC <ul>
# MAGIC <li>Fuel cell at &nbsp;<code>122,79</code>, grid serial number <code>57</code>: power level <code>-5</code>.</li>
# MAGIC <li>Fuel cell at <code>217,196</code>, grid serial number <code>39</code>: power level &nbsp;<code>0</code>.</li>
# MAGIC <li>Fuel cell at <code>101,153</code>, grid serial number <code>71</code>: power level &nbsp;<code>4</code>.</li>
# MAGIC </ul>
# MAGIC <p>Your goal is to find the 3x3 square which has the largest total power. The square must be entirely within the 300x300 grid. Identify this square using the <code>X,Y</code> coordinate of its <em>top-left fuel cell</em>. For example:</p>
# MAGIC <p>For grid serial number <code>18</code>, the largest total 3x3 square has a top-left corner of <code><em>33,45</em></code> (with a total power of <code>29</code>); these fuel cells appear in the middle of this 5x5 region:</p>
# MAGIC <pre><code>-2  -4   4   4   4
# MAGIC -4  <em> 4   4   4  </em>-5
# MAGIC  4  <em> 3   3   4  </em>-4
# MAGIC  1  <em> 1   2   4  </em>-3
# MAGIC -1   0   2  -5  -2
# MAGIC </code></pre>
# MAGIC <p>For grid serial number <code>42</code>, the largest 3x3 square's top-left is <code><em>21,61</em></code> (with a total power of <code>30</code>); they are in the middle of this region:</p>
# MAGIC <pre><code>-3   4   2   2   2
# MAGIC -4  <em> 4   3   3  </em> 4
# MAGIC -5  <em> 3   3   4  </em>-4
# MAGIC  4  <em> 3   3   4  </em>-3
# MAGIC  3   3   3  -5  -1
# MAGIC </code></pre>
# MAGIC <p><em>What is the <code>X,Y</code> coordinate of the top-left fuel cell of the 3x3 square with the largest total power?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = 4172

# COMMAND ----------

import numpy as np

def get_power_level(x, y, grid_serial_number):
  rack_id = x + 10
  power_level = rack_id * y
  power_level += grid_serial_number
  power_level *= rack_id
  power_level = power_level // 100 % 10
  power_level -= 5
  
  return power_level

def solve(m, min_size=3, max_size=3):
  summed_area_table = m.cumsum(axis=0).cumsum(axis=1)
  result = (float("-inf"), 0, 0, 0)
  
  for size in range(min_size, max_size + 1):
    for x in range(np.shape(m)[0] - size):
      for y in range(np.shape(m)[1] - size):
        area = (
          summed_area_table[x, y] + 
          summed_area_table[x + size, y + size] - 
          summed_area_table[x + size, y] -
          summed_area_table[x, y + size]
        )

        result = max(
          result,
          (area, x + 1, y + 1, size)
        )
        
  return result


m = np.fromfunction(get_power_level, (300, 300), grid_serial_number=inp)
_, x, y, _ = solve(m)

answer = f'{x},{y}'
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You discover a dial on the side of the device; it seems to let you select a square of <em>any size</em>, not just 3x3. Sizes from 1x1 to 300x300 are supported.</p>
# MAGIC <p>Realizing this, you now must find the <em>square of any size with the largest total power</em>. Identify this square by including its size as a third parameter after the top-left coordinate: a 9x9 square with a top-left corner of <code>3,5</code> is identified as <code>3,5,9</code>.</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li>For grid serial number <code>18</code>, the largest total square (with a total power of <code>113</code>) is 16x16 and has a top-left corner of <code>90,269</code>, so its identifier is <code><em>90,269,16</em></code>.</li>
# MAGIC <li>For grid serial number <code>42</code>, the largest total square (with a total power of <code>119</code>) is 12x12 and has a top-left corner of <code>232,251</code>, so its identifier is <code><em>232,251,12</em></code>.</li>
# MAGIC </ul>
# MAGIC <p><em>What is the <code>X,Y,size</code> identifier of the square with the largest total power?</em></p>
# MAGIC </article>

# COMMAND ----------

_, x, y, size = solve(m, 1, 300)

answer = f'{x},{y},{size}'
print(answer)
