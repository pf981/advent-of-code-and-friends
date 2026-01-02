def int_to_digits(n):
    return [int(d) for d in str(n)]


answer = max(sum(int_to_digits(a**b)) for a in range(100) for b in range(100))
print(answer)
