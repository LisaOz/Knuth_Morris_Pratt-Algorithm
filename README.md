# Knuth-Morris-Pratt Algorithm
This repository contains the implementation of the Knuth-Morris-Pratt (KMP) Algortithm in Python.

## Overview
The KMP Algorithm is an efficient string searching algorithm. It is particularly useful for finding occurrences 
of a pattern within a text in linear time complexity, O(m + n), where m is the length of the pattern
and n is the length of the text.

## Implementation Steps
### 1. Creating the Partial Match Table (Prefix Table):
   - Initialize a pattern array 'p' with zeros for the length of the pattern.
   - Set index 'j' to 0 (pattern index) and [i] to 1 (text index).
### 2. Building the Partial Match Table:
  - Iterate through the text while i is less than the length of the text.
  - If characters t[j] (pattern) and t[i] (text) match:
    - increment 'j' and set p[i] to 'j + 1'.
  - if characters do not match:
    -  if 'j' is 0, set 'p[i] to 0 (no partial match).
    -  Otherwise, update 'j' using the previous match information from 'p' and continue.

### 3. Searching for the Pattern in the Text:
  - Initialize 'j' (pattern index) and 'i' (text index) to 0.
  - Iterate through the text:
      - If characters match (t1[i] == t[j]), increment both 'i' and 'j'.
      - If 'j' equals the length of the pattern('m'), print the index where the pattern starts in the text.
      - If characters do not match and 'j' is not 0, update 'j' using the partial match table 'p'.
      - If characters do not match and 'j' is 0, increment 'i'.
    
### 4. Output:
  - If the pattern is found, print "Pattern found at index <index>".
  - If the pattern is not found, print "The pattern is not found."


