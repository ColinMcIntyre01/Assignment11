#!/usr/bin/env python3
import sys

def find_lowest_number(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Extract numbers from non-empty lines
        numbers = []
        for line in lines:
            line = line.strip()
            if line:
                numbers.append(line)
        
        # Check if we have any numbers
        if not numbers:
            with open(output_file, 'w') as f:
                f.write("No numbers found in file\n")  # Add newline
            return
        
        # Convert to integers
        try:
            numbers_int = [int(num) for num in numbers]
        except ValueError:
            print("Error: Non-integer value found in input file")
            sys.exit(1)
        
        # Find the lowest number
        lowest = min(numbers_int)
        
        # Write to output file WITH newline
        with open(output_file, 'w') as f:
            f.write(f"{lowest}\n")  # Add newline here
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    find_lowest_number(input_file, output_file)
