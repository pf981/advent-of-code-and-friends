n = int(input())

s = n * (n + 1) // 2
if s % 2:
    print("NO")
    exit(0)

group1 = []
group2 = []
s1 = s2 = 0
for i in reversed(range(1, n + 1)):
    if s1 <= s2:
        group1.append(i)
        s1 += i
    else:
        group2.append(i)
        s2 += i

print("YES")
print(len(group1))
print(*group1)
print(len(group2))
print(*group2)
