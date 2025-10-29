# Requirements Document

## Introduction

A comprehensive micro-patterns system for daily coding warm-up exercises that focuses on building fluency with small, recurring Python patterns through bite-sized, repeatable exercises designed for 10-15 minute daily practice sessions.

## Glossary

- **Micro_Patterns_System**: The complete system of categorized Python pattern exercises for daily warm-up practice
- **Pattern_Category**: A specific grouping of related micro-patterns (e.g., loop patterns, string manipulation)
- **Pattern_Exercise**: An individual coding exercise focusing on a specific micro-pattern with function stub and test cases
- **Warm_Up_Session**: A 10-15 minute daily practice session using micro-pattern exercises
- **Pattern_File**: A Python file containing 3-5 related pattern exercises for a specific category
- **Fluency_Building**: The process of developing automatic recall and implementation of common coding patterns

## Requirements

### Requirement 1

**User Story:** As a developer wanting to build coding fluency, I want a dedicated micro_patterns folder with categorized pattern exercises, so that I can practice small recurring patterns that appear in larger coding problems.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL create a micro_patterns directory in the repository root
2. THE Micro_Patterns_System SHALL organize pattern exercises into 9 distinct categories covering fundamental Python patterns
3. THE Micro_Patterns_System SHALL provide separate Python files for each pattern category
4. THE Micro_Patterns_System SHALL include comprehensive coverage of loop patterns, data manipulation, algorithmic patterns, and Python idioms
5. THE Micro_Patterns_System SHALL focus on micro-patterns rather than complete algorithmic problems

### Requirement 2

**User Story:** As a developer practicing daily warm-ups, I want each pattern file to contain 3-5 bite-sized exercises with clear structure, so that I can quickly understand and practice specific patterns without cognitive overhead.

#### Acceptance Criteria

1. WHEN accessing a pattern file, THE Pattern_File SHALL contain exactly 3-5 focused exercises per category
2. THE Pattern_Exercise SHALL include a short 1-2 line description explaining the pattern focus
3. THE Pattern_Exercise SHALL provide a function stub with comprehensive docstring explaining input/output expectations
4. THE Pattern_Exercise SHALL include example input/output demonstrations for clarity
5. THE Pattern_Exercise SHALL contain simple assert-based test cases for immediate validation

### Requirement 3

**User Story:** As a developer building muscle memory for coding patterns, I want exercises covering loop patterns and iteration techniques, so that I can automatically implement common iteration approaches without hesitation.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL provide a loop_patterns.py file with iteration exercises
2. THE Pattern_File SHALL include exercises for iterating over indices using range and len
3. THE Pattern_File SHALL include exercises for iterating with both elements and indices using enumerate
4. THE Pattern_File SHALL include exercises for reverse iteration using reversed or negative indexing
5. THE Pattern_File SHALL include exercises for looping over multiple arrays simultaneously using zip

### Requirement 4

**User Story:** As a developer working with data structures, I want exercises covering list and string manipulation patterns, so that I can fluently perform common data transformation operations.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL provide a list_string_patterns.py file with manipulation exercises
2. THE Pattern_File SHALL include exercises for reversing lists using slicing and built-in methods
3. THE Pattern_File SHALL include exercises for extracting subarrays using slice notation
4. THE Pattern_File SHALL include exercises for filtering data using list comprehensions
5. THE Pattern_File SHALL include exercises for mapping values, flattening nested lists, and string join/split operations

### Requirement 5

**User Story:** As a developer analyzing data patterns, I want exercises covering frequency counting and set operations, so that I can efficiently implement counting and uniqueness patterns.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL provide frequency_counting.py and set_patterns.py files
2. THE Pattern_File SHALL include exercises using Counter from collections module for frequency analysis
3. THE Pattern_File SHALL include exercises for manual frequency counting using dictionaries
4. THE Pattern_File SHALL include exercises for conditional counting using sum with generator expressions
5. THE Pattern_File SHALL include exercises for set operations including intersection, union, and difference

### Requirement 6

**User Story:** As a developer implementing algorithmic solutions, I want exercises covering two-pointer and sliding window patterns, so that I can recognize and implement these common optimization techniques.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL provide a two_pointer_sliding_window.py file with algorithmic pattern exercises
2. THE Pattern_File SHALL include exercises for two pointers moving towards each other from array ends
3. THE Pattern_File SHALL include exercises for sliding window sum calculations with fixed window size
4. THE Pattern_File SHALL include exercises for moving window patterns with cumulative sum tracking
5. THE Pattern_File SHALL demonstrate the relationship between two-pointer and sliding window approaches

### Requirement 7

**User Story:** As a developer working with dictionaries and mappings, I want exercises covering dictionary patterns and Python idioms, so that I can leverage Python's powerful built-in features effectively.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL provide dictionary_patterns.py and python_idioms.py files
2. THE Pattern_File SHALL include exercises using defaultdict for automatic value initialization
3. THE Pattern_File SHALL include exercises for manual frequency counting and key-value manipulation
4. THE Pattern_File SHALL include exercises for Python idioms like variable swapping, min/max with defaults, and any/all conditions
5. THE Pattern_File SHALL include exercises combining enumerate with conditional logic and generator expressions

### Requirement 8

**User Story:** As a developer learning recursive thinking and handling edge cases, I want exercises covering recursion patterns and boundary conditions, so that I can implement robust solutions with proper error handling.

#### Acceptance Criteria

1. THE Micro_Patterns_System SHALL provide recursion_patterns.py and edge_case_patterns.py files
2. THE Pattern_File SHALL include exercises demonstrating base case and recursive call templates
3. THE Pattern_File SHALL include exercises for memoization using dictionary caching
4. THE Pattern_File SHALL include exercises for empty input validation and single-element edge cases
5. THE Pattern_File SHALL include exercises for boundary checks in loops and array access

### Requirement 9

**User Story:** As a developer establishing a daily practice routine, I want clear usage instructions and timing guidance for each pattern file, so that I can effectively use these exercises as 10-15 minute warm-up sessions.

#### Acceptance Criteria

1. WHEN opening any pattern file, THE Pattern_File SHALL include a comment header explaining daily warm-up usage
2. THE Pattern_File SHALL provide timing guidance for 10-15 minute practice sessions
3. THE Pattern_File SHALL include instructions for progressive difficulty and pattern combination
4. THE Pattern_File SHALL explain how the exercises build muscle memory for larger coding problems
5. THE Pattern_File SHALL be designed for independent, repeatable practice without external dependencies