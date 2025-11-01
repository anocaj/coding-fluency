# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** 2434. Using a Robot to Print the Lexicographically Smallest String

**Source:** [LeetCode]

**Difficulty:** [Medium]

### Problem Statement
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 
Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.

### Examples
```

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
```

## Approach/Pseudocode

### Initial Thoughts
[Write down your first thoughts about the problem. 
queue like approach but also stack

strings are immutable and we cannot  inplace change the strings we need to create new strings:



we have two operations: a take first element of s and push to stack t. how do i take an element    
t += s[0]
s = s[1:]

second operation is popping from t. 
popped = t[-1]      # get the last character
t = t[:-1]          # remove it from t

What patterns do you recognize? 

What data structures might be useful?
queue, stack
wehat is the lexicographically smallest string?  lexicographically smallest string is the string that would appear first in dictionary order


]

At any point:
	•	Let min_char be the smallest character remaining in s.
	•	If the last character in t is ≤ min_char, pop it from t and write it to p.
	•	Otherwise, move the next character from s to t.

This ensures we always write the smallest possible next character.

### Approach

find smallest char and ensure to run t after identifying it. 

once smallest is identified we can think of the next smallest one. 

we could go through s in O(n) and identify the smallest values that should be in the beginning
    - 


### Pseudocode
```
1. count char in s 
2. for c in s append t and reduce counter of that char
3. while t and t[-1] min([k for k in counter if counter[k] > 0], default='z'):
    p.append(t.pop())
4. while t:
p.append(t.pop())

return "".join(p)
```

### Alternative Approaches Considered
	•	Using recursion: would simulate all sequences of moves (too slow, exponential).
	•	Using brute force with permutations: not feasible due to input size (up to 10⁵).
## Edge Cases

- [ ] **Empty input:** If s is empty, output is "".
- [ ] **Single element:** e.g., s = "a" → output "a".
- [ ] **Maximum constraints:** Works efficiently with s of length 10⁵ using O(n) approach. when using min_suffx
- [ ] **Duplicates:** Handled correctly via counter or min_suff.
- [ ] **Non-lowercase input:** : Problem constraint prevents this; otherwise, validation needed.


## Time & Space Complexity

### Time Complexity
**O(n)** - each character is pushed and popped at most once, and compting min_suff is O(n).

### Space Complexity  
**O(n)** - for the stack t and output p and min_suff if used

### Optimization Notes
- avoid computing min() repeatedly over remaining characters by precomputing min_suff[i] for O(1) lookups.
- using a stack ensures each character is handled at most twice (push + pop)
 ---

**Planning completed at:** 2025-11-01 11:31:59
**Estimated implementation time:** 20-30 min