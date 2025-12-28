# Comparative Analysis of Substring Search Algorithms

## Overview
This document presents the performance comparison of three substring search algorithms:
1. **Boyer-Moore**
2. **Knuth-Morris-Pratt (KMP)**
3. **Rabin-Karp**

The algorithms were tested on two different text files ("Article 1" and "Article 2") using two types of search patterns:
* **Existing:** A substring that is present in the text.
* **Fake:** A substring that does not exist in the text.

## Benchmark Results

The time represents the total execution time for 100 iterations (in seconds).

| Algorithm | Text | Pattern Type | Time (sec) |
| :--- | :--- | :--- | :--- |
| **Boyer-Moore** | Article 1 | Existing | **0.00055** |
| KMP | Article 1 | Existing | 0.00211 |
| Rabin-Karp | Article 1 | Existing | 0.00273 |
| | | | |
| **Boyer-Moore** | Article 1 | Fake | **0.00757** |
| KMP | Article 1 | Fake | 0.11043 |
| Rabin-Karp | Article 1 | Fake | 0.17464 |
| | | | |
| **Boyer-Moore** | Article 2 | Existing | **0.00785** |
| KMP | Article 2 | Existing | 0.03264 |
| Rabin-Karp | Article 2 | Existing | 0.04110 |
| | | | |
| **Boyer-Moore** | Article 2 | Fake | **0.01030** |
| KMP | Article 2 | Fake | 0.15708 |
| Rabin-Karp | Article 2 | Fake | 0.24589 |

## Analysis

### 1. Boyer-Moore (The Winner)
* **Performance:** It proved to be the **fastest algorithm** in all test cases.
* **Reasoning:** The efficiency comes from its ability to skip sections of the text. By analyzing the pattern from right to left and using the "Bad Character Heuristic," the algorithm can make large jumps when a mismatch occurs.
* **Observation:** The advantage is most visible in the "Fake" pattern tests. While KMP and Rabin-Karp took over 0.15s, Boyer-Moore finished in ~0.01s. This is because it frequently encountered characters not present in the pattern, allowing it to skip the entire length of the pattern repeatedly.

### 2. Knuth-Morris-Pratt (KMP)
* **Performance:** It consistently ranked **second**.
* **Reasoning:** KMP is efficient because it never re-evaluates characters in the text that have already been matched (linear time complexity). However, it still inspects the text character-by-character more frequently than Boyer-Moore, making it slower in practice for general text searching.

### 3. Rabin-Karp
* **Performance:** It was the **slowest** algorithm in this comparison.
* **Reasoning:** While Rabin-Karp is excellent for multi-pattern searching (plagiarism detection), for a single pattern, the overhead of calculating and updating rolling hashes is computationally more expensive than the direct character comparisons used by Boyer-Moore and KMP.

## Conclusion
Based on the experimental data, **Boyer-Moore** is the most efficient choice for general substring searching in these texts. It significantly outperforms KMP and Rabin-Karp, especially in scenarios where the substring does not exist or is located at the very end of the text.