import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import sys

def interpolate_row(row, new_length, kind):
    x = np.arange(len(row))
    y = row
    f = interp1d(x, y, kind=kind)

    new_x = np.linspace(0, len(row) - 1, new_length)
    return f(new_x)

def interpolate_csv(input_file, output_file, new_length, kind):
    df = pd.read_csv(input_file, header=None)
    interpolated_data = []
    for _, row in df.iterrows():
        interpolated_row = interpolate_row(row.values, new_length, kind)
        interpolated_data.append(interpolated_row)
    interpolated_df = pd.DataFrame(interpolated_data)
    interpolated_df.to_csv(output_file, index=False, header=False)

def plot_row(data, row_number, ax, plot_type):
    if 0 <= row_number < len(data):
        selected_row = data[row_number]
        x_values = range(1, len(selected_row) + 1)
        ax.plot(x_values, selected_row)
        ax.set_xlabel('Column')
        ax.set_ylabel('Value')
        row_number_visible = row_number + 1

        if plot_type == 'original':
            ax.set_title('Plot of row ' + str(row_number_visible))
        elif plot_type == 'interpolated':
            ax.set_title('Plot of row ' + str(row_number_visible) + ' after interpolation')
    else:
        print("Invalid row number. No plot will be generated")

def print_help():
    print()
    print("Interpolation Script for NMR Data Sets in CSV Files")
    print("by Arkadiusz Leniak (arek.kein@gmail.com)")
    print()
    print("This script performs interpolation on NMR (Nuclear Magnetic Resonance) data sets")
    print("stored in CSV (Comma-Separated Values) files. It allows you to interpolate the data")
    print("to a specified number of columns using different interpolation methods.")
    print()
    print("Usage:")
    print("python interpolation2.py --help")
    print()
    print("Options:")
    print("--help          : Show this help message and exit.")
    print()
    print("Before running the script, make sure you have the necessary dependencies installed:")
    print("- pandas")
    print("- matplotlib")
    print("- numpy")
    print("- scipy")
    print()
    print("To use the script, follow these steps:")
    print("1. Run the script by executing 'python script.py'.")
    print("2. Specify the input file name (CSV file containing the NMR data).")
    print("3. Specify the output file name (CSV file to save the interpolated data).")
    print("4. Enter the target number of columns after interpolation.")
    print("5. Choose an interpolation method from the available options.")
    print("6. Specify the row number to draw a graph for that particular row.")
    print("7. The script will generate two plots: one for the original data and one for the interpolated data.")
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
    input_file = input("Specify input file name: ")
    print()
    output_file = input("Specify output file name: ")
    print()

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [list(map(float, row)) for row in reader]

        num_columns = len(header)
        print("Number of columns in the loaded file: ", num_columns)
        print()
        num_rows = len(data)  # Count the rows in the loaded data list
        print("Number of rows in the loaded file:", num_rows)
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

    row_number = int(input("Drawing a graph for a row from the data.\n\nSpecify the number of the row: "))
    row_number -= 1
    print()

    # Turn on interactive mode
    plt.ion()
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.8)

    # Draw the first plot
    plot_row(data, row_number, ax1, 'original')

    # Interpolate the CSV file
    interpolate_csv(input_file, output_file, new_length, kind)

    # Read output file for the second plot
    with open(output_file, 'r') as file2:
        reader = csv.reader(file2)
        data = [list(map(float, row)) for row in reader]

    # Draw the second plot
    plot_row(data, row_number, ax2,  'interpolated')

    # Show the plots
    plt.show()

    input("Press Enter to finish the script: ")
    print()

if __name__ == '__main__':
    main()
