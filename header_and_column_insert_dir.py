import os
import csv
import sys
import pandas as pd

# Generate message
print()
print()
print(" |--------------------------------------|")
print(" |--------CSV Manipulation SCRIPT-------|")
print(" |----for NMR data sets in CSV files----|")
print(" |-------------------------------------------------------------------------------|")
print(" | 1.  Script asks if user wants to add headers to the data (as C1, C2, C3, etc.)|")
print(" | 2.  Script asks if user wants to copy defined column from another CSV file    |")
print(" |     as the first column to the current one                                    |")
print(" |-------------------------------------------------------------------------------|")
print()

# Get the directory path
directory_path = input("Enter the directory path containing the CSV files: ")
print()
# Get the list of CSV files in the directory
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

custom_headers = input("Specify headers name: ")
# Ask the user to input the path for the second CSV file
print()
second_file_path = input("Enter the path for the second CSV file: ")
second_file_path = second_file_path
print()
column_number = int(input("Enter the column number to copy: ")) - 1

# Process each CSV file in the directory
for file_name in csv_files:
    print()
    print(f"Processing file: {file_name}")
    print("------------------------------------------------------------")

    # Add headers to the final CSV file
    final_file_path = os.path.join(directory_path, file_name)

    # Check number of columns and rows
    with open(final_file_path, 'r') as input_file:
        reader = csv.reader(input_file)
        data = [list(map(float, row)) for row in reader if all(value.replace('.', '', 1).isdigit() for value in row)]

    df = pd.read_csv(final_file_path)
    num_columns_df = len(df.columns)
    num_rows_df = len(df)
    num_rows_df = num_rows_df + 1

    print()
    print(f"----> File contains {num_columns_df} columns and {num_rows_df} rows.")


    df = pd.read_csv(final_file_path)
    headers = [custom_headers + str(i + 1) for i in range(len(df.columns))]
    df.columns = headers
    df.to_csv(final_file_path, index=False)
    print()
    print(f"{custom_headers}1, {custom_headers}2, {custom_headers}3, etc. column headers has been")
    print(f"added to {len(df.columns)} columns in {file_name} CSV file.")

    with open(final_file_path, 'r') as input_file:
        reader = csv.reader(input_file)
        data = []
        for row in reader:
            converted_row = []
            for value in row:
                try:
                    converted_row.append(float(value))
                except ValueError:
                    converted_row.append(value)
            data.append(converted_row)

    df = pd.read_csv(final_file_path)
    num_columns_df = len(df.columns)
    num_rows_df = len(df)
    num_rows_df += 2

    print()
    print(f"----> File contains {num_columns_df} columns and {num_rows_df} rows.")


    # Appending first column from other CSV files

    # Read the first CSV file into a DataFrame
    df1 = pd.read_csv(final_file_path)


    # Read the second CSV file into a DataFrame
    df2 = pd.read_csv(second_file_path)

    # Get the number of columns in the DataFrame
    num_columns = len(df2.columns)

    # Print the number of columns
    print()
    print("Number of columns:", num_columns)

    while True:
        # Validate the column number input
        column_number2 = column_number
        if column_number2 < 0 or column_number >= len(df2.columns):
            print()
            print("Invalid column number!")
        else:
            break

    # Extract the column you want to copy from the second file
    column_name = df2.columns[column_number2]
    column_to_copy = df2.iloc[:, column_number2]

    # Insert the copied column as the first column in the first file
    df1.insert(0, column_name, column_to_copy)

    # Save the updated DataFrame to the first CSV file
    df1.to_csv(final_file_path, index=False)
    print()
    column_number2 = column_number2 + 1
    print(f"----> Column {column_number2} from {second_file_path} was copied successfuly")
    print(f"      to the {file_name} and saved as a first column.")
    print()

    with open(final_file_path, 'r') as input_file:
        reader = csv.reader(input_file)
        data = []
        for row in reader:
            converted_row = []
            for value in row:
                try:
                    converted_row.append(float(value))
                except ValueError:
                    converted_row.append(value)
            data.append(converted_row)

        df = pd.read_csv(final_file_path)
        num_columns_df = len(df.columns)
        num_rows_df = len(df)
        num_rows_df += 2
    column_number2 = None
    print(f"----> File contains {num_columns_df} columns and {num_rows_df} rows.")
    print()

print("------------------------------------------------------------")
KONIEC = input("Press ENTER to end script: ")
sys.exit(1)
