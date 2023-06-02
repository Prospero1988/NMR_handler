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
# Add headers to the final CSV files
print()
final_file_path = input("Specify input file path: ")

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

while True:
    print()
    choice = input(f"Do you want to add headers to columns in {final_file_path}? (yes/no): ")
    if choice == 'yes':
        print()
        custom_headers = input("Specify headers name: ")
        df = pd.read_csv(final_file_path)
        headers = [custom_headers + str(i + 1) for i in range(len(df.columns))]
        df.columns = headers
        df.to_csv(final_file_path, index=False)
        print()
        print(f"{custom_headers}1, {custom_headers}2, {custom_headers}3, etc. column headers has been")
        print(f"added to {len(df.columns)} columns in {final_file_path} CSV file.")

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

        break
    else:
        break

# Appending first column from other CSV files

while True:
    print()
    choice = input("Do you want to append (add) first column to the file from another CSV file?\nYou can choose which column will be extracted from second CSV file. \n\n(yes/no)?: ")
    if choice == 'yes':

        # Read the first CSV file into a DataFrame
        df1 = pd.read_csv(final_file_path)

        # Ask the user to input the path for the second CSV file
        print()
        second_file_path = input("Enter the path for the second CSV file: ")
        second_file_path = second_file_path
        # Read the second CSV file into a DataFrame
        df2 = pd.read_csv(second_file_path)

        # Get the number of columns in the DataFrame
        num_columns = len(df2.columns)

        # Print the number of columns
        print()
        print("Number of columns:", num_columns)

        while True:
            # Validate the column number input
            print()
            column_number = int(input("Enter the column number to copy: ")) - 1

            if column_number < 0 or column_number >= len(df2.columns):
                print()
                print("Invalid column number!")
            else:
                break

        # Extract the column you want to copy from the second file
        column_name = df2.columns[column_number]
        column_to_copy = df2.iloc[:, column_number]

        # Insert the copied column as the first column in the first file
        df1.insert(0, column_name, column_to_copy)

        # Save the updated DataFrame to the first CSV file
        df1.to_csv(final_file_path, index=False)
        print()
        column_number = column_number + 1
        print(f"----> Column {column_number} from {second_file_path} was copied successfuly")
        print(f"      to the {final_file_path} and saved as a first column.")
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

            print(f"----> File contains {num_columns_df} columns and {num_rows_df} rows.")
            print()
        break
    else:
        print()
        print("----> Column appending process canceled.")
        print()
        break
KONIEC = input("Press ENTER to end script: ")
sys.exit(1)
