````markdown
# Project Euler #1 - Multiples of 3 or 5

## Problem

If we list all the natural numbers below **10** that are multiples of **3** or **5**, we get:

> 3, 5, 6, 9

The sum of these multiples is **23**.

Find the sum of all the multiples of **3 or 5** below **1000**.

---

## Solutions

This repository contains three different implementations of the same problem.

| File | Description |
|------|-------------|
| `short.py` | Shortest readable Python solution. |
| `memory.py` | Memory-optimized solution using arithmetic series (O(1) time, O(1) space). |
| `visual.py` | Generates a graphical visualization of the multiples using Matplotlib. |

---

## Output

```
233168
```

---

## Complexity

### short.py

| Metric | Value |
|--------|-------|
| Time Complexity | O(n) |
| Space Complexity | O(1) |

---

### memory.py

| Metric | Value |
|--------|-------|
| Time Complexity | O(1) |
| Space Complexity | O(1) |

---

### visual.py

| Metric | Value |
|--------|-------|
| Time Complexity | O(n) |
| Space Complexity | O(n) |

---

## Requirements

Python 3.10+

For the visual version:

```bash
pip install matplotlib
```

---

## Run

Shortest solution

```bash
python short.py
```

Memory optimized solution

```bash
python memory.py
```

Visual solution

```bash
python visual.py
```
