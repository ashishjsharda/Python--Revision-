# simple_read.py
# Purpose: Read and display the contents of a text file

def read_file(filename):
    """Read and print the contents of a text file."""
    try:
        # Open the file using a context manager
        with open(filename, 'r') as file:
            # Read all contents at once
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
if __name__ == "__main__":
    file_name = "sample.txt"
    read_file(file_name)
