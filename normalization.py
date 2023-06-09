import csv
import numpy as np
import os
import sys

def print_help():
    print()
    print("This script performs normalization on NMR data sets stored in CSV files.")
    print("Usage: python normalization.py [--help]")
    print()
    print("Options:")
    print("  --help     Display this help message and exit.")
    print()
    print("Description:")
    print("  This script reads an input CSV file and performs normalization on the dataset.")
    print("  It prompts the user to enter the file path of the input CSV file to be normalized.")
    print("  The user is also asked to provide the file path for the output file.")
    print("  Additionally, the user is prompted to enter a multiplication factor for normalization.")
    print("  The script normalizes each dataset in the input CSV file.")
    print("  It calculates the minimum and maximum values in the dataset, normalizes the values,")
    print("  scales them by the factor provided, and rounds the values to the specified number of decimals.")
    print("  The processed data is then written to the output CSV file.")
    print()
    print("Example:")
    print("  python script_name.py")
    print("  - This will run the script and prompt the user to enter the necessary inputs.")
    print("  python normalization.py --help")
    print("  - This will display this help message and exit the script.")
    print()
    
if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

# General message
print()
print()
print(" |--------------------------------------|")
print(" |---------NORMALIZATION SCRIPT---------|")
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
file_path = input("Type input file name for normalization: ")
print()
output_path = input("Type name for output file: ")
# Prompt the user for the value of factor to normalization
print()
print(">> When you choose multiplication factor = 1, then values after normalization")
print(">> will be in range of [0,1]; factor = 10, values =[0,10]; factor = 100, values = [0,100], etc.)")
print()
factor = int(input(" Enter the value of factor:  "))

# Prompt the user for the number of decimals in rounding
print()
decimals = int(input("Enter the number of decimals for rounded values (0,XXXX): "))

# Read the input CSV file
with open(file_path, 'r') as input_file:
    reader = csv.reader(input_file)
    data = [list(map(float, row)) for row in reader]

# Normalize each dataset in the rows
normalized_data = [normalize_dataset(row) for row in data]

# Write the processed data to the output file
with open(output_path, 'w', newline='') as normalized_file:
    writer = csv.writer(normalized_file)
    writer.writerows(normalized_data)

print()
print("----> Normalization complete.")
print()
print(f"----> File {output_path} saved.")
print()
