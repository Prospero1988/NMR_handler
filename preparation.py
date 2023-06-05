# Import libraries
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shutil

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
    scaled_dataset = (normalized_dataset * factor)
    rounded_dataset = np.round(scaled_dataset, decimals=decimals)
    return rounded_dataset

# General message
print()
print()
print(" |--------------------------------------|")
print(" |----------PREPARATION SCRIPT----------|")
print(" |----for NMR data sets in CSV files----|")
print(" |--------------------------------------|")
print(" |-by Arkadiusz Leniak -----------------|")
print(" |-arek.kein@gmail.com -----------------|")
print(" |--------------------------------------|")
print()

while True: 
    print()
    print(">>> If you need any additional informations about the script type: help ")
    start_script = input (">>> if not just press ENTER: ")
    if start_script.lower() == 'help':
        print()
        print("  1.  Script asks for a path to the directory that contains files with the extension *.csv,")
        print("      in which the columns represent datasets. Then scripts selects only the second column")
        print("      from each file and adds it to one temporary output file as a new, next column.")
        print()
        print("  2.  The temporary file is then transposed - columns are converted to rows and saved ")
        print("      as an second output temporary file. Script draws a plot of selected data row.")
        print()
        print("  3.  In the next step, the script deletes selected columns from data sets.")
        print("      Script asks user to specify the number of column ranges to delete, and then")
        print("      prompts to define those ranges. After removing columns from the dataset, the script")
        print("      draws a second plot below the already active one. User can choose zero")
        print("      ranges, which will skip the step of deleting columns from the dataset.")
        print()
        print("  4.  The script will ask user to normalize the data. Process could be skipped. ")
        print("      Normalization will be carried out in any range from 0 to N. User specifies")
        print("      N factor. Script draws a plot after this process.")
        print()
        print("  5.  Each step creates temporary file. At the end of the script, the user will be asked.")
        print("      if he wants to delete temporary files")
        print()
        break
    else:
        break

# Ask for input directory with .csv files
while True:
    print()
    input_dir = input("Enter the input directory path containing .csv files: ")

    if not os.path.exists(input_dir):
        print()
        print(">>> Directory does not exist.")

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
                exit()
                break
        else:
            print()
            print(">>> Number of CSV files found in the directory:", num_csv_files)
            break

# Step 3: Ask for output .csv file name
while True:
    print()
    norm_file = input("Enter the output file name: ")
    end_file = norm_file
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

temp_file = 'TEMP.csv'

# Write the merged data to the output file
with open(temp_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(zip(*output_data))

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
    num_rows_df = num_rows_df + 1

    print()
    print(f"----> Transposition of data completed. Data saved to '{temp_file2}'.")
    print(f"      File contains {num_columns_df} columns and {num_rows_df} rows.")
transpose_csv()

# Ask for the row number to be used for the plot
print()
row_number = int(input(">>> Drawing a graph for a row from the data after the transposition.\n>>> Specify the number of the row: "))
row_number -= 1 
row_number_visible = row_number + 1 

# Read the input TEMP2.csv file
temp_file2 = 'TEMP2.csv'
with open(temp_file2, 'r') as input_file:
    reader = csv.reader(input_file)
    data = [list(map(float, row)) for row in reader]

# Turn on interactive mode
plt.ion()

# Create a figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.8)

# Draw a plot of the specified row
if 0 <= row_number < len(data):
    selected_row = data[row_number]
    x_values = range(1, len(selected_row) + 1)
    ax1.plot(x_values, selected_row)
    ax1.set_xlabel('Column')
    ax1.set_ylabel('Value')

    ax1.set_title('Plot of RAW row ' + str(row_number_visible), fontsize = 8)
    plt.show()
else:
    print()
    print(">>> Invalid row number. No plot will be generated")

# Prompt the user for the number of ranges to remove
print()
num_ranges = int(input("Enter the number of column ranges to be removed: "))

# Initialize the list to store the ranges
ranges = []

# Prompt for each range and add it to the list
if num_ranges > 0:
    for i in range(num_ranges):
        start = int(input(f"Enter the start column for range {i + 1}: "))
        end = int(input(f"Enter the end column for range {i + 1}: "))
        ranges.append((start, end))

        # Remove specified columns from the data
        cleaned_data = remove_columns(data, ranges)

        # Write the cleaned data to the temporary3 output file
        temp_file3 = 'TEMP3.csv'
        with open(temp_file3, 'w', newline='') as temp3_outfile:
            writer = csv.writer(temp3_outfile)
            writer.writerows(cleaned_data)

    print()
    print(f"----> Removing defined columns from file finished. Data saved to '{temp_file3}'.")

else:
    print()
    print(f"----> No columns removed.")
    # Write the cleaned data to the temporary3 output file
      
# Prompt for confirmation to draw a plot of a random row after removing defined columns.
print()
print(f">>> Drawing a graph of the same row after column deleting (row number {row_number_visible}).")

if num_ranges > 0:
    temp_file3 = 'TEMP3.csv'
else:
    temp_file3 = 'TEMP2.csv'

# Read the input CSV file
with open(temp_file3, 'r') as input_file:
    reader = csv.reader(input_file)
    data = [list(map(float, row)) for row in reader]

# Turn on interactive mode
plt.ion()

# Draw a plot of the specified row
selected_row = data[row_number]
x_values = range(1, len(selected_row) + 1)
ax2.plot(x_values, selected_row)
ax2.set_xlabel('Column')
ax2.set_ylabel('Value')
ax2.set_title('Plot of CLEANED row ' + str(row_number_visible), fontsize = 8)
plt.show()

# Create the "done" subdirectory if it doesn't exist
output_directory = 'processed_data'
os.makedirs(output_directory, exist_ok=True)

# Generate the output file path
final_file_path = os.path.join(output_directory, norm_file)

# Read the input CSV file
with open(temp_file3, 'r') as input_file:
    reader = csv.reader(input_file)
    data = [list(map(float, row)) for row in reader]

# Ask for normalization

while True: 
    print()
    ask_for_normal = input("Do you want to normalize dataset? (yes/no): ")
    if ask_for_normal.lower() == 'yes':

        # Prompt the user for the number of decimals in rounding
        print()
        decimals = int(input("Enter the number of decimals for rounded values (0,XXXX) after normalization: "))

        # Prompt the user for the value of factor to normalization
        print()
        print(">> When you choose multiplication factor = 1, then values after normalization")
        print(">> will be in range of [0,1]; factor = 10, values =[0,10]; factor = 100, values = [0,100], etc.)")
        factor = int(input("Specify the value of the factor for normalization: "))
        print()

        # Normalize each dataset in the rows
        normalized_data = [normalize_dataset(row) for row in data]
        print()
        print("----> Normalization completed.")

        # Write the processed data to the output file
        with open(final_file_path, 'w', newline='') as normalized_file:
            writer = csv.writer(normalized_file)
            writer.writerows(normalized_data)
        
        with open(final_file_path, 'r') as input_file:
            reader = csv.reader(input_file)
            data = [list(map(float, row)) for row in reader]

        df = pd.read_csv(final_file_path)
        num_columns_df = len(df.columns)
        num_rows_df = len(df)
        num_rows_df = num_rows_df + 1

        print(f"----> File contains {num_columns_df} columns and {num_rows_df} rows.")

        # Turn on interactive mode
        plt.ion()

        # Plot the selected row of data

        selected_row = data[row_number]
        x_values = range(1, len(selected_row) + 1)
        ax3.plot(x_values, selected_row)
        ax3.set_xlabel('Column')
        ax3.set_ylabel('Normalized Value')
        ax3.set_title('Plot of NORMALIZED row ' + str(row_number_visible), fontsize = 8)
        plt.show()
        break

    elif ask_for_normal.lower() == 'no':
        shutil.copyfile(temp_file3, final_file_path)
        break

    else:
        print()
        print("Incorrect input. Type yes or no. ")


# Delete the TEMP files
print()
removing_temps = input("Do you want to remove TEMP files after the script execution? (yes/no): ")
print()
if removing_temps.lower() =='yes':
    temp_file1 = 'TEMP.csv'
    temp_file2 = 'TEMP2.csv'
    temp_file3 = 'TEMP3.csv'

    if os.path.exists(temp_file1):
        os.remove(temp_file1)

    if os.path.exists(temp_file2):
        os.remove(temp_file2)

    if os.path.exists(temp_file3):
        os.remove(temp_file3)

    current_path = os.getcwd()
    print(">>> Script execution has been concluded with the erasing of all the TEMP files.")
    print(">>> CSV file with the processed data is saved in the directory: ")
    print()
    print(f"{current_path}\{output_directory}\{end_file}")
else:
    current_path = os.getcwd()
    print()
    print(">>> Script execution has been concluded without erasing any of the TEMP files.")
    print(f">>>> All temporary files are saved in the main script directory: {current_path}.")
    print()
    print(">>>> CSV file with the processed data set is saved in the directory: ")
    print()
    print(f"{current_path}\{output_directory}\{end_file}")
print()
print("-------------------------------------------------------------------------")
print()
#END
