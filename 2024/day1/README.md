# 🎄 Advent of Code 2024: Day 1 - Historian Hysteria 🎅

## The Problem

The Chief Historian has gone missing, and the Elvish Senior Historians need help reconciling two incomplete lists of location IDs discovered in his office. The task has two parts:

1. Calculate the **total distance** between the two lists by pairing numbers and summing the absolute differences.
2. Determine a **similarity score** by counting how often each number in the left list appears in the right list, then summing their weighted contributions.

---

## Steps to Solve

### Part 1: Total Distance

1. **Sort both lists** in ascending order.
2. **Pair the numbers** in order: smallest with smallest, second smallest with second smallest, and so on.
3. **Calculate the distance** for each pair as the absolute difference.
4. **Sum all distances** to get the total distance.

#### Example Walkthrough for Part 1:
Given lists:  
- Left: `3, 4, 2, 1, 3, 3`  
- Right: `4, 3, 5, 3, 9, 3`

**Sorted Lists**:  
- Left: `1, 2, 3, 3, 3, 4`  
- Right: `3, 3, 3, 4, 5, 9`

**Pairing and Calculating Distances**:
| Pair       | Distance |  
|------------|----------|  
| (1, 3)     | 2        |  
| (2, 3)     | 1        |  
| (3, 3)     | 0        |  
| (3, 4)     | 1        |  
| (3, 5)     | 2        |  
| (4, 9)     | 5        |  

**Total Distance**:  
`2 + 1 + 0 + 1 + 2 + 5 = 11`

### Part 2: Similarity Score

1. For each number in the **left list**, count how many times it appears in the **right list**.
2. Multiply each number by its occurrence count and add the results to calculate the **similarity score**.

#### Example Walkthrough for Part 2:
Given lists:  
- Left: `3, 4, 2, 1, 3, 3`  
- Right: `4, 3, 5, 3, 9, 3`

**Frequency of Left List Numbers in Right List**:
| Number | Count in Right | Contribution |  
|--------|----------------|--------------|  
| 3      | 3              | `3 * 3 = 9`  |  
| 4      | 1              | `4 * 1 = 4`  |  
| 2      | 0              | `2 * 0 = 0`  |  
| 1      | 0              | `1 * 0 = 0`  |  
| 3      | 3              | `3 * 3 = 9`  |  
| 3      | 3              | `3 * 3 = 9`  |  

**Similarity Score**:  
`9 + 4 + 0 + 0 + 9 + 9 = 31`

---

## My Results

- **Part 1 Answer (Total Distance):** `1882714`  
- **Part 2 Answer (Similarity Score):** `19437052`
