import pandas as pd
from MulticoreTSNE import MulticoreTSNE as TSNE
import numpy as np
import os
import sys

def print_help():
    print()
    print("MulticoreTSNE Dimensionality Reduction Script")
    print()
    print("This script performs dimensionality reduction on a given dataset using the MulticoreTSNE library.")
    print("It reduces the dimensionality of the input data to a specified target dimension.")
    print()
    print("Usage:")
    print("python mctsne.py --help")
    print()
    print("Options:")
    print("--help          : Show this help message and exit.")
    print()
    print("Before running the script, make sure you have the necessary dependencies installed:")
    print("- pandas")
    print("- MulticoreTSNE")
    print()
    print("To use the script, follow these steps:")
    print("1. Install the MulticoreTSNE library by following the instructions provided by the author:")
    print("   https://github.com/DmitryUlyanov/Multicore-TSNE/")
    print("2. Run the script by executing 'python script.py'.")
    print("3. Enter the name of the .csv file containing the input data.")
    print("4. Specify the target dimensionality for the dimensionality reduction.")
    print("5. Specify the number of significant places to round off the values after performing MulticoreTSNE reduction.")
    print("6. The script will perform the dimensionality reduction using MulticoreTSNE.")
    print("7. The reduced data will be saved in a new .csv file with '_MCTSNE' suffix in the same directory as the input file.")
    print()
    
if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

print()
print("Check how to install MulticoreTSNE library at github site of the author:")
print("https://github.com/DmitryUlyanov/Multicore-TSNE/")
print()
print()
# prompt for the name of the .csv file
filepath = input("Enter the name of the .csv file: ")

# read the data from the .csv file
data = pd.read_csv(filepath, header=None)

# prompt for the target dimensionality
print()
target_dim = int(input("Enter target dimensionality: "))

# Specify significantnumbers in rounding values
print()
decimals = int(input("Specify how many significant places to round off the values after performing MulticoreTSNE reduction: "))

# perform dimensionality reduction using MulticoreTSNE
reducer = TSNE(n_components=target_dim, n_jobs=-1)

# Reducing data
reduced_data = reducer.fit_transform(data)

# Round the reduced_data to the specified number of decimal places
reduced_data = np.round(reduced_data, decimals)

# save the reduced data to a new .csv file
filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_MCTSNE.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)

pd.DataFrame(reduced_data).to_csv(output_filepath, header=False, index=False)

print()
print(f">>> Data saved as: {output_filepath}")
print()
KONIEC = input("Press Enter to finish the script: ")
print()
exit()
