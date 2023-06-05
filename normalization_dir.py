import csv
import numpy as np
import os

# General message
print()
print()
print(" |--------------------------------------|")
print(" |---------INTERPOLATION SCRIPT---------|")
print(" |----for NMR data sets in CSV files----|")
print(" |--------------------------------------|")
print(" |-by Arkadiusz Leniak -----------------|")
print(" |-arek.kein@gmail.com -----------------|")
print(" |--------------------------------------|")
print()

def normalize_dataset(dataset):
    min_value = np.min(dataset)
    max_value = np.max(dataset)
    normalized_dataset = (dataset - min_value) / (max_value - min_value)
    scaled_dataset = (normalized_dataset * factor)
    rounded_dataset = np.round(scaled_dataset, decimals=decimals)
    return rounded_dataset

print()
directory_path = input("Type the directory path containing CSV files for normalization: ")
print()
# Prompt the user for the value of factor for normalization
print()
print(">> When you choose multiplication factor = 1, then values after normalization")
print(">> will be in the range of [0,1]; factor = 10, values =[0,10]; factor = 100, values = [0,100], etc.)")
print()
factor = int(input("Enter the value of the factor: "))

# Prompt the user for the number of decimals in rounding
print()
decimals = int(input("Enter the number of decimals for rounded values (0,XXXX): "))
print()

# Process each CSV file recursively
for root, dirs, files in os.walk(directory_path):
    for csv_file in files:
        if csv_file.endswith(".csv"):
            # Read the input CSV file
            file_path = os.path.join(root, csv_file)
            with open(file_path, 'r') as input_file:
                reader = csv.reader(input_file)
                data = [list(map(float, row)) for row in reader]

            # Normalize each dataset in the rows
            normalized_data = [normalize_dataset(row) for row in data]

            # Prepare the output file path
            file_name, file_extension = os.path.splitext(csv_file)
            output_file_path = os.path.join(root, file_name + "_normalized" + file_extension)

            # Write the processed data to the output file
            with open(output_file_path, 'w', newline='') as normalized_file:
                writer = csv.writer(normalized_file)
                writer.writerows(normalized_data)

            print(f"----> File {output_file_path} saved.")

print()
print("----> Normalization complete.")
print()
