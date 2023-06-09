import csv
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import os
import sys

def interpolate_row(row, new_length, kind):
    x = np.arange(len(row))
    y = row
    f = interp1d(x, y, kind=kind)

    new_x = np.linspace(0, len(row) - 1, new_length)
    return f(new_x)

def interpolate_csv(file_path, output_file, new_length, kind):
    df = pd.read_csv(file_path, header=None)
    interpolated_data = []
    for _, row in df.iterrows():
        interpolated_row = interpolate_row(row.values, new_length, kind)
        interpolated_data.append(interpolated_row)
    interpolated_df = pd.DataFrame(interpolated_data)
    interpolated_df.to_csv(output_file, index=False, header=False)

def print_help():
    print()
    print("This script performs interpolation on NMR data sets stored in CSV files.")
    print("It takes a directory path containing the CSV files and interpolates each file individually.")
    print("The user is prompted to enter the target number of columns after interpolation and to choose an interpolation method.")
    print("The interpolated files are saved with '_interpolated' appended to their names in the same directory.")
    print()
    print("Usage: python interpolation_dir.py [--help]")
    print()
    print("Options:")
    print("  --help: Print this help message and exit.")
    print()
    
if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)
    
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

def main():
    print()
    directory_path = input("Type the directory path containing CSV files for interpolation: ")
    print()
    new_length = int(input("Enter the target number of columns after interpolation: "))
    print()
    print("Possible interpolation methods: ")
    print()
    print("'linear': Perform linear interpolation.")
    print("'nearest': Perform nearest-neighbor interpolation.")
    print("'zero': Perform zero-order hold interpolation.")
    print("'slinear': Perform linear spline interpolation.")
    print("'quadratic': Perform quadratic spline interpolation.")
    print("'cubic': Perform cubic spline interpolation.")
    print()
    kind = str(input("Choose method for interpolation: "))
    print()


    # Process each CSV file recursively
    for root, dirs, files in os.walk(directory_path):
        for csv_file in files:
             if csv_file.endswith(".csv"):

                # Read the input CSV file
                file_path = os.path.join(root, csv_file)
                
                # Prepare the output file path
                file_name, file_extension = os.path.splitext(csv_file)
                output_file = os.path.join(file_name + "_interpolated" + file_extension)

                # Interpolate the CSV file
                interpolate_csv(file_path, output_file, new_length, kind)

                print(f"----> File {output_file} saved.")

    # Finish script
    print()
    input("Press Enter to finish the script: ")
    print()

if __name__ == '__main__':
    main()
