# Project Euler #1 - Memory Optimized
# O(1) time and O(1) memory.
# Uses the arithmetic series formula instead of iterating.

# Returns the sum of numbers from 1 to n.
def series(n):
    return n * (n + 1) // 2

# Sum of multiples of 3 and 5 below 1000.
# Subtract multiples of 15 to avoid counting them twice.
print(
    3 * series(999 // 3) +
    5 * series(999 // 5) -
    15 * series(999 // 15)
)
