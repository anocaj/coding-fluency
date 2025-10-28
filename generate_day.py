#!/usr/bin/env python3
"""
Daily Practice Folder Generator

This script creates a new daily practice folder with the required template files
for structured coding practice sessions.

Usage:
    python generate_day.py [YYYY-MM-DD]
    
If no date is provided, uses today's date.
"""

import argparse
import sys
import shutil
from datetime import datetime
from pathlib import Path


def parse_arguments():
    """Parse command line arguments for date input."""
    parser = argparse.ArgumentParser(
        description="Generate a daily practice folder with templates for structured coding practice",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python generate_day.py                    # Use today's date
    python generate_day.py 2024-01-15        # Use specific date
    python generate_day.py 2024-12-25        # Use future date for planning
    python generate_day.py --help            # Show this help message

The script creates a folder structure like:
    daily_practice/YYYY-MM-DD/
    ├── plan.md         (problem analysis template)
    ├── solution.py     (implementation template)
    └── reflection.md   (post-solution analysis)

Requirements:
    - Date must be in YYYY-MM-DD format
    - Folder must not already exist
    - Templates must be available in daily_practice/ directory
        """
    )
    
    parser.add_argument(
        'date',
        nargs='?',
        default=None,
        metavar='YYYY-MM-DD',
        help='Date in YYYY-MM-DD format (default: today\'s date)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Daily Practice Generator 1.0'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be created without actually creating files'
    )
    
    return parser.parse_args()


def validate_and_format_date(date_str):
    """
    Validate and format the input date string with comprehensive error checking.
    
    Args:
        date_str (str): Date string in YYYY-MM-DD format or None for today
        
    Returns:
        str: Validated date string in YYYY-MM-DD format
        
    Raises:
        ValueError: If date format is invalid or date is unreasonable
    """
    if date_str is None:
        # Use today's date
        return datetime.now().strftime('%Y-%m-%d')
    
    # Check basic format first
    if not isinstance(date_str, str):
        raise ValueError(f"Date must be a string, got {type(date_str).__name__}")
    
    # Check for common format issues
    if len(date_str) != 10:
        raise ValueError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD format (10 characters)")
    
    if date_str.count('-') != 2:
        raise ValueError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD with exactly 2 hyphens")
    
    try:
        # Validate the date format and that it's a real date
        parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Additional validation for reasonable dates
        current_year = datetime.now().year
        if parsed_date.year < 2000:
            raise ValueError(f"Year {parsed_date.year} is too far in the past. Use a year >= 2000")
        if parsed_date.year > current_year + 10:
            raise ValueError(f"Year {parsed_date.year} is too far in the future. Use a year <= {current_year + 10}")
        
        return parsed_date.strftime('%Y-%m-%d')
        
    except ValueError as e:
        if "does not match format" in str(e):
            raise ValueError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD format (e.g., 2024-01-15)")
        elif "day is out of range" in str(e) or "month must be" in str(e):
            raise ValueError(f"Invalid date '{date_str}'. Please check the day and month values")
        else:
            # Re-raise our custom errors or other validation errors
            raise


def create_daily_folder(date_str):
    """
    Create a daily practice folder with template files.
    
    Args:
        date_str (str): Date string in YYYY-MM-DD format
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Define paths
        daily_practice_dir = Path("daily_practice")
        target_folder = daily_practice_dir / date_str
        template_dir = daily_practice_dir
        
        # Check if folder already exists
        if target_folder.exists():
            print(f"❌ Error: Folder for {date_str} already exists")
            print(f"   Location: {target_folder}")
            print("💡 Solutions:")
            print("   - Use a different date")
            print(f"   - Remove existing folder: rm -rf {target_folder}")
            print("   - Use --dry-run to preview without creating")
            return False
        
        # Ensure daily_practice directory exists
        daily_practice_dir.mkdir(exist_ok=True)
        
        # Create the target folder
        target_folder.mkdir(parents=True)
        print(f"📁 Created folder: {target_folder}")
        
        # Copy and populate template files
        template_files = [
            ("plan_template.md", "plan.md"),
            ("solution_template.py", "solution.py"),
            ("reflection_template.md", "reflection.md")
        ]
        
        for template_name, target_name in template_files:
            success = copy_and_populate_template(
                template_dir / template_name,
                target_folder / target_name,
                date_str
            )
            if not success:
                return False
        
        return True
        
    except OSError as e:
        print(f"❌ Error creating folder: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Unexpected error during folder creation: {e}", file=sys.stderr)
        return False


def copy_and_populate_template(template_path, target_path, date_str):
    """
    Copy a template file and populate it with date information.
    
    Args:
        template_path (Path): Path to the template file
        target_path (Path): Path where the populated file should be created
        date_str (str): Date string to populate in the template
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if template exists
        if not template_path.exists():
            print(f"❌ Error: Template file not found: {template_path}", file=sys.stderr)
            print("💡 Make sure you're running this script from the repository root", file=sys.stderr)
            print("   and that template files exist in daily_practice/", file=sys.stderr)
            return False
        
        # Read template content
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Populate template with date information
        content = populate_template_content(content, date_str)
        
        # Write to target file
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"📝 Created: {target_path.name}")
        return True
        
    except IOError as e:
        print(f"❌ Error processing template {template_path.name}: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Unexpected error processing template {template_path.name}: {e}", file=sys.stderr)
        return False


def populate_template_content(content, date_str):
    """
    Replace placeholder values in template content with actual values.
    
    Args:
        content (str): Template file content
        date_str (str): Date string in YYYY-MM-DD format
        
    Returns:
        str: Content with placeholders replaced
    """
    # Replace date placeholders
    content = content.replace("[YYYY-MM-DD]", date_str)
    
    # Add timestamp for reflection template
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = content.replace("[timestamp]", current_time)
    
    return content


def perform_dry_run(date_str):
    """
    Show what would be created without actually creating files.
    
    Args:
        date_str (str): Date string in YYYY-MM-DD format
    """
    print(f"🔍 DRY RUN: Showing what would be created for {date_str}")
    print()
    
    # Check current state
    daily_practice_dir = Path("daily_practice")
    target_folder = daily_practice_dir / date_str
    
    if target_folder.exists():
        print(f"❌ Folder already exists: {target_folder}")
        print("   No action would be taken.")
        return
    
    # Show what would be created
    print(f"📁 Would create folder: daily_practice/{date_str}/")
    print("📝 Would create files:")
    
    template_files = [
        ("plan_template.md", "plan.md", "problem planning template"),
        ("solution_template.py", "solution.py", "implementation template"),
        ("reflection_template.md", "reflection.md", "post-solution analysis")
    ]
    
    for template_name, target_name, description in template_files:
        template_path = daily_practice_dir / template_name
        if template_path.exists():
            print(f"   ✓ {target_name} ({description})")
        else:
            print(f"   ❌ {target_name} - WARNING: Template {template_name} not found!")
    
    print()
    print("💡 To actually create the folder, run without --dry-run flag")


def main():
    """Main entry point for the script."""
    try:
        args = parse_arguments()
        
        # Validate date first
        formatted_date = validate_and_format_date(args.date)
        
        # Handle dry run
        if args.dry_run:
            perform_dry_run(formatted_date)
            return
        
        # Show what we're about to do
        if args.date is None:
            print(f"📅 Using today's date: {formatted_date}")
        else:
            print(f"📅 Using specified date: {formatted_date}")
        
        print("🚀 Generating daily practice folder...")
        
        # Create the daily practice folder and populate with templates
        success = create_daily_folder(formatted_date)
        
        if success:
            print()
            print(f"✅ Successfully created daily practice folder for {formatted_date}")
            print(f"📁 Location: daily_practice/{formatted_date}/")
            print("📝 Files created:")
            print("   - plan.md (problem planning template)")
            print("   - solution.py (implementation template)")
            print("   - reflection.md (post-solution analysis)")
            print()
            print("💡 Next steps:")
            print(f"   1. cd daily_practice/{formatted_date}")
            print("   2. Edit plan.md to analyze your chosen problem")
            print("   3. Implement your solution in solution.py")
            print("   4. Complete reflection.md after solving")
        else:
            print("❌ Failed to create daily practice folder")
            sys.exit(1)
        
    except ValueError as e:
        print(f"❌ Input Error: {e}", file=sys.stderr)
        print("💡 Use --help for usage examples", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user.", file=sys.stderr)
        sys.exit(130)  # Standard exit code for SIGINT
    except PermissionError as e:
        print(f"❌ Permission Error: {e}", file=sys.stderr)
        print("💡 Check that you have write permissions in this directory", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"❌ File System Error: {e}", file=sys.stderr)
        print("💡 Check available disk space and directory permissions", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        print("💡 Please report this issue if it persists", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()