import math

with open("./input/2026/10/input2.txt") as f:
    lines = f.read().splitlines()

beta = next(float(line.split()[1]) for line in lines if line[0] == "β")
gamma = next(float(line.split()[1]) for line in lines if line[0] == "γ")
TARGET = 990
S = 999.0
I = 1.0
R = 0.0
N = S + I + R

h = 0.05
t = 0.0
while R < TARGET:
    S, I, R = (
        S + h * (-beta / N * I * S),
        I + h * (beta / N * I * S - gamma * I),
        R + h * (gamma * I),
    )
    t += h

answer = math.ceil(t) // 60 + 1
print(answer)
