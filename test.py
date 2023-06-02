# Import libraries
import os
import csv
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd

def remove_columns(data, ranges):
    cleaned_data = []
    for row in data:
        cleaned_row = []
        for i, value in enumerate(row):
            skip_column = any(start <= i <= end for start, end in ranges)
            if not skip_column:
                cleaned_row.append(value)
        cleaned_data.append(cleaned_row)
    return cleaned_data

def normalize_dataset(dataset):
    min_value = np.min(dataset)
    max_value = np.max(dataset)
    normalized_dataset = (dataset - min_value) / (max_value - min_value)
    rounded_dataset = np.round(normalized_dataset, decimals=decimals)
    return rounded_dataset

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Generate message
print()
print()
print(" |--------------------------------------|")
print(" |---------NORMALIZATION SCRIPT---------|")
print(" |----for NMR data sets in CSV files----|")
print(" |--------------------------------------|")
print(" |-by Arkadiusz Leniak -----------------|")
print(" |-arek.kein@gmail.com -----------------|")
print(" |-------------------------------------------------------------------------------|")
print(" | 1.  It loads a directory containing files with the extension *.csv,           |")
print(" |     in which the columns are separated by commas. Then it selects             |")
print(" |     only the second column from each file and adds it to one temporary        |")
print(" |     output file as a new column.                                              |")
print(" | 2.  The temporary file is then transposed - columns are converted to rows     |")
print(" |     and saved as an output file. Script draws a plot of selected data row.    |")
print(" | 3.  In the next step, the script deletes the unwanted columns from data set.  |")
print(" |     It asks user to specify the number of column ranges to delete, and then   |")
print(" |     define those ranges. After removing columns from the dataset, the script  |")
print(" |     adds a second chart below the already active one.                         |")
print(" | 4.  The script performs normalization of the data in rows in the range <0,1>  |")
print(" |     and draws a third graph under the previous two.                           |")
print(" | 5.  Each step creates temporary file that can be delted at the end of script. |")
print(" |-------------------------------------------------------------------------------|")
print()


# Ask for input directory with .csv files
while True:
    print()
    input_dir = input("Enter the input directory path containing .csv files: ")

    if not os.path.exists(input_dir):
        print()
        print(">>> Directory does not exist.")
        print()
        choice = input("Do you want to enter a correct directory path? (yes/no): ")

        if choice.lower() != 'yes':
            print()
            print(">>> Terminating script.")
            print()
            sys.exit(1)
    else:
        csv_files = [file for file in os.listdir(input_dir) if file.endswith('.csv')]
        num_csv_files = len(csv_files)

        if num_csv_files == 0:
            print()
            print(">>> Directory exists but no .csv files found in the directory.")
            print()
            choice = input("Would you like to enter a new directory path? (yes/no): ")

            if choice.lower() != 'yes':
                print()
                print(">>> Terminating script.")
                print()
                sys.exit(1)
                break
        else:
            print()
            print(">>> Number of CSV files found in the directory:", num_csv_files)
            break

# Step 3: Ask for output .csv file name
while True:
    print()
    norm_file = input("Enter the output file name (without .csv suffix): ")
    if os.path.isfile(norm_file):
        overwrite = input("The output file already exists. Do you want to overwrite it? (yes/no): ")
        if overwrite.lower() == "yes":
            break
        elif choice == 'no':
            norm_file = input("Enter a new output CSV file name: ")
        else:
            print(">>> Invalid choice. Please enter 'yes' or 'no'.")
    else:
        break

# Get a list of all .csv files in the input directory
csv_files = sorted([file for file in os.listdir(input_dir) if file.endswith('.csv')])

# Process each file and merge into the output file
output_data = []  # List to store merged data

for csv_file in csv_files:
    file_path = os.path.join(input_dir, csv_file)

    with open(file_path, 'r') as infile:
        reader = csv.reader(infile)
        column_data = []
        for row in reader:
            if len(row) >= 2:
                column_data.append(row[1])  # Extract the second column

        output_data.append(column_data)  # Append extracted column data to the merged data

# Save merged data to TEMP.csv
temp_file = 'TEMP.csv'

df = pd.read_csv(temp_file)
num_columns_df = len(df.columns)
num_rows_df = len(df)
num_rows_df = num_rows_df + 1

print()
print(f"----> Column Filtering and Merging completed. Data saved to '{temp_file}'.")
print(f"      File contains {num_columns_df} columns and {num_rows_df} rows.")

with open(temp_file, 'w', newline='') as temp_outfile:
    writer = csv.writer(temp_outfile)

    for row in zip(*output_data):
        writer.writerow(row)

# Define trenspose function
def transpose_csv():

    # Read and transpose the CSV data
    with open(temp_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        transposed_data = list(zip(*data))

    # Save the transposed data to the TEMP2.csv file
    temp_file2 = 'TEMP2.csv'
    with open(temp_file2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transposed_data)

    df = pd.read_csv(temp_file2)
    num_columns_df = len(df.columns)
    num_rows_df = len(df)

    print()
    print(f"----> Transposition of data completed. Data saved to '{temp_file2}'.")
    print(f"      File contains {num_columns_df} columns and {num_rows_df} rows.")
transpose_csv()
