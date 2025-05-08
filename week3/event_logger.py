def log_event(event, log_file='app.log'):
    """
    Append a timestamped event to a log file.
    
    Args:
        event (str): The event description to log
        log_file (str): Path to the log file (default: 'app.log')
    """
    # Import datetime here to keep it encapsulated in the function
    from datetime import datetime
    
    # Generate a timestamp in a readable format
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')
    # Result: "Thursday, May 08, 2025 at 02:32 PM"
    
    # Format the log entry with timestamp
    log_entry = f'[{timestamp}] {event}\n'
    
    # Open file in append mode and write the log entry
    with open(log_file, 'a') as file:
        file.write(log_entry)
        
    # Optional: Print confirmation (useful for debugging)
    print(f"Logged: {log_entry.strip()}")

# Usage example:
if __name__ == "__main__":
    # These will be appended one after another to app.log
    log_event('Application started')
    log_event('User logged in: alice')
    log_event('Error: Database connection failed')
    
    # You can specify a different log file
    log_event('Special event', log_file='special.log')
