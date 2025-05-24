import os

files_data = {
    'valid_data.csv': '10,20,30,40\n5.5,10.2,15.8\n100,200,300\n7,14,21,28,35\n2.5,7.5,12.5,17.5,22.5',
    'mixed_data.csv': '1,2,3,4,5\n10.5,20.3,30.7\n100,200\n5,10,15,20,25,30\n7.2,14.4,21.6',
    'invalid_data.csv': '10,20,30\nabc,40,50\n60,70,80',
    'empty_rows.csv': '10,20,30\n\n40,50,60\n\n70,80,90',
    'single_values.csv': '42\n3.14159\n100\n-25\n0',
    'negative_numbers.csv': '-10,20,-30,40\n-5.5,-10.2,15.8\n100,-200,300',
    'decimal_numbers.csv': '1.1,2.2,3.3,4.4\n0.5,1.5,2.5,3.5\n10.25,20.75,30.125',
    'large_numbers.csv': '1000000,2000000,3000000\n999.999,1000.001,2000.002\n5000,10000,15000,20000',
    'empty_file.csv': ''
}

for filename, content in files_data.items():
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

print("All test files created successfully!")
