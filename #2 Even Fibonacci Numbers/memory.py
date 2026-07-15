a, b = 2, 8
s = 0

while a <= 4_000_000:
    s += a
    a, b = b, 4 * b + a

print(s)
