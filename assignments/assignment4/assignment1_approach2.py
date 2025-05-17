import re
from collections import Counter
from datetime import datetime

def analyze_log_file(input_file, output_file):
    """
    Analyzes a log file and generates a summary report using libraries.
    
    Parameters:
    - input_file: Path to the input log file
    - output_file: Path to the output summary file
    """
    # Regular expression to extract parts from log entries
    log_pattern = re.compile(r'\[(.*?)\] \[(.*?)\] (.*)')
    
    # Initialize data structures
    log_levels = Counter()  # Automatically counts occurrences
    error_messages = set()  # Automatically handles uniqueness
    error_timestamps = []
    
    try:
        # Read and process the file
        with open(input_file, 'r') as file:
            lines = [line for line in file if line.strip()]  # Skip empty lines
            
            # Process each valid log entry
            for line in lines:
                match = log_pattern.match(line.strip())
                if match:
                    timestamp, level, message = match.groups()
                    log_levels[level] += 1
                    
                    # Track error information
                    if level == "ERROR":
                        error_messages.add(message)
                        error_timestamps.append(timestamp)
        
        # Generate the report
        with open(output_file, 'w') as file:
            file.write("LOG ANALYSIS SUMMARY\n")
            file.write("--------------------\n")
            file.write(f"Total log entries: {sum(log_levels.values())}\n\n")
            
            # Write log level counts
            file.write("By level:\n")
            for level, count in log_levels.items():
                file.write(f"{level}: {count}\n")
            file.write("\n")
            
            # Write error period info if we have errors
            if error_timestamps:
                file.write(f"Most errors occurred between {error_timestamps[0]} and {error_timestamps[-1]} "
                           f"({len(error_timestamps)} occurrences)\n\n")
            
            # Write unique error messages
            file.write("Unique error messages:\n")
            for message in error_messages:
                file.write(f"- {message}\n")
                
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
if __name__ == "__main__":
    analyze_log_file('log_file.txt', 'log_analysis.txt')
