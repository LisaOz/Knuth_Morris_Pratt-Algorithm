'''
This code is the implementation of the Knuth-Morris-Pratt (KMP) string matching algorithm,
which searches for occurrences of a pattern within a text.
'''

# calculation of the prefix table
t = 'lulula'  # Pattern that is being looked for in the text
p = [0] * len(t)  # Prefix table with a list of zeros
j = 0  # Length of the previous longest prefix that is also a suffix
i = 1  # Current position in the pattern. Starts from 1 since p[0] is always 0

# Loop runs until 'i' reaches the end of the pattern.
# If the character at position 'j' matches the character at position 'i' in the pattern,
# set the prefix table at position 'i' to 'j + 1'
while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1 # Move to the next position
        j += 1

    # If there is no match and 'j' is 0, set the prefix at position 'i' to 0
    else:
        if j == 0:
            p[i] = 0
            i += 1  # Move to the next position
        else:
            j = p[j - 1]  # If there is no match and 'j' is not 0, set 'j' to 'j - 1'
print("Prefix table:", p)

# Pattern Matching
t1 = 'lululam'  # Text in which we are searching for the pattern 't'
m = len(t)  # length of the pattern t
n = len(t1)  # length of the pattern t1

j = 0  # index to track the position in the pattern
i = 0 # index to track the position in the text

# Run loop until 'i' reach the end of the text
while i < n:
    if t1[i] == t[j]:
        i += 1
        j += 1

        # if 'j' reaches the end of the pattern, the pattern is found
        if j == m:
            print("Pattern found at index", i - j)
            break

    # If there is no match and 'j' is greater than 0, set 'j' to the value
    # of the prefix table at position 'j - 1'
    else:
        if j > 0:
            j = p[j - 1]
        else:
            i += 1

# If the end of the text is reached and the pattern is not found
if i == n:
    print("Pattern not found")
