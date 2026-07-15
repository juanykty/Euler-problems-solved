# Project Euler #1 - Multiples of 3 or 5

## Problem

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get:

```
3, 5, 6, 9
```

The sum of these multiples is **23**.

Find the sum of all the multiples of 3 or 5 below **1000**.

---

## Solutions

| File          | Description                                                                |
| ------------- | -------------------------------------------------------------------------- |
| **short.py**  | Shortest readable Python solution.                                         |
| **memory.py** | Memory-optimized solution using arithmetic series (O(1) time, O(1) space). |
| **visual.py** | Graphically displays the solution using Matplotlib.                        |

---

## Output

```
233168
```

---

## Complexity

| File          | Time | Space |
| ------------- | ---- | ----- |
| **short.py**  | O(n) | O(1)  |
| **memory.py** | O(1) | O(1)  |
| **visual.py** | O(n) | O(n)  |

---

## Requirements

* Python 3.10+
* Matplotlib (only for **visual.py**)

Install dependencies:

```bash
pip install matplotlib
```

---

## Usage

Run the shortest solution:

```bash
python short.py
```

Run the memory-optimized solution:

```bash
python memory.py
```

Run the visual solution:

```bash
python visual.py
```
