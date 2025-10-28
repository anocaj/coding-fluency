# Session 1 Problems

## Problem Selection Guide

Choose 2-3 problems based on your skill level and time constraints:
- **Beginner**: 2 Easy + 1 Medium (or 3 Easy)
- **Intermediate**: 1 Easy + 2 Medium (or 1 Medium + 1 Hard)
- **Advanced**: 1 Medium + 1 Hard (or 2 Hard)

---

## Easy Problems (15-20 minutes each)

### Problem E1: Two Sum
**Difficulty**: Easy | **Time Estimate**: 15 minutes

**Description**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example**:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

**Constraints**:
- 2 ≤ nums.length ≤ 10^4
- -10^9 ≤ nums[i] ≤ 10^9
- -10^9 ≤ target ≤ 10^9

**Reference**: [LeetCode #1](https://leetcode.com/problems/two-sum/)

---

### Problem E2: Valid Parentheses
**Difficulty**: Easy | **Time Estimate**: 18 minutes

**Description**: Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: open brackets are closed by the same type of brackets, and open brackets are closed in the correct order.

**Example**:
```
Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false
```

**Constraints**:
- 1 ≤ s.length ≤ 10^4
- s consists of parentheses only '()[]{}'

**Reference**: [LeetCode #20](https://leetcode.com/problems/valid-parentheses/)

---

### Problem E3: Merge Two Sorted Lists
**Difficulty**: Easy | **Time Estimate**: 20 minutes

**Description**: You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

**Example**:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Constraints**:
- The number of nodes in both lists is in the range [0, 50]
- -100 ≤ Node.val ≤ 100
- Both list1 and list2 are sorted in non-decreasing order

**Reference**: [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## Medium Problems (20-25 minutes each)

### Problem M1: Add Two Numbers
**Difficulty**: Medium | **Time Estimate**: 22 minutes

**Description**: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Example**:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Constraints**:
- The number of nodes in each linked list is in the range [1, 100]
- 0 ≤ Node.val ≤ 9
- It is guaranteed that the list represents a number that does not have leading zeros

**Reference**: [LeetCode #2](https://leetcode.com/problems/add-two-numbers/)

---

### Problem M2: Longest Substring Without Repeating Characters
**Difficulty**: Medium | **Time Estimate**: 25 minutes

**Description**: Given a string `s`, find the length of the longest substring without repeating characters.

**Example**:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

**Constraints**:
- 0 ≤ s.length ≤ 5 * 10^4
- s consists of English letters, digits, symbols and spaces

**Reference**: [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

### Problem M3: Group Anagrams
**Difficulty**: Medium | **Time Estimate**: 23 minutes

**Description**: Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

**Example**:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Constraints**:
- 1 ≤ strs.length ≤ 10^4
- 0 ≤ strs[i].length ≤ 100
- strs[i] consists of lowercase English letters only

**Reference**: [LeetCode #49](https://leetcode.com/problems/group-anagrams/)

---

## Hard Problems (25-30 minutes each)

### Problem H1: Median of Two Sorted Arrays
**Difficulty**: Hard | **Time Estimate**: 30 minutes

**Description**: Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

**Example**:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Constraints**:
- nums1.length == m
- nums2.length == n
- 0 ≤ m ≤ 1000
- 0 ≤ n ≤ 1000
- 1 ≤ m + n ≤ 2000

**Reference**: [LeetCode #4](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

### Problem H2: Trapping Rain Water
**Difficulty**: Hard | **Time Estimate**: 28 minutes

**Description**: Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example**:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water are being trapped.
```

**Constraints**:
- n == height.length
- 1 ≤ n ≤ 2 * 10^4
- 0 ≤ height[i] ≤ 3 * 10^4

**Reference**: [LeetCode #42](https://leetcode.com/problems/trapping-rain-water/)

---

## Session Planning Template

**Selected Problems**:
- [ ] Problem ___: _______ (__ minutes)
- [ ] Problem ___: _______ (__ minutes)  
- [ ] Problem ___: _______ (__ minutes)

**Total Estimated Time**: ___ minutes

**Strategy Notes**:
- Start with: _______
- Focus on: _______
- If stuck: _______

**Key Concepts to Remember**:
- [ ] Time/Space complexity analysis
- [ ] Edge case handling
- [ ] Code clarity and naming
- [ ] Test with examples