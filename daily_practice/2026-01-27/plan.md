# Daily Coding Practice - Word Ladder

## Problem Description

**Problem:** [Brief problem title/name]

**Source:** [LeetCode/HackerRank/etc. with problem number if applicable]

**Difficulty:** [Easy/Medium/Hard]

Word Ladder
Solved 
Hard
Company Tags
Hints
You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.

Your goal is to transform beginWord into endWord by following the rules:

You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]

Output: 4
Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".

Example 2:

Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]

Output: 0
Explanation: There is no possible transformation sequence from "cat" to "sag" since the word "sag" is not in the wordList.

Constraints:

1 <= beginWord.length <= 10
1 <= wordList.length <= 100
```

## Approach/Pseudocode

### Initial Thoughts
we could solve it with graph and bfs solution
### Approach
words are nodes and edges are when we can transition from one word to the other.
next we can do bfs on the graph starting with the beginWord and search for the endWord

if startword == endword the solution is 1

### Pseudocode
```
1. generate the adjacency list -> for each new word create a map to an array of its reaching words
2. build_patterns((wordlist))
3. initialize a counter to count the output
4. counter = 0
5. queue = deque([(start, 0)]) = (node, distance)
6. visited = set()
7. if startWord == endword return 1:
8. 
9. while queue:
   1. node = queue.pop()
   2. 
   3. if node == target:
      1. return counter
   4. if node not in visited:
      1. visited.add(node)
      2. for neighbor in graph.get(node, []):
         1. queue.append((neighbor, steps + 1))
         2. 
10. return -1

def buildPatterns(wordList):
    patterns = defaultdict(list)

    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            patterns[pattern].append(word)

    return patterns
```

### Alternative Approaches Considered
[List any other approaches you considered and why you didn't choose them]

## Edge Cases

- [ ] **Empty input:** [How does your solution handle empty arrays, strings, etc.?]
- [ ] **Single element:** [What happens with minimal input?]
- [ ] **Maximum constraints:** [How does it perform at the upper limits?]
- [ ] **Negative numbers/Invalid input:** [How do you handle unexpected input?]
- [ ] **Duplicates:** [If applicable, how do you handle duplicate values?]
- [ ] **[Custom edge case]:** [Add problem-specific edge cases]

## Time & Space Complexity

### Time Complexity
**O([your analysis])** - [Explain why this is the time complexity]

### Space Complexity  
**O([your analysis])** - [Explain the space usage, including auxiliary space]

### Optimization Notes
[Any thoughts on how this could be optimized further, or trade-offs made]

---

**Planning completed at:** 2026-01-27 06:54:43
**Estimated implementation time:** [your estimate]