import matplotlib.pyplot as plt

LIMIT = 4_000_000

a, b = 1, 2
sum_even = 0

fibonacci_numbers = []
even_numbers = []
even_indices = []

index = 0

while a <= LIMIT:
    fibonacci_numbers.append(a)

    if a % 2 == 0:
        even_numbers.append(a)
        even_indices.append(index)
        sum_even += a

    a, b = b, a + b
    index += 1

print(f"Sum of even Fibonacci numbers: {sum_even}")

plt.figure(figsize=(10, 5))
plt.plot(
    fibonacci_numbers,
    marker="o",
    label="Fibonacci Sequence"
)

plt.scatter(
    even_indices,
    even_numbers,
    s=80,
    label="Even Fibonacci Numbers"
)

plt.title("Fibonacci Sequence up to 4,000,000")
plt.xlabel("Sequence Index")
plt.ylabel("Value")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
