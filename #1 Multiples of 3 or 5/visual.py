```python
# Project Euler #1 - Visual
# Graphically display the multiples of 3 or 5 below 1000.

import matplotlib.pyplot as plt

# Find all multiples of 3 or 5 below 1000
numbers = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
total = sum(numbers)

# Create the plot
plt.figure(figsize=(12, 4))
plt.bar(numbers, numbers)

# Title and labels
plt.title(f"Project Euler #1\nSum = {total:,}")
plt.xlabel("Multiples of 3 or 5")
plt.ylabel("Value")

# Show the result
plt.tight_layout()
plt.show()
```
