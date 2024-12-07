# 🎄 Advent of Code 2024: Day 4 - Ceres Search 🎅

## The Problem

The Historians continue their search for the Chief, but while at the Ceres monitoring station, an Elf asks for help with a word search puzzle. The task is to search for specific patterns in a grid.

- **Part 1**: Count all occurrences of the word "XMAS" in the grid. Words can be horizontal, vertical, diagonal, backwards, or overlapping.
- **Part 2**: Search for "X-MAS" patterns, which consist of two occurrences of "MAS" arranged in an "X" shape.

---

## Steps to Solve

### Part 1: Counting "XMAS"

The goal is to find all occurrences of "XMAS" in the grid.  
Words can appear in:
- Horizontal rows (forwards and backwards).
- Vertical columns (upwards and downwards).
- Diagonal lines (in all four directions).

#### Example Grid:
```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

**Occurrences of XMAS**:  
In the example, "XMAS" appears **18 times**, including overlapping and diagonal cases.

---

### Part 2: Finding "X-MAS" Patterns

Now, you’re looking for "X-MAS" patterns:
1. Two "MAS" sequences arranged in an "X" shape.
2. Each "MAS" can be written forwards or backwards.

The structure of an "X-MAS" is:
```
M.S
.A.
M.S
```

#### Example Grid:
```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

In this example, "X-MAS" appears **9 times**, where each "MAS" in the "X" shape is counted, including all forward and backward variations.

---

## My Results

- **Part 1 Answer (Occurrences of XMAS):** `2462`
- **Part 2 Answer (Occurrences of X-MAS):** `1877`
