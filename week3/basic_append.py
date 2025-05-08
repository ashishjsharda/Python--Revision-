# Define the file path
file_path = 'output.txt'

# Open the file in append mode ('a')
# The 'with' statement ensures the file is properly closed after the block
with open(file_path, 'a') as file:
    # Write a string to the end of the file
    # The write() method returns the number of characters written
    chars_written = file.write('New log entry\n')
    
    # Optional: Print confirmation
    print(f"Added {chars_written} characters to {file_path}")

# At this point, the file is automatically closed
# The content has been appended without overwriting existing data
