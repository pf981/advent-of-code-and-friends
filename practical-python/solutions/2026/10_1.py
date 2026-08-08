with open("./input/2026/10/input1.txt") as f:
    lines = f.read().splitlines()

beta = next(float(line.split()[1]) for line in lines if line[0] == "β")
gamma = next(float(line.split()[1]) for line in lines if line[0] == "γ")
ITERATIONS = 8500
S = 999.0
I = 1.0
R = 0.0
N = S + I + R

for _ in range(ITERATIONS):
    S, I, R = (
        S + -beta / N * I * S,
        I + beta / N * I * S - gamma * I,
        R + gamma * I,
    )

answer = round(I)
print(answer)
