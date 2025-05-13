import csv  # Import the CSV module

# File paths
input_file = "users.csv"
output_file = "filtered_users.csv"
error_log = "error_log.txt"

try:
    with open(input_file, mode='r', newline='') as infile, \
         open(output_file, mode='w', newline='') as outfile, \
         open(error_log, mode='w') as log:

        reader = csv.reader(infile)  # Create a CSV reader object
        writer = csv.writer(outfile)  # Create a CSV writer object

        header = next(reader)  # Read the header row
        writer.writerow(header)  # Write header to output file

        # Get the index of each column to avoid hardcoding
        name_idx = header.index("name")
        email_idx = header.index("email")
        age_idx = header.index("age")

        for row in reader:
            # Check if any required value is missing
            if not row[name_idx] or not row[email_idx] or not row[age_idx]:
                log.write(f"Missing data: {row}\n")
                continue

            try:
                age = int(row[age_idx])
                if age > 30:
                    writer.writerow(row)
            except ValueError:
                log.write(f"Invalid age value: {row[age_idx]} in row {row}\n")

    print("Processing complete using csv.reader.")

except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
