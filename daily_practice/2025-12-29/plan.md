# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:**  Task Scheduling

**Source:** Helsing

**Difficulty:** Mediuem

### Problem Statement
#### 3. Task Scheduling

This problem is encountered in many day-to-day tasks when tasks that can sometimes occur in
parallel and sometimes have dependencies on another need to be performed. Consider a cooking
recipe: You might need to wash and chop some vegetables while preheating the oven; while the
vegetables are roasting you can pan fry your favourite protein and prepare a sauce and finally put
everything together, give it a finishing touch and serve it.

The tasks to cook the dish described above may be described in the problem input as:
```sh
preheat_oven
wash_vegetables
chop_vegetables wash_vegetables
bake_vegetables chop_vegetables preheat_oven
prepare_protein
panfry_protein prepare_protein
arrange_on_plate bake_vegetables panfry_protein
serve_dish arrange_on_plate
```
The format of each line is task_id [task_id [...]], where the zero- or more following task IDs
represent the tasks that must be completed before the current task (the first task ID) can be
started.

Step 1: Decide whether a task can be completed as a starting task
Step 2: Arrive at a valid order in which those tasks can be performed

Example input 1:
```sh
bake_vegetables chop_vegetables preheat_oven
chop_vegetables wash_vegetables
panfry_protein prepare_protein
clean_kitchen arrange_on_plate
prepare_protein
preheat_oven
serve_dish arrange_on_plate
wash_vegetables
arrange_on_plate bake_vegetables panfry_protein
```

```sh
Example input 2:
bake_vegetables chop_vegetables preheat_oven
chop_vegetables wash_vegetables
panfry_protein prepare_protein arrange_on_plate
clean_kitchen arrange_on_plate
prepare_protein
preheat_oven
serve_dish arrange_on_plate
wash_vegetables
arrange_on_plate bake_vegetables panfry_protein
``` 
### Examples
```
Input: [example input]
Output: [example output]
Explanation: [brief explanation if needed]
```

## Approach/Pseudocode

### Initial Thoughts
[Write down your first thoughts about the problem. What patterns do you recognize? What data structures might be useful?]

### Approach
[Describe your chosen approach in plain English. Why did you choose this method?]

### Pseudocode
```
1. [Step 1 of your algorithm]
2. [Step 2 of your algorithm]
3. [Continue with logical steps...]
4. [Final step and return]
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

**Planning completed at:** 2025-12-29 10:57:33
**Estimated implementation time:** [your estimate]