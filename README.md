# Assignment 3: Sorting and Searching Algorithm Analysis

## Project Overview

In this project I implemented and compared different sorting and searching algorithms.
The goal was to measure their performance on arrays of different sizes and understand how they behave in practice.

I selected:

* Bubble Sort
* Merge Sort
* Binary Search

The program generates arrays, runs algorithms, and measures execution time.

---

## Algorithms

### Bubble Sort

Bubble Sort compares adjacent elements and swaps them if needed.

Time complexity:

* O(n²)

---

### Merge Sort

Merge Sort splits the array and merges it back.

Time complexity:

* O(n log n)

---

### Binary Search

Binary Search works on sorted arrays.

Time complexity:

* O(log n)

---

## Experimental Results

The program was tested on arrays of size:

* 10
* 100
* 1000

Both random and sorted arrays were used.

Results showed that:

* Merge Sort is much faster than Bubble Sort
* Bubble Sort becomes slow on large arrays
* Binary Search is very fast but requires sorted data

---

## Analysis

Performance increases with array size for all algorithms, but at different rates.

Bubble Sort slows down significantly because of quadratic complexity.
Merge Sort scales much better due to logarithmic behavior.

Sorted data slightly improves Bubble Sort performance, but not enough to make it efficient.

Binary Search is efficient because it reduces the search space in half each step.
It only works on sorted arrays, which is why sorting is required before using it.

---

## Screenshots

Program output for different runs and array sizes is included.

---

## Reflection

This assignment helped me understand the difference between simple and efficient algorithms.

I learned that even if an algorithm is easy to implement, it may not be suitable for large datasets.

I also learned how to measure execution time and compare performance in practice.

---

## How to Run

python main.py