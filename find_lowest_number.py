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

# Check command line arguments
if len(sys.argv) != 3:
    print("Usage: python3 find_lowest_number.py <input_file> <output_file>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

number_found = False
lowest_number = None

try:
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    current_number = float(line)
                    if not number_found:
                        lowest_number = current_number
                        number_found = True
                    elif current_number < lowest_number:
                        lowest_number = current_number
                except ValueError:
                    # Skip lines that are not valid numbers
                    continue
except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
    sys.exit(1)

with open(output_filename, 'w') as output_file:
    if number_found:
        # Write without extra newline to match diff expectations
        output_file.write(str(lowest_number))
    else:
        output_file.write("No numbers found in file")
