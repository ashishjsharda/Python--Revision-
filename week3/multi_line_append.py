def append_multiple_lines(file_path, lines_to_append):
    """
    Append multiple lines to a file at once.
    
    Args:
        file_path (str): Path to the file
        lines_to_append (list): List of strings to append
    """
    # Make sure each line ends with a newline character
    formatted_lines = []
    for line in lines_to_append:
        # If the line doesn't end with a newline, add one
        if not line.endswith('\n'):
            line = line + '\n'
        formatted_lines.append(line)
    
    # Open the file in append mode
    with open(file_path, 'a') as file:
        # Write all lines at once
        file.writelines(formatted_lines)
        
        # Alternative: write each line individually
        # for line in formatted_lines:
        #     file.write(line)
    
    print(f"Added {len(formatted_lines)} lines to {file_path}")

# Example usage
new_entries = [
    'First new line',  # No newline character
    'Second new line\n',  # Has newline character
    'Third new line'  # No newline character
]

append_multiple_lines('data.txt', new_entries)
