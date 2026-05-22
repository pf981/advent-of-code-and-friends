# b/n * (b-1)/(n-1) = 1/2
# b*(b-1) / (n*(n-1)) = 1/2
# 2 * b*(b-1) = n * (n - 1)
# n^2 - n - 2*(b^2-b) = 0
#
# Letting x = 2n - 1; y = 2b -1 yields Negative Pell's equation. https://en.wikipedia.org/wiki/Pell%27s_equation#The_negative_Pell's_equation
# x^2 - 2y^2 = -1
#
# Fundamental solution at x=1, y=1
# Next solution x=3, y=2
#
# Recurrence relation
# x_{k+1} = x_{k-2} * x_1 * x_1 + N * x_{k-2} * y_1 * y_1 + 2 * N * y_{k-2} * y_1 * x_1
# y_{k+1} = y_{k-2} * x_1 * x_1 + N * y_{k-2} * y_1 * y_1 + 2 * x_{k-2} * y_1 * x_1
# Where N = 2
target = 10**12

x_1, y_1 = 1, 1
x_prev2, y_prev2 = x_1, y_1
x_prev, y_prev = 3, 2

while True:
    x_next = x_prev2 * x_1 * x_1 + 2 * x_prev2 * y_1 * y_1 + 2 * 2 * y_prev2 * y_1 * x_1
    y_next = y_prev2 * x_1 * x_1 + 2 * y_prev2 * y_1 * y_1 + 2 * x_prev2 * y_1 * x_1

    x_prev2, y_prev2 = x_prev, y_prev
    x_prev, y_prev = x_next, y_next

    n = (x_next + 1) // 2
    b = (y_next + 1) // 2

    if n > target:
        break

answer = b
print(answer)
