import collections

import z3

with open("./2026/input/everybody_codes_e2026_q19_p3.txt") as f:
    text = f.read().strip()
text = """CCMM
YYKK""".strip()

counts = collections.Counter(text.replace("\n", ""))

# K is fixed or can increase

# Is this a flow problem?

"""
K -> K
C -> K, B, G, C
M -> K, B, R, M
Y -> K, G, R, Y
"""

o = z3.Optimize()

k_in = counts["K"]
c_in = counts["C"]
m_in = counts["M"]
y_in = counts["Y"]

k_out, r_out, g_out, b_out = z3.Ints("k_out r_out g_out b_out")
c_to_k, m_to_k, y_to_k = z3.Ints("c_to_k m_to_k y_to_k")
c_to_b, m_to_b = z3.Ints("c_to_b m_to_b")
c_to_g, y_to_g = z3.Ints("c_to_g y_to_g")
m_to_r, y_to_r = z3.Ints("m_to_r y_to_r")
c_out, m_out, y_out = z3.Ints("c_out m_out y_out")

for symbol in [
    k_out,
    r_out,
    g_out,
    b_out,
    c_to_k,
    m_to_k,
    y_to_k,
    c_to_b,
    m_to_b,
    c_to_g,
    y_to_g,
    m_to_r,
    y_to_r,
    c_out,
    m_out,
    y_out,
]:
    o.add(symbol >= 0)

o.add(c_in == c_to_k + c_to_b + c_to_g + c_out)
o.add(m_in == m_to_k + m_to_b + m_to_r + m_out)
o.add(y_in == y_to_k + y_to_g + y_to_r + y_out)

k_out = k_in + c_to_k + m_to_k + y_to_k
r_out = m_to_r + y_to_r
g_out = c_to_g + y_to_g
b_out = c_to_b + m_to_b

xx = max(k_out, r_out)

score = ...

# o.maximize(score)# FIXME: UNCOMMENT
o.check()
# answer = o.model()[score].as_long()
# print(answer)
o.model()
