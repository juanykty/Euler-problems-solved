```python
# Project Euler #1
# Find the sum of all numbers below 1000
# that are multiples of 3 or 5.

print(sum(
    i                    # Current number
    for i in range(1000) # Numbers from 0 to 999
    if i % 3 == 0 or i % 5 == 0
))
```

### Output

```
233168
```
