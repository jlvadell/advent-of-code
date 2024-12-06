# 🎄 Advent of Code 2024: Day 3 - Mull It Over 🎅

## The Problem

The North Pole Toboggan Rental Shop's computer is malfunctioning, and the program in memory is corrupted. Your task is to analyze the corrupted memory to extract valid multiplication instructions (`mul(X,Y)`) and compute their results. In **Part 2**, you must also handle conditional instructions (`do()` and `don't()`) that enable or disable `mul` operations.

---

## Steps to Solve

### Part 1: Extract Valid Multiplication Instructions

A valid multiplication instruction has the format `mul(X,Y)`, where:
- `X` and `Y` are integers (1-3 digits).
- There are no invalid characters in the instruction.

#### Example:
For the input:
```
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```
The valid instructions are:
- `mul(2,4)` → Result: `2 * 4 = 8`
- `mul(5,5)` → Result: `5 * 5 = 25`
- `mul(11,8)` → Result: `11 * 8 = 88`
- `mul(8,5)` → Result: `8 * 5 = 40`

The sum of the results is:
```
8 + 25 + 88 + 40 = 161
```

---

### Part 2: Handle Conditional Instructions (`do()` and `don't()`)

The memory now includes two additional instructions:
- `do()` enables future `mul` instructions.
- `don't()` disables future `mul` instructions.

At the start, `mul` instructions are enabled. Only the most recent `do()` or `don't()` affects subsequent `mul` operations.

#### Example:
For the input:
```
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```
The valid instructions are:
- `mul(2,4)` → Enabled → Result: `2 * 4 = 8`
- `mul(5,5)` → Disabled by `don't()`
- `mul(32,64)` → Disabled by `don't()`
- `mul(11,8)` → Disabled by `don't()`
- `mul(8,5)` → Re-enabled by `do()` → Result: `8 * 5 = 40`

The sum of the results is:
```
8 + 40 = 48
```

---

## My Results

- **Part 1 Answer (Sum of All Valid Multiplications):** `179834255`
- **Part 2 Answer (Sum of Enabled Multiplications):** `80570939`