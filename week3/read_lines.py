# read_lines.py
# Purpose: Read a file line by line and process each line

def process_file_by_line(filename):
    """Read and process a file line by line."""
    try:
        line_count = 0
        with open(filename, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                line_count += 1
                # Strip whitespace and newlines
                cleaned_line = line.strip()
                print(f"Line {line_count}: {cleaned_line}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
if __name__ == "__main__":
    file_name = "output.txt"
    process_file_by_line(file_name)
