import csv
import os

class InvalidCSVFormatError(Exception):
    """Raised when the CSV file has an invalid format"""
    pass

def process_csv(filename):
    """
    Process a CSV file containing numeric data and calculate sum and average for each row.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries containing row data, sum, and average
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        InvalidCSVFormatError: If the CSV format is invalid
        ValueError: If non-numeric values are found
    """
    
    results = []
    file_handle = None
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check if file is empty
        if os.path.getsize(filename) == 0:
            raise InvalidCSVFormatError("File is empty")
        
        # Open and read the CSV file
        file_handle = open(filename, 'r', newline='', encoding='utf-8')
        csv_reader = csv.reader(file_handle)
        
        row_count = 0
        for row_num, row in enumerate(csv_reader, 1):
            # Skip empty rows
            if not row or all(cell.strip() == '' for cell in row):
                continue
                
            row_count += 1
            numeric_values = []
            
            # Process each cell in the row
            for col_num, cell in enumerate(row):
                cell = cell.strip()
                
                # Skip empty cells
                if cell == '':
                    continue
                
                try:
                    # Try to convert to float
                    numeric_value = float(cell)
                    numeric_values.append(numeric_value)
                except ValueError:
                    raise ValueError(f"Invalid data (non-numeric value '{cell}') found at row {row_num}, column {col_num + 1}")
            
            # Calculate sum and average if we have numeric values
            if numeric_values:
                row_sum = sum(numeric_values)
                row_average = row_sum / len(numeric_values)
                
                results.append({
                    'row_number': row_num,
                    'values': numeric_values,
                    'sum': row_sum,
                    'average': round(row_average, 2)
                })
            else:
                # Row has no numeric values
                results.append({
                    'row_number': row_num,
                    'values': [],
                    'sum': 0,
                    'average': 0
                })
        
        # Check if we processed any rows with data
        if row_count == 0:
            raise InvalidCSVFormatError("CSV file contains no valid data rows")
            
    except FileNotFoundError:
        raise
    except InvalidCSVFormatError:
        raise
    except ValueError:
        raise
    except PermissionError:
        raise PermissionError(f"Permission denied to access file '{filename}'")
    except Exception as e:
        raise InvalidCSVFormatError(f"Error processing CSV file: {str(e)}")
    
    finally:
        # Ensure file is properly closed
        if file_handle and not file_handle.closed:
            file_handle.close()
    
    return results

def print_results(results, filename):
    """Helper function to print results in a formatted way"""
    print(f"\nProcessing results for '{filename}':")
    print("-" * 50)
    
    if not results:
        print("No data to display")
        return
    
    for result in results:
        print(f"Row {result['row_number']}: {result['values']}")
        print(f"  Sum: {result['sum']}")
        print(f"  Average: {result['average']}")
        print()

# Test the function with different scenarios
def test_csv_processor():
    """Test function with various scenarios"""
    
    test_files = [
        "valid_data.csv",
        "non_existent_file.csv", 
        "invalid_data.csv"
    ]
    
    for filename in test_files:
        print(f"\n{'='*60}")
        print(f"Testing with file: {filename}")
        print('='*60)
        
        try:
            results = process_csv(filename)
            print_results(results, filename)
            print("✓ File processed successfully!")
            
            
        except FileNotFoundError as e:
            print(f"❌ File Error: {e}")
            
        except InvalidCSVFormatError as e:
            print(f"❌ Format Error: {e}")
            
        except ValueError as e:
            print(f"❌ Data Error: {e}")
            
        except PermissionError as e:
            print(f"❌ Permission Error: {e}")
            
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    # Example usage
    print("CSV File Processor")
    print("=" * 50)
    
    #You can test with actual files like this:
    try:
        results = process_csv("users.csv")
        print_results(results, "users.csv")
    except Exception as e:
        print(f"Error: {e}")
    
    # Run tests
    test_csv_processor()
