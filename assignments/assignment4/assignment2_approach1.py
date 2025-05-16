def process_csv_data(input_file, pass_file, fail_file, summary_file):
    """
    Processes student grade data from a CSV file and generates reports.
    
    Parameters:
    - input_file: Path to the input CSV file
    - pass_file: Path to the output CSV file for passing students
    - fail_file: Path to the output CSV file for failing students
    - summary_file: Path to the output summary file
    """
    passed_students = []  # List to store passing students
    failed_students = []  # List to store failing students
    all_averages = []  # List to store all student averages
    data_issues = []  # List to track data issues
    
    # Read and process the CSV file
    try:
        with open(input_file, 'r') as file:
            # Read header line and split by comma
            headers = file.readline().strip().split(',')
            
            # Find indices for each column
            name_idx = headers.index('Name')
            id_idx = headers.index('ID')
            subject_indices = {
                'Math': headers.index('Math'),
                'Science': headers.index('Science'),
                'English': headers.index('English'),
                'History': headers.index('History')
            }
            
            # Process each student (each line in the file)
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue
                
                # Split line into values
                values = line.strip().split(',')
                name = values[name_idx]
                student_id = values[id_idx]
                
                # Calculate average grade
                grades = []
                for subject, idx in subject_indices.items():
                    if idx < len(values) and values[idx] and values[idx].lower() != 'n/a':
                        try:
                            grades.append(float(values[idx]))
                        except ValueError:
                            data_issues.append(f"Invalid grade format: {name} (ID: {student_id}), {subject}")
                    else:
                        data_issues.append(f"Missing grade: {name} (ID: {student_id}), {subject}")
                
                # Calculate average if there are any valid grades
                if grades:
                    average = sum(grades) / len(grades)
                    all_averages.append((name, average))
                    
                    # Determine if student passed or failed
                    student_data = [name, student_id, f"{average:.1f}"]
                    if average >= 60:
                        passed_students.append(student_data)
                    else:
                        failed_students.append(student_data)
                else:
                    data_issues.append(f"No valid grades for: {name} (ID: {student_id})")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    # Write passing students to CSV
    write_csv(pass_file, ['Name', 'ID', 'Average'], passed_students)
    
    # Write failing students to CSV
    write_csv(fail_file, ['Name', 'ID', 'Average'], failed_students)
    
    # Create summary report
    create_summary(summary_file, passed_students, failed_students, all_averages, data_issues)

def write_csv(filename, headers, rows):
    """
    Writes data to a CSV file without using the csv module.
    
    Parameters:
    - filename: Path to the output CSV file
    - headers: List of column headers
    - rows: List of rows, where each row is a list of values
    """
    try:
        with open(filename, 'w') as file:
            # Write header row
            file.write(','.join(headers) + '\n')
            
            # Write data rows
            for row in rows:
                file.write(','.join(row) + '\n')
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

def create_summary(filename, passed, failed, averages, issues):
    """
    Creates a summary report file with statistics about the student data.
    
    Parameters:
    - filename: Path to the output summary file
    - passed: List of passing students
    - failed: List of failing students
    - averages: List of tuples (name, average) for all students
    - issues: List of data issues encountered
    """
    try:
        with open(filename, 'w') as file:
            total = len(passed) + len(failed)
            
            file.write("STUDENT GRADE SUMMARY\n")
            file.write("---------------------\n")
            file.write(f"Total students: {total}\n")
            
            # Calculate passing/failing percentages
            pass_percent = (len(passed) / total * 100) if total > 0 else 0
            fail_percent = (len(failed) / total * 100) if total > 0 else 0
            
            file.write(f"Passing: {len(passed)} ({pass_percent:.0f}%)\n")
            file.write(f"Failing: {len(failed)} ({fail_percent:.0f}%)\n")
            
            # Find highest and lowest averages
            if averages:
                # Find highest average
                highest_name, highest_avg = averages[0]
                for name, avg in averages:
                    if avg > highest_avg:
                        highest_name, highest_avg = name, avg
                
                # Find lowest average
                lowest_name, lowest_avg = averages[0]
                for name, avg in averages:
                    if avg < lowest_avg:
                        lowest_name, lowest_avg = name, avg
                
                # Calculate class average
                class_average = sum(avg for _, avg in averages) / len(averages)
                
                file.write(f"Highest average: {highest_name} ({highest_avg:.1f})\n")
                file.write(f"Lowest average: {lowest_name} ({lowest_avg:.1f})\n")
                file.write(f"Class average: {class_average:.2f}\n")
            
            # Report data issues
            if issues:
                file.write("Data issues:\n")
                for issue in issues:
                    file.write(f"- {issue}\n")
    except Exception as e:
        print(f"Error writing summary: {e}")

# Usage example
if __name__ == "__main__":
    process_csv_data('students.csv', 'passed.csv', 'failed.csv', 'summary.txt')
