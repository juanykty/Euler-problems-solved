a, b, s = 1, 2, 0
while a <= 4_000_000:
    s += a * (a % 2 == 0)
    a, b = b, a + b
print(s)
