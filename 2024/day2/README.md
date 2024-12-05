# 🎄 Advent of Code 2024: Day 2 - Red-Nosed Reports 🎅

## The Problem

The engineers at the Red-Nosed Reindeer reactor need help analyzing safety reports. Each report is a list of levels, and the safety of a report is determined by strict rules:

1. Levels must be either **increasing** or **decreasing**.
2. The difference between adjacent levels must be between **1 and 3 (inclusive)**.

In **Part 2**, a "Problem Dampener" allows for the removal of one "bad" level to potentially make an otherwise unsafe report count as safe.

---

## Steps to Solve

### Part 1: Safe Reports (Strict Rules)

A report is **safe** if:
- All levels are either increasing or decreasing.
- Any two adjacent levels differ by at least 1 and at most 3.

#### Example Reports:
```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```
| Report       | Result  | Reason                                                                 |
|--------------|---------|------------------------------------------------------------------------|
| `7 6 4 2 1`  | Safe    | Levels are all decreasing, with differences of 1 or 2.                |
| `1 2 7 8 9`  | Unsafe  | The difference between `2` and `7` is 5, which exceeds the allowed range. |
| `9 7 6 2 1`  | Unsafe  | The difference between `6` and `2` is 4, which exceeds the allowed range. |
| `1 3 2 4 5`  | Unsafe  | The levels change from increasing (`1 3`) to decreasing (`3 2`).      |
| `8 6 4 4 1`  | Unsafe  | The pair `4 4` is neither increasing nor decreasing.                  |
| `1 3 6 7 9`  | Safe    | Levels are all increasing, with differences of 1, 2, or 3.            |

**In this example, 2 reports are safe.**

---

### Part 2: Safe Reports (With the Problem Dampener)

With the **Problem Dampener**, a report can tolerate one "bad" level:
- If removing a single level makes the report safe, it counts as safe.

#### Updated Example Reports:
| Report       | Result  | Reason                                                                 |
|--------------|---------|------------------------------------------------------------------------|
| `7 6 4 2 1`  | Safe    | No levels need to be removed; still meets criteria.                   |
| `1 2 7 8 9`  | Unsafe  | Removing any level does not resolve the large jump (5).               |
| `9 7 6 2 1`  | Unsafe  | Removing any level does not resolve the large drop (4).               |
| `1 3 2 4 5`  | Safe    | Removing `3` makes the sequence increasing: `1 2 4 5`.               |
| `8 6 4 4 1`  | Safe    | Removing the third `4` makes the sequence decreasing: `8 6 4 1`.      |
| `1 3 6 7 9`  | Safe    | No levels need to be removed; still meets criteria.                   |

**With the Problem Dampener, 4 reports are safe.**

---

## My Results

- **Part 1 Answer (Strict Rules):** `379`  
- **Part 2 Answer (With Problem Dampener):** `430`
