import csv  # Import the csv module to handle CSV file reading and writing

# File paths
input_file = "users.csv"           # CSV file with user data (input)
output_file = "filtered_users.csv" # File to save users with age > 30 and valid data
error_log = "error_log.txt"        # File to log any errors or missing data

try:
    # Open all files using a context manager
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile, \
         open(error_log, mode='w') as log:

        reader = csv.DictReader(infile)  # Read rows as dictionaries using column headers
        writer = csv.DictWriter(outfile, fieldnames=['name', 'email', 'age'])  # Write rows using specified headers
        writer.writeheader()  # Write the header row to the output file

        # Loop through each row in the input CSV
        for row in reader:
            # Check if any required field is missing
            if not row['name'] or not row['email'] or not row['age']:
                log.write(f"Missing data: {row}\n")  # Log the issue
                continue  # Skip this row

            try:
                age = int(row['age'])  # Try to convert age to an integer
                if age > 30:  # Only keep users older than 30
                    writer.writerow(row)  # Write valid row to the output file
            except ValueError:
                # Log error if age is not a number (e.g., "N/A" or "thirty")
                log.write(f"Invalid age value: {row['age']} in row {row}\n")

    # Message when processing is complete
    print("Processing complete. Filtered data and errors logged.")

# Handle missing file error
except FileNotFoundError as e:
    print(f"File not found: {e}")

# Catch any other unexpected errors
except Exception as e:
    print(f"An error occurred: {e}")
