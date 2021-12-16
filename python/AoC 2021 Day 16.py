# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 16: Packet Decoder ---</h2><p>As you leave the cave and reach open waters, you receive a transmission from the Elves back on the ship.</p>
# MAGIC <p>The transmission was sent using the Buoyancy Interchange Transmission System (<span title="Just be glad it wasn't sent using the BuoyancY Transmission Encoding System.">BITS</span>), a method of packing numeric expressions into a binary sequence. Your submarine's computer has saved the transmission in <a href="https://en.wikipedia.org/wiki/Hexadecimal" target="_blank">hexadecimal</a> (your puzzle input).</p>
# MAGIC <p>The first step of decoding the message is to convert the hexadecimal representation into binary. Each character of hexadecimal corresponds to four bits of binary data:</p>
# MAGIC <pre><code>0 = 0000
# MAGIC 1 = 0001
# MAGIC 2 = 0010
# MAGIC 3 = 0011
# MAGIC 4 = 0100
# MAGIC 5 = 0101
# MAGIC 6 = 0110
# MAGIC 7 = 0111
# MAGIC 8 = 1000
# MAGIC 9 = 1001
# MAGIC A = 1010
# MAGIC B = 1011
# MAGIC C = 1100
# MAGIC D = 1101
# MAGIC E = 1110
# MAGIC F = 1111
# MAGIC </code></pre>
# MAGIC <p>The BITS transmission contains a single <em>packet</em> at its outermost layer which itself contains many other packets. The hexadecimal representation of this packet might encode a few extra <code>0</code> bits at the end; these are not part of the transmission and should be ignored.</p>
# MAGIC <p>Every packet begins with a standard header: the first three bits encode the packet <em>version</em>, and the next three bits encode the packet <em>type ID</em>. These two values are numbers; all numbers encoded in any packet are represented as binary with the most significant bit first. For example, a version encoded as the binary sequence <code>100</code> represents the number <code>4</code>.</p>
# MAGIC <p>Packets with type ID <code>4</code> represent a <em>literal value</em>. Literal value packets encode a single binary number. To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken into groups of four bits. Each group is prefixed by a <code>1</code> bit except the last group, which is prefixed by a <code>0</code> bit. These groups of five bits immediately follow the packet header. For example, the hexadecimal string <code>D2FE28</code> becomes:</p>
# MAGIC <pre><code>110100101111111000101000
# MAGIC VVVTTTAAAAABBBBBCCCCC
# MAGIC </code></pre>
# MAGIC <p>Below each bit is a label indicating its purpose:</p>
# MAGIC <ul>
# MAGIC <li>The three bits labeled <code>V</code> (<code>110</code>) are the packet version, <code>6</code>.</li>
# MAGIC <li>The three bits labeled <code>T</code> (<code>100</code>) are the packet type ID, <code>4</code>, which means the packet is a literal value.</li>
# MAGIC <li>The five bits labeled <code>A</code> (<code>10111</code>) start with a <code>1</code> (not the last group, keep reading) and contain the first four bits of the number, <code>0111</code>.</li>
# MAGIC <li>The five bits labeled <code>B</code> (<code>11110</code>) start with a <code>1</code> (not the last group, keep reading) and contain four more bits of the number, <code>1110</code>.</li>
# MAGIC <li>The five bits labeled <code>C</code> (<code>00101</code>) start with a <code>0</code> (last group, end of packet) and contain the last four bits of the number, <code>0101</code>.</li>
# MAGIC <li>The three unlabeled <code>0</code> bits at the end are extra due to the hexadecimal representation and should be ignored.</li>
# MAGIC </ul>
# MAGIC <p>So, this packet represents a literal value with binary representation <code>011111100101</code>, which is <code>2021</code> in decimal.</p>
# MAGIC <p>Every other type of packet (any packet with a type ID other than <code>4</code>) represent an <em>operator</em> that performs some calculation on one or more sub-packets contained within. Right now, the specific operations aren't important; focus on parsing the hierarchy of sub-packets.</p>
# MAGIC <p>An operator packet contains one or more packets. To indicate which subsequent binary data represents its sub-packets, an operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the <em>length type ID</em>:</p>
# MAGIC <ul>
# MAGIC <li>If the length type ID is <code>0</code>, then the next <em>15</em> bits are a number that represents the <em>total length in bits</em> of the sub-packets contained by this packet.</li>
# MAGIC <li>If the length type ID is <code>1</code>, then the next <em>11</em> bits are a number that represents the <em>number of sub-packets immediately contained</em> by this packet.</li>
# MAGIC </ul>
# MAGIC <p>Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.</p>
# MAGIC <p>For example, here is an operator packet (hexadecimal string <code>38006F45291200</code>) with length type ID <code>0</code> that contains two sub-packets:</p>
# MAGIC <pre><code>00111000000000000110111101000101001010010001001000000000
# MAGIC VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>The three bits labeled <code>V</code> (<code>001</code>) are the packet version, <code>1</code>.</li>
# MAGIC <li>The three bits labeled <code>T</code> (<code>110</code>) are the packet type ID, <code>6</code>, which means the packet is an operator.</li>
# MAGIC <li>The bit labeled <code>I</code> (<code>0</code>) is the length type ID, which indicates that the length is a 15-bit number representing the number of bits in the sub-packets.</li>
# MAGIC <li>The 15 bits labeled <code>L</code> (<code>000000000011011</code>) contain the length of the sub-packets in bits, <code>27</code>.</li>
# MAGIC <li>The 11 bits labeled <code>A</code> contain the first sub-packet, a literal value representing the number <code>10</code>.</li>
# MAGIC <li>The 16 bits labeled <code>B</code> contain the second sub-packet, a literal value representing the number <code>20</code>.</li>
# MAGIC </ul>
# MAGIC <p>After reading 11 and 16 bits of sub-packet data, the total length indicated in <code>L</code> (27) is reached, and so parsing of this packet stops.</p>
# MAGIC <p>As another example, here is an operator packet (hexadecimal string <code>EE00D40C823060</code>) with length type ID <code>1</code> that contains three sub-packets:</p>
# MAGIC <pre><code>11101110000000001101010000001100100000100011000001100000
# MAGIC VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>The three bits labeled <code>V</code> (<code>111</code>) are the packet version, <code>7</code>.</li>
# MAGIC <li>The three bits labeled <code>T</code> (<code>011</code>) are the packet type ID, <code>3</code>, which means the packet is an operator.</li>
# MAGIC <li>The bit labeled <code>I</code> (<code>1</code>) is the length type ID, which indicates that the length is a 11-bit number representing the number of sub-packets.</li>
# MAGIC <li>The 11 bits labeled <code>L</code> (<code>00000000011</code>) contain the number of sub-packets, <code>3</code>.</li>
# MAGIC <li>The 11 bits labeled <code>A</code> contain the first sub-packet, a literal value representing the number <code>1</code>.</li>
# MAGIC <li>The 11 bits labeled <code>B</code> contain the second sub-packet, a literal value representing the number <code>2</code>.</li>
# MAGIC <li>The 11 bits labeled <code>C</code> contain the third sub-packet, a literal value representing the number <code>3</code>.</li>
# MAGIC </ul>
# MAGIC <p>After reading 3 complete sub-packets, the number of sub-packets indicated in <code>L</code> (3) is reached, and so parsing of this packet stops.</p>
# MAGIC <p>For now, parse the hierarchy of the packets throughout the transmission and <em>add up all of the version numbers</em>.</p>
# MAGIC <p>Here are a few more examples of hexadecimal-encoded transmissions:</p>
# MAGIC <ul>
# MAGIC <li><code>8A004A801A8002F478</code> represents an operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of <code><em>16</em></code>.</li>
# MAGIC <li><code>620080001611562C8802118E34</code> represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of <code><em>12</em></code>.</li>
# MAGIC <li><code>C0015000016115A2E0802F182340</code> has the same structure as the previous example, but the outermost packet uses a different length type ID. This packet has a version sum of <code><em>23</em></code>.</li>
# MAGIC <li><code>A0016C880162017C3686B18A3D4780</code> is an operator packet that contains an operator packet that contains an operator packet that contains five literal values; it has a version sum of <code><em>31</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>Decode the structure of your hexadecimal-encoded BITS transmission; <em>what do you get if you add up the version numbers in all packets?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '420D5A802122FD25C8CD7CC010B00564D0E4B76C7D5A59C8C014E007325F116C958F2C7D31EB4EDF90A9803B2EB5340924CA002761803317E2B4793006E28C2286440087C5682312D0024B9EF464DF37EFA0CD031802FA00B4B7ED2D6BD2109485E3F3791FDEB3AF0D8802A899E49370012A926A9F8193801531C84F5F573004F803571006A2C46B8280008645C8B91924AD3753002E512400CC170038400A002BCD80A445002440082021DD807C0201C510066670035C00940125D803E170030400B7003C0018660034E6F1801201042575880A5004D9372A520E735C876FD2C3008274D24CDE614A68626D94804D4929693F003531006A1A47C85000084C4586B10D802F5977E88D2DD2898D6F17A614CC0109E9CE97D02D006EC00086C648591740010C8AF14E0E180253673400AA48D15E468A2000ADCCED1A174218D6C017DCFAA4EB2C8C5FA7F21D3F9152012F6C01797FF3B4AE38C32FFE7695C719A6AB5E25080250EE7BB7FEF72E13980553CE932EB26C72A2D26372D69759CC014F005E7E9F4E9FA7D3653FCC879803E200CC678470EC0010E82B11E34080330D211C663004F00101911791179296E7F869F9C017998EF11A1BCA52989F5EA778866008D8023255DFBB7BD2A552B65A98ECFEC51D540209DFF2FF2B9C1B9FE5D6A469F81590079160094CD73D85FD2699C5C9DCF21F0700094A1AC9EDA64AE3D37D34200B7B401596D678A73AFB2D0B1B88057230A42B2BD88E7F9F0C94F1ECB7B0DD393489182F9802D3F875C00DC40010F8911C61F8002111BA1FC2E400BEA5AA0334F9359EA741892D81100B83337BD2DDB4E43B401A800021F19A09C1F1006229C3F8726009E002A12D71B96B8E49BB180273AA722468002CC7B818C01B04F77B39EFDF53973D95ADB5CD921802980199CF4ADAA7B67B3D9ACFBEC4F82D19A4F75DE78002007CD6D1A24455200A0E5C47801559BF58665D80'

# COMMAND ----------

import collections
import math


def bin_to_int(binary):
  return int(''.join(binary), 2)


def take_binary(binary, n):
  return collections.deque(binary.popleft() for _ in range(n))


def take_int(binary, n):
  return bin_to_int(take_binary(binary, n))


def parse_literal(binary):
  result = []
  do_continue = True
  while do_continue:
    do_continue = take_int(binary, 1)
    result.extend(take_binary(binary, 4, ))
      
  return [bin_to_int(result)]


def parse_operator_n_bits(binary):
  total_length = take_int(binary, 15)
  subpackets = take_binary(binary, total_length)
  
  result = []
  while subpackets:
    result.append(parse_packet(subpackets))

  return result


def parse_operator_n_subpackets(binary):
  n_subpackets = take_int(binary, 11)
  
  result = []
  for _ in range(n_subpackets):
    result.append(parse_packet(binary))

  return result


def parse_packet(binary):
  global global_version_sum
  
  version = take_int(binary, 3)
  global_version_sum += version
  
  type_id = take_int(binary, 3)
  
  if type_id == 4:
    parser = parse_literal
  elif take_int(binary, 1) == 0:
    parser = parse_operator_n_bits
  else:
    parser = parse_operator_n_subpackets
    
  subpackets = parser(binary)
  
  f = [
    sum,
    math.prod,
    min,
    max,
    lambda l: l[0],
    lambda l: l[0] > l[1],
    lambda l: l[0] < l[1],
    lambda l: l[0] == l[1]
  ][type_id]

  return f(subpackets)


def evaluate(transmission):
  binary = collections.deque(bin(int(transmission, 16))[2:])

  while len(binary) % 4 != 0:
    binary.appendleft('0')

  return parse_packet(binary)


global_version_sum = 0
evaluation = evaluate(inp)

answer = global_version_sum
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.</p>
# MAGIC <p>Literal values (type ID <code>4</code>) represent a single number as described above. The remaining type IDs are more interesting:</p>
# MAGIC <ul>
# MAGIC <li>Packets with type ID <code>0</code> are <em>sum</em> packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.</li>
# MAGIC <li>Packets with type ID <code>1</code> are <em>product</em> packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.</li>
# MAGIC <li>Packets with type ID <code>2</code> are <em>minimum</em> packets - their value is the minimum of the values of their sub-packets.</li>
# MAGIC <li>Packets with type ID <code>3</code> are <em>maximum</em> packets - their value is the maximum of the values of their sub-packets.</li>
# MAGIC <li>Packets with type ID <code>5</code> are <em>greater than</em> packets - their value is <em>1</em> if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is <em>0</em>. These packets always have exactly two sub-packets.</li>
# MAGIC <li>Packets with type ID <code>6</code> are <em>less than</em> packets - their value is <em>1</em> if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is <em>0</em>. These packets always have exactly two sub-packets.</li>
# MAGIC <li>Packets with type ID <code>7</code> are <em>equal to</em> packets - their value is <em>1</em> if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is <em>0</em>. These packets always have exactly two sub-packets.</li>
# MAGIC </ul>
# MAGIC <p>Using these rules, you can now work out the value of the outermost packet in your BITS transmission.</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li><code>C200B40A82</code> finds the sum of <code>1</code> and <code>2</code>, resulting in the value <code><em>3</em></code>.</li>
# MAGIC <li><code>04005AC33890</code> finds the product of <code>6</code> and <code>9</code>, resulting in the value <code><em>54</em></code>.</li>
# MAGIC <li><code>880086C3E88112</code> finds the minimum of <code>7</code>, <code>8</code>, and <code>9</code>, resulting in the value <code><em>7</em></code>.</li>
# MAGIC <li><code>CE00C43D881120</code> finds the maximum of <code>7</code>, <code>8</code>, and <code>9</code>, resulting in the value <code><em>9</em></code>.</li>
# MAGIC <li><code>D8005AC2A8F0</code> produces <code>1</code>, because <code>5</code> is less than <code>15</code>.</li>
# MAGIC <li><code>F600BC2D8F</code> produces <code>0</code>, because <code>5</code> is not greater than <code>15</code>.</li>
# MAGIC <li><code>9C005AC2F8F0</code> produces <code>0</code>, because <code>5</code> is not equal to <code>15</code>.</li>
# MAGIC <li><code>9C0141080250320F1802104A08</code> produces <code>1</code>, because <code>1</code> + <code>3</code> = <code>2</code> * <code>2</code>.</li>
# MAGIC </ul>
# MAGIC <p><em>What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = evaluation
print(answer)
