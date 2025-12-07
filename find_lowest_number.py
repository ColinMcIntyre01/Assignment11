#!/usr/bin/env python3
"""
The script will find the lowest number in a file and write it to another file.

Run as: python3 find_lowest_number.py <input_file> <output_file>
Example: python3 find_lowest_number.py numbers.txt lowest_number.txt

If python is setup to run as "python" instead of "python3" on the machine, 
then we should use "python" instead of "python3" in the above.

The input file should contain one number per line. The output file will 
contain the lowest number.

If the input file is blank, the output file will contain the text: "No 
numbers found in file".
"""

import sys

def find_lowest_number(input_file, output_file):
    """Find the lowest number in input_file and write it to output_file."""
    try:
        # Read all lines from the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Parse numbers from non-empty lines
        numbers = []
        for line in lines:
            stripped = line.strip()
            if stripped:  # Skip empty lines
                try:
                    # Convert to integer (assignment uses integers)
                    num = int(stripped)
                    numbers.append(num)
                except ValueError:
                    # If not an integer, skip it or handle as needed
                    # For this assignment, we assume all inputs are integers
                    pass
        
        # Handle empty file or file with no valid numbers
        if not numbers:
            with open(output_file, 'w') as f:
                f.write("No numbers found in file\n")
            return
        
        # Find the minimum number
        lowest = min(numbers)
        
        # Write the result to output file
        with open(output_file, 'w') as f:
            f.write(f"{lowest}\n")
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
        print("Example: python3 find_lowest_number.py numbers.txt lowest.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    find_lowest_number(input_file, output_file)
