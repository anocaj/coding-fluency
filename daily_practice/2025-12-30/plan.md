# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** Course Schedule (Prerequisites)		

**Source:** LeetCode #207

**Difficulty:** Medium

### Problem Statement

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

### Examples
```
Input: [example input]
Output: [example output]
Explanation: [brief explanation if needed]
```

## Approach/Pseudocode

### Initial Thoughts
we can do topological search and when we detect a loop or a component return False
- a loop or disconnected component happens when the number of resulting traversed nodes is not equal to the number of courses



### Approach
my approach would be to parse the prerequisits to n array where i is the course and the value is the list of prerequisits
also we need to store the indegree of each nodes. 

we start traversing the graph by selecting the nodes with indegree[node] == 0. we add them to a queue
### Pseudocode
```
dependencies = defaultdict(list) # dependent node -> in
indegree = defaultdict(int)
all_nodes = set()
resulting = node

1. for edge in prerequisits:
        source = preq[1]
        target = preq[0]
        all_nodes.add(source)
        all_nodes.add(target)

        dependencies[source] = target
        indegree[target] += 1

2. for node in all_nodes:
    if indegree[node] == 0
        queue.append(node)



3. while queue:
        node = queue.popleft()
        result.append(source)
    
        for target in dependencies[source]:
            if indegree[target] == 0:
                queue.append(target)
            indegree[target] -= 1

4. return True if len(all_nodes) != len()
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

**Planning completed at:** 2025-12-30 09:07:08
**Estimated implementation time:** 09:40:08