# x = 0.(123)
# => 1000x = 123.(123)
# =>  999x = 123
# =>     x = 123/999
#
# y = 0.(142857)
# => 1000000y = 142857.(142857)
# =>  999999y = 142857
# =>        y = 142857/999999
#
# So 1/7 = something / 999999
# So 999999 mod 7 == 0 and the length of the cycle is the number of digits in 999999. Ie 6.
# We'll call this length "order"
# order is such that (10**order - 1) % n == 0
def recurring_length(n: int) -> int:
    for order in range(1, n):
        if pow(10, order, n) == n - 1:
            return order
    return 0


answer = max(range(7, 1000, 2), key=recurring_length)
print(answer)
