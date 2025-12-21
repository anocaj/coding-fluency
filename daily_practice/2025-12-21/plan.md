# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** Design In-Memory File System

**Source:** https://www.designgurus.io/answers/detail/588-design-in-memory-file-system-ans89

**Difficulty:** Hard

### Problem Statement
Design an in-memory file system that supports basic file and directory operations. You need to implement the following functions:

**ls(path):** If the given path is a file path, return a list containing only that file name. If it is a directory path, return a list of all files and subdirectories in that directory. The output should be sorted in lexicographic (alphabetical) order.

**mkdir(path):** Create a new directory given by path. This should create any intermediate directories that do not exist as well. This operation does not return anything.

**addContentToFile(filePath, content):** If the file at filePath does not exist, create a new file and add content to it. If the file already exists, append the new content to the end of the current content. This operation does not return anything.

**readContentFromFile(filePath):** Return the current content of the file at filePath.

The file system is hierarchical (like a standard file system). All paths are absolute (they begin with "/"). The root directory is "/" (forward slash). There are no trailing slashes at the end of paths (except for the root path itself). All file and directory names consist only of lowercase letters, and in each directory no two files or subdirectories share the same name.

Examples:

Example 1:
Input:

["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]  
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]  
Output:

[null, [], null, null, ["a"], "hello"]  
Explanation:

FileSystem: Instantiate the file system (initially empty). Returns null (no output).
ls("/"): List contents of the root directory "/". It's empty at the start, so output [].
mkdir("/a/b/c"): Create a directory path /a/b/c. This creates directories "a", "b", and "c" recursively. No output (null).
addContentToFile("/a/b/c/d", "hello"): Create a new file "d" in directory /a/b/c with content "hello". (Since /a/b/c exists after the previous step, we can create file "d" there.) No output (null).
ls("/"): List contents of root "/". Now it contains a directory "a", so output ["a"] (sorted lexicographically; only one entry here).
readContentFromFile("/a/b/c/d"): Read content of file "d" at path /a/b/c/d. The content is "hello", so output "hello".
Example 2:
Input:

["FileSystem","mkdir","addContentToFile","addContentToFile","ls","readContentFromFile"]  
[[],["/g"],["/g/file1","Hello"],["/g/file1","World"],["/g"],["/g/file1"]]  
Output:

[null, null, null, null, ["file1"], "HelloWorld"]  
Explanation:

FileSystem: Instantiate the file system.
mkdir("/g"): Create directory "/g".
addContentToFile("/g/file1", "Hello"): Create file "file1" in "/g" with content "Hello".
addContentToFile("/g/file1", "World"): Append "World" to the content of /g/file1. The file’s content becomes "HelloWorld".
ls("/g"): List contents of directory "/g". It contains one file "file1", so output ["file1"].
readContentFromFile("/g/file1"): Read the content of /g/file1. Outputs "HelloWorld" (the concatenated content from steps 3 and 4).
Example 3:
Input:

["FileSystem","addContentToFile","mkdir","mkdir","ls"]  
[[],["/z","zzz"],["/a"],["/b"],["/"]]  
Output:

[null, null, null, null, ["a","b","z"]]  
Explanation:

FileSystem: Instantiate the file system.
addContentToFile("/z", "zzz"): Create a file "z" in the root directory with content "zzz".
mkdir("/a"): Create directory "/a" in root.
mkdir("/b"): Create directory "/b" in root.
ls("/"): List contents of root. Now root contains a directory "a", a directory "b", and a file "z". Lexicographically sorted, these names appear as ["a","b","z"]. (Note that both files and subdirectories are listed together in sorted order.)
Constraints:
All file paths and directory paths are absolute (start with "/"). The only path that ends with "/" is the root itself.
You can assume all operations are given valid parameters. For example, you won't be asked to list a directory that doesn’t exist or read a file that hasn’t been created. Similarly, if a path is supposed to be a file path, the file will exist by the time you read it.
All file and directory names consist only of lowercase English letters (a-z). There will be no duplicate names in any given directory.
This is a design problem focused on the data structure; the number of operations can be large (potentially thousands), so each operation should be designed to run efficiently under those constraints.
Hints to Guide the Thought Process
Think of a Hierarchical Structure: The file system is naturally a tree-like hierarchy (directories contain subdirectories or files). Consider representing the paths using a data structure that reflects this hierarchy, such as a tree or trie. Each node in this tree could represent a directory or a file.

Distinguish Files from Directories: In your design, you need to differentiate between a directory node and a file node. A directory holds children (subdirectories or files), whereas a file holds content. Think about how you can mark a node as a file and store its content.

Path Parsing: Each operation will involve parsing a path like "/a/b/c" into its components. Consider using string split operations (e.g., splitting by "/") to navigate or build the structure. Be careful with the root path ("/") and empty path components from splitting.

Implement Operations Step by Step: For each function (ls, mkdir, addContentToFile, readContentFromFile), outline how to traverse or modify your data structure:

Listing (ls): Find the node corresponding to the given path. If it's a file, return its name; if it's a directory, gather and sort the names of its children.
Making Directories (mkdir): Traverse from the root, creating any missing directory nodes along the path.
Adding Content (addContentToFile): Traverse to the file's parent directory. If the file node exists, append content; if not, create a new file node.
Reading Content (readContentFromFile): Simply retrieve the content stored in the file node.
Lexicographic Order: Remember that when listing directory contents, the result must be sorted lexicographically. You can achieve this by sorting the list of child names before returning, or by maintaining the children in a sorted structure as you insert them.

By considering these hints, you should be able to piece together a design for the in-memory file system. Try to sketch out how you would store the directories and files in memory and how each operation would interact with that storage.
```

## Approach/Pseudocode

### Initial Thoughts
Create a Tree where we have nodes(directories) and special nodes which are files
node:
    isFile: False # helps us to distinguish when iterating through children
    children: node|file[]

file: 
    isFile: True
    content: {}

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

**Planning completed at:** 2025-12-21 09:27:19
**Estimated implementation time:** 2025-12-21 10:50:19