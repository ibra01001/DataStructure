# GomyCode Checkpoint - README

## Problem 1: Sum of Distinct Elements

### Goal

Find the numbers that appear in only one of the two arrays and add them together.

### Example

A = [3, 1, 7, 9]

B = [2, 4, 1, 9, 3]

Common numbers: 3, 1, 9

Distinct numbers: 7, 2, 4

Sum = 7 + 2 + 4 = 13

### How I solved it

1. Compare each element of A with B.
2. If the element is not found in B, save it.
3. Compare each element of B with A.
4. If the element is not found in A, save it.
5. Add all saved elements.

---

## Problem 2: Dot Product and Orthogonal Vectors

### Goal

Calculate the dot product of two vectors and check if they are orthogonal.

### What is a dot product?

Multiply numbers in the same position and add the results.

Example:

V1 = [1, 2]

V2 = [2, -1]

Dot Product = (1 × 2) + (2 × -1)

Dot Product = 2 - 2

Dot Product = 0

### Orthogonal Vectors

If the dot product is 0, the vectors are orthogonal.

### How I solved it

1. Store vectors in arrays.
2. Use a loop to multiply matching elements.
3. Add all products to get the dot product.
4. If the result is 0, print "Orthogonal".
5. Otherwise, print "Not Orthogonal".

### Procedure vs Function

* Procedure: stores the result in a variable (ps).
* Function: returns the result directly.

Both give the same answer.
