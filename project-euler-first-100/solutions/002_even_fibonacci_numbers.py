from typing import Generator


def fib() -> Generator[int, None, None]:
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


answer = 0
for num in fib():
    if num > 4000000:
        break
    if num % 2 == 0:
        answer += num
print(answer)
