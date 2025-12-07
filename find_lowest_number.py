#!/usr/bin/env python3
import subprocess
import os

def compare_files(file1, file2):
    """Compare two files, ignoring trailing whitespace."""
    with open(file1, 'r') as f1:
        content1 = f1.read().rstrip()  # Remove trailing whitespace
    
    with open(file2, 'r') as f2:
        content2 = f2.read().rstrip()  # Remove trailing whitespace
    
    return content1 == content2

def run_test(test_num, input_file, expected_file):
    output_file = f"test_output_{test_num}.txt"
    
    print(f"\n=== Test {test_num} ===")
    print(f"Input: {input_file}")
    print(f"Expected: {expected_file}")
    
    # Run the program
    result = subprocess.run(
        ["python", "find_lowest_number.py", input_file, output_file],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"❌ Failed to run: {result.stderr}")
        return False
    
    # Compare files
    if compare_files(output_file, expected_file):
        print(f"✅ Test {test_num} passed")
        # Show what we got
        with open(output_file, 'r') as f:
            print(f"Output: '{f.read().rstrip()}'")
        return True
    else:
        print(f"❌ Test {test_num} failed")
        with open(output_file, 'r') as f:
            actual = f.read()
        with open(expected_file, 'r') as f:
            expected = f.read()
        print(f"Expected: '{expected.rstrip()}'")
        print(f"Actual:   '{actual.rstrip()}'")
        return False

def main():
    tests = [
        ("test_data/test1_input.txt", "test_data/test1_expected.txt"),
        ("test_data/test2_input.txt", "test_data/test2_expected.txt"),
        ("test_data/test3_input.txt", "test_data/test3_expected.txt"),
    ]
    
    all_passed = True
    for i, (input_file, expected_file) in enumerate(tests, 1):
        if not run_test(i, input_file, expected_file):
            all_passed = False
    
    # Cleanup
    for i in range(1, len(tests) + 1):
        output_file = f"test_output_{i}.txt"
        if os.path.exists(output_file):
            os.remove(output_file)
    
    if all_passed:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n💥 Some tests failed!")
        return 1

if __name__ == "__main__":
    exit(main())
