# simple_write.py
# Purpose: Create a file and write content to it

def write_file(filename, content):
    """Write content to a text file."""
    try:
        # Open file in write mode
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
if __name__ == "__main__":
    file_name = "output.txt"
    content_to_write = "Hello, Python!\nThis is a test file.\nWriting files is easy!"
    write_file(file_name, content_to_write)
