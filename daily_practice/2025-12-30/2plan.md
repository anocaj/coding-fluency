# Daily Coding Practice - Passage Pathing

## Problem Description

**Problem:** Passage Pathing	
**Source:** Advent of Code 2021 Day 12

**Difficulty:** Medium

--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end
This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end
Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

Here is a slightly larger example:

dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
The 19 paths through it are as follows:

start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
Finally, this even larger example has 226 paths through it:

fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
How many paths through this cave system are there that visit small caves at most once?

## Approach/Pseudocode

### Initial Thoughts
we have a list of edges. first we want to parse it to an adjacencyList which stores for each node the corresponding edges.
further we need to track visited nodes ->  mark visited by adding it to an array
further we need to distinguish nodes that can be visited only once or multiple times -> if UPPER(node) == node -> don't mark as visited. 
    what happens when we dont mark the upper nodes as visited

what happens if there is an infinit loop? how do we stop that? we should be able to cache the paths of nodes that allow further tracking. 

what about disconnected componentes? -> return no path if target cannot be reached.

### Approach
I would approach the problem by using DFS. the goal is to find every possible path from source to target


### Pseudocode
```
# 1. parse list of edges to adjacency list:
    adj = defaultdict(list)
    for edge in edges:
        adj[edge[0]] = adj[edge[0]].append(edge[1])
        adj[edge[1]] = adj[edge[1]].append(edge[0])
        

# 2. 
    def dfs(graph, start, end, ,path=[]):
        path = path + [start]

        # base case: 
        if start == end:
            return [path]
        if start not in graph: 
            return []

        paths = []
        # recurrence relation:
        for neighbor in graph(start):
            newpaths = dfs(graph,node, end,path)
            for p in newpaths:
                paths.append(p)
        return paths

# now we don't handle the special nodes that can be visited multiple times

# 3. dfs(start)
    dfs(adj,"start","end")
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

**Planning completed at:** 16:30
**Estimated implementation time:** 17:10 -> actually 17:05 with help