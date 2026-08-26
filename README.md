# security-pin-and-tree-decor-combinatorics
Python solutions for two combinatorics problems: counting valid security PINs under parity/prime constraints (with modular exponentiation for large n) and generating all ordered accessory combinations for tree decoration.
# Security PIN & Tree Decor Combinatorics

Python solutions to two combinatorics-style coding problems:

1. **Security PIN Counter** — Count valid PINs of length `n` under parity/prime digit constraints, computed efficiently modulo `10^9 + 7` for `n` up to `10^15`.
2. **Christmas Tree Accessory Combinations** — Generate all ordered arrangements of bells, candies, and balloons that use exactly `N` accessories, respecting per-item availability.

---

## 1. Security PIN Counter

### Problem
Given an integer `n`, count how many valid PINs of length `n` exist, where:
- Digits at **even indices** (0, 2, 4, ...) must be **even** digits: `{0, 2, 4, 6, 8}`
- Digits at **odd indices** (1, 3, 5, ...) must be **prime** digits: `{2, 3, 5, 7}`

Since `n` can be as large as `10^15`, the answer is returned modulo `10^9 + 7`.

### Approach
- Even-index positions each have 5 valid choices.
- Odd-index positions each have 4 valid choices.
- Number of even-index positions: `⌈n/2⌉`
- Number of odd-index positions: `⌊n/2⌋`
- Total = `5^(even_count) * 4^(odd_count) mod (10^9 + 7)`, computed with fast modular exponentiation (`pow(base, exp, mod)`) in O(log n) time.

### File
`pin_counter.py`

### Usage
```bash
python pin_counter.py
# Input: n (single integer via stdin)
```

**Examples**

| Input | Output | Explanation |
|-------|--------|-------------|
| `1`   | `5`    | Valid PINs: 0, 2, 4, 6, 8 |
| `3`   | `100`  | 5 choices × 4 choices × 5 choices = 100 |

---

## 2. Christmas Tree Accessory Combinations

### Problem
Given `N` (accessories needed) and counts of Bells (`B`), Candies (`C`), and Balloons (`A`), print every distinct ordered sequence of length `N` that can be formed, respecting the available count of each item and trying items in priority order **B → C → A**.

### Approach
- Backtracking (DFS): build strings position by position.
- At each position, attempt `B` first, then `C`, then `A`, only if that item's remaining count is greater than 0.
- Recurse with decremented counts; once the string reaches length `N`, record it.
- This produces output in a deterministic, priority-ordered sequence matching the expected format.

### File
`tree_decor_combinations.py`

### Usage
```bash
python tree_decor_combinations.py
# Input line 1: n
# Input line 2: B C A (space-separated)
```

**Examples**

**Input**
```
2
0 1 1
```
**Output**
```
CA
AC
```

**Input**
```
3
1 1 1
```
**Output**
```
BCA
BAC
CBA
CAB
ABC
ACB
```

---

## Constraints Summary

| Problem | Constraints |
|---|---|
| Security PIN Counter | `1 ≤ n ≤ 10^15` |
| Tree Decor Combinations | `1 ≤ N ≤ 10`, `0 ≤ a, b, c ≤ 20` |

---

## Tech
- Language: Python 3
- No external dependencies

## Repository Structure
```
.
├── pin_counter.py
├── tree_decor_combinations.py
└── README.md
```
