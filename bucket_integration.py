import csv
import matplotlib.pyplot as plt
import os
import sys

def plot_row(data, row_number, ax, plot_type):
    if 0 <= row_number < len(data):
        selected_row = data[row_number]
        x_values = range(1, len(selected_row) + 1)
        ax.plot(x_values, selected_row)
        ax.set_xlabel('Column')
        ax.set_ylabel('Value')

        if plot_type == 'original':
            ax.set_title('Plot of row ' + str(row_number))
        elif plot_type == 'bucketed':
            ax.set_title('Plot of row ' + str(row_number) + ' bucket integrated')
    else:
        print("Invalid row number. No plot will be generated")


def load_data_from_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = [list(map(float, row)) for row in reader]
    return data


def create_bucketed_data(data, n):
    num_columns = len(data[0])
    if num_columns % n != 0:
        print("The number of columns is not divisible by the number of ranges.")
        exit()

    columns_per_range = num_columns // n

    new_data = []
    for row in data:
        new_row = []
        for i in range(n):
            range_values = [float(value) for value in row[i * columns_per_range:(i + 1) * columns_per_range]]
            sum_points = sum(value for value in range_values if value != 0)
            new_row.append(sum_points)
        new_data.append(new_row)

    return new_data


def save_data_to_csv(data, filename):
    file_name, file_extension = os.path.splitext(filename)
    new_filename = os.path.join(file_name + "_bucketed" + file_extension)
    with open(new_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return new_filename

def print_help():
    print()
    print("Usage: python bucket_integration.py [input_file]")
    print("Options:")
    print("  --help          Display this help message")
    print()
    print("Description:")
    print("This script performs bucket integration on NMR (Nuclear Magnetic Resonance) data sets stored in CSV files.")
    print("It allows you to analyze and manipulate the data by dividing the columns into ranges and creating a new file with the integrated values.")
    print()
    print("Steps:")
    print("1. Provide the name of the input CSV file when prompted.")
    print("2. The script will load the data from the input file.")
    print("3. You will be prompted to specify the row number to plot on a graph.")
    print("4. The script will create a graph with two subplots: the original row and the bucket-integrated row.")
    print("5. Enter the number of ranges to divide the columns into.")
    print("6. The script will create a new file with the integrated values.")
    print("7. The name of the new file will be displayed.")
    print("8. The script will load the new file and plot the specified row on the second subplot.")
    print("9. Press ENTER to finish and exit the script.")
    print()

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

# General message
print()
print()
print(" |--------------------------------------|")
print(" |----------BUCKET INTEGRATION----------|")
print(" |----for NMR data sets in CSV files----|")
print(" |--------------------------------------|")
print(" |-by Arkadiusz Leniak -----------------|")
print(" |-arek.kein@gmail.com -----------------|")
print(" |--------------------------------------|")
print()

# Step 1: Provide the name of the batch file
print()
filename = input("Enter the name of the input file: ")

# Step 2: Load data from the batch file
data = load_data_from_csv(filename)

# Plotting the graph
print()
row_number = int(input("Drawing a graph for a row from the data.\n\nSpecify the number of the row: "))

# Turn on interactive mode
plt.ion()

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1)

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.8)

# Draw the first plot
plot_row(data, row_number, ax1, 'original')

# Step 3: Divide the number of columns into ranges and create bucketed data
print()
n = int(input("Enter the number of ranges: "))
bucketed_data = create_bucketed_data(data, n)

# Step 4: Create a new file with range values
new_filename = save_data_to_csv(bucketed_data, filename)

print()
print("Processing completed. Created a new file:", new_filename)

# Plotting the second graph
datax2 = load_data_from_csv(new_filename)

# Draw the second plot
plot_row(datax2, row_number, ax2, 'bucket integrated')

print()
input("To finish, press ENTER:  ")
print()
