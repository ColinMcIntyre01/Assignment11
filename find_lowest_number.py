#!/usr/bin/env python3
# The script will find the lowest number in a file and write it to another file.
#
# Run as: python3 find_lowest_number.py <input_file> <output_file>
#
# Example: python3 find_lowest_number.py numbers.txt lowest_number.txt
#
# If python is setup to run as "python" instead of "python3" on the machine, 
# then we should use "python" instead of "python3" in the above.
#
# The input file should contain one number per line. The output file will 
# contain the lowest number.
#
# If the input file is blank, the output file will contain the text: "No 
# numbers found in file".

import sys

def find_lowest_number(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        # Extract numbers from non-empty lines
        numbers = []
        for line in lines:
            line = line.strip()
            if line:  # Only process non-empty lines
                numbers.append(line)
        
        # Check if we have any numbers
        if not numbers:
            with open(output_file, 'w') as f:
                f.write("No numbers found in file")
            return
        
        # Convert to integers (use float if decimals are possible)
        # But based on the test, we should use int since test files have integers
        try:
            numbers_int = [int(num) for num in numbers]
        except ValueError:
            # If integers fail, try floats
            numbers_float = [float(num) for num in numbers]
            lowest = min(numbers_float)
            # Write as integer if it's a whole number
            if lowest.is_integer():
                with open(output_file, 'w') as f:
                    f.write(str(int(lowest)))
            else:
                with open(output_file, 'w') as f:
                    f.write(str(lowest))
            return
        
        # Find the lowest number and write as integer
        lowest = min(numbers_int)
        with open(output_file, 'w') as f:
            f.write(str(lowest))
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid number in input file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    find_lowest_number(input_file, output_file)
