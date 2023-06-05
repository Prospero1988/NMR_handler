import csv
import os

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
    new_filename = filename + "_bucketed.csv"
    with open(new_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return new_filename


# General message
print()
print(" |--------------------------------------|")
print(" |----------BUCKET INTEGRATION----------|")
print(" |----for NMR data sets in CSV files----|")
print(" |--------------------------------------|")
print(" |-by Arkadiusz Leniak -----------------|")
print(" |-arek.kein@gmail.com -----------------|")
print(" |--------------------------------------|")
print()

# Step 1: Provide the name of the directory
directory = input("Enter the name of the directory containing the CSV files: ")

# Step 2: Load and process data from CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        print("Processing file:", filename)
        data = load_data_from_csv(filepath)

        # Step 3: Divide the number of columns into ranges and create bucketed data
        n = int(input("Enter the number of ranges: "))
        bucketed_data = create_bucketed_data(data, n)

        # Step 4: Create a new file with range values
        new_filename = save_data_to_csv(bucketed_data, filename)

        print("Created a new file:", new_filename)
        print()

print("Processing completed for all files in the directory.")

