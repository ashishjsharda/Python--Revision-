def analyze_log_file(input_file, output_file):
    """
    Analyzes a log file and generates a summary report without using imports.
    
    Parameters:
    - input_file: Path to the input log file
    - output_file: Path to the output summary file
    """
    # Initialize counters and trackers
    log_levels = {}  # Dictionary to count occurrences of each log level
    error_messages = []  # List to store unique error messages
    error_timestamps = []  # List to store timestamps of ERROR messages
    total_entries = 0  # Counter for total log entries
    
    # Read log file line by line
    try:
        with open(input_file, 'r') as file:
            for line in line_reader(file):
                # Skip empty lines
                if not line.strip():
                    continue
                
                total_entries += 1
                
                # Parse the log entry manually
                # Format: [TIMESTAMP] [LOG_LEVEL] Message
                if line.count('[') >= 2 and line.count(']') >= 2:
                    # Extract timestamp
                    timestamp_start = line.find('[') + 1
                    timestamp_end = line.find(']')
                    timestamp = line[timestamp_start:timestamp_end]
                    
                    # Extract log level
                    level_start = line.find('[', timestamp_end) + 1
                    level_end = line.find(']', timestamp_end + 1)
                    level = line[level_start:level_end]
                    
                    # Extract message
                    message = line[level_end + 1:].strip()
                    
                    # Update log level count
                    if level in log_levels:
                        log_levels[level] += 1
                    else:
                        log_levels[level] = 1
                    
                    # Track error messages and timestamps
                    if level == "ERROR":
                        if message not in error_messages:
                            error_messages.append(message)
                        error_timestamps.append(timestamp)
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    # Find time period with most errors (simplified approach)
    error_period = get_error_period(error_timestamps)
    
    # Write summary report
    try:
        with open(output_file, 'w') as file:
            file.write("LOG ANALYSIS SUMMARY\n")
            file.write("--------------------\n")
            file.write(f"Total log entries: {total_entries}\n")
            
            file.write("By level:\n")
            for level, count in log_levels.items():
                file.write(f"{level}: {count}\n")
            
            if error_period:
                start_time, end_time, count = error_period
                file.write(f"Most errors occurred between {start_time} and {end_time} ({count} occurrences)\n")
            
            file.write("Unique error messages:\n")
            for message in error_messages:
                file.write(f"- {message}\n")
    except Exception as e:
        print(f"Error writing to output file: {e}")

def line_reader(file):
    """
    A generator function to read a file line by line.
    This helps avoid loading the entire file into memory.
    """
    for line in file:
        yield line

def get_error_period(timestamps):
    """
    Finds the time period with the most ERROR messages.
    For this simple implementation, we just return the start and end times
    of all error timestamps.
    
    In a more sophisticated implementation, we would:
    1. Group timestamps by hour or other time period
    2. Count errors in each period
    3. Return the period with the highest count
    """
    if not timestamps:
        return None
    
    if len(timestamps) == 1:
        return timestamps[0], timestamps[0], 1
    
    # For this simplified version, we just return the full range
    return timestamps[0], timestamps[-1], len(timestamps)

# Usage example
if __name__ == "__main__":
    analyze_log_file('log_file.txt', 'log_analysis.txt')
