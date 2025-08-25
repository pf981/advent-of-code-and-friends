# The answer must lie between
#     sqrt(1020304050607080900) = 1010101010.1 and
#     sqrt(1929394959697989990) = 1389026623.11
# Furthermore, the answer must end in 30 or 70 as they are the only ending
# digits that will result in a 900 at the end of the square
LOWER_BOUND = 1010101000
UPPER_BOUND = 1389026600

for candidate in (
    hundreds + tens
    for hundreds in range(UPPER_BOUND, LOWER_BOUND, -100)
    for tens in (30, 70)
):
    if str(candidate * candidate)[::2] == "1234567890":
        answer = candidate
        break

print(answer)
