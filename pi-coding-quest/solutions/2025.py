def shift(s: str, n: int) -> str:
    return "".join(chr((ord(ch) - ord("A") + n) % 26 + ord("A")) for ch in s)


text = """Day          Price ($)          Ticker
1            150.00             TLM
2            93.23              PIH
3            300.50             MTH
4            420.75             IUV
5            3.14               GST
6            720.20             FKE
7            12.57              KVW
8            88.90              TEC
9            210.00             OIL
10           2.64               PHI
11           45.60              CUV
12           33.83              SPI
13           999.99             MEME
14           28.27              MED
15           123.45             BIA
16           65.80              REN
17           6.53               HST
18           250.00             AND
19           18.85              YVO
20           33.33              XOR
21           8.46               NUM
22           777.77             POT
23           9.42               BNO
24           199.99             NOT
25           15.92              SPI
26           850.00             VSL
27           19.94              IVA
28           58.97              GST
29           27.95              PHI
30           21.99              EXW"""

pi = "31415926535897932384626433832795"

result = 0.0
target_tickers = set()
for line in text.splitlines()[1:]:
    day, price_str, ticker = line.split()

    if price_str.replace(".", "") not in pi:
        continue

    manipulated.add(ticker)

    price = float(price_str)
    if not result:
        result = price
    elif int(day) % 2 == 0:
        result *= price
    else:
        result /= price

    target_tickers.add(shift(ticker, int(price_str.replace(".", ""))))

answer1 = str(result).replace(".", "")[:10]
print(answer1)
# 6361428769


cipher_map = """X J P Z Q T M C A O W Y B G D A
N F R S H V K U E X J P Z Q T M
C L O W Y B G D A N F R S H V K
G E X J P Z Q T M P L O W Y B G
D A N F R S H V K U E X J P Z Q
T M A L O W Y B G D A O F I S H
A K U E X J P Z Q T M C L O W Y
O G D A N F R S H V K U E X J P
Y Q T M C L O W Y B G D A N F R
S H V K U E X Y G Z Q T M C L O
D Y B G D A N F R S H V K U D X
J P Z Q T M C L O W Y B G D A N
F R S H V K U E X J P Z Q T M C
D O W Y B G D A N F R S H V K U
E X J P Z Q T M C O O W Y B G D
A N F R S H V K U E X J P Z Q T"""

letters = "".join(cipher_map.split())

answer2 = ""
for line in text.splitlines()[1:]:
    _, price, ticker = line.split()
    if ticker in target_tickers:
        i = int(price.replace(".", "")) % len(letters)
        answer2 += letters[i]

print(answer2)
# GOODPIDAY
