#!/usr/bin/env python3
"""
Quick script to add new practice entries to the practice log.
Usage: python add_practice_entry.py
"""

from datetime import datetime

def add_practice_entry():
    print("=== Add New Practice Entry ===\n")
    
    # Get input
    date = input("Date (YYYY-MM-DD) [today]: ").strip() or datetime.now().strftime("%Y-%m-%d")
    problem = input("Problem name: ").strip()
    source = input("Source (e.g., LeetCode 1234): ").strip()
    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
    time_spent = input("Time spent (e.g., 25min): ").strip()
    status = input("Status (✅/❌/⏳): ").strip() or "✅"
    pattern = input("Key pattern: ").strip()
    complexity = input("Time complexity: ").strip()
    confidence = input("Confidence (1-5): ").strip()
    
    # Format the table row
    row = f"| {date} | {problem} | {source} | {difficulty} | {time_spent} | {status} | {pattern} | {complexity} | {confidence}/5 |"
    
    print(f"\nAdd this row to your practice_log.md:")
    print(row)
    print(f"\nAlso consider updating:")
    print(f"- Pattern frequency for: {pattern}")
    print(f"- Difficulty progress for: {difficulty}")
    print(f"- Time management for: {time_spent}")

if __name__ == "__main__":
    add_practice_entry()