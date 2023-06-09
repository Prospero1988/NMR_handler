import pandas as pd
from sklearn.decomposition import NMF
import numpy as np
import os
import sys

def reduce_csv_nmf(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the NMF model with n_components
    nmf = NMF(n_components=n_components)

    # Fit the NMF model on the data
    nmf.fit(data)

    # Transform the data to the new lower-dimensional space
    reduced_data = nmf.transform(data)

    # Round the reduced_data to the specified number of decimal places
    reduced_data = np.round(reduced_data, decimals)

    # Save the reduced data to a new csv file
    pd.DataFrame(reduced_data).to_csv(output_filepath, index=False, header=False)

    # Get the basis matrix from NMF
    basis_matrix = nmf.components_

    print()
    print(f">>> Basis matrix shape: {basis_matrix.shape}")
    print(f">>> Basis matrix:\n\n{basis_matrix}")
    print()

def print_help():
    print()
    print("Dimensionality Reduction Script using NMF")
    print("---------------------------------------")
    print("This script performs dimensionality reduction on a .csv file using the NMF (Non-negative Matrix Factorization) model.")
    print("During the reduction, the script creates a new lower-dimensional data matrix by rounding the results to a specified number of decimal places.")
    print("The reduced data matrix is saved to a new .csv file.")
    print()
    print("Usage:")
    print("python nmf.py [--help]")
    print()
    print("Arguments:")
    print("  --help       Displays this help message and exits the script.")
    print()
    print("When running the script without any arguments, you will be prompted to enter the number of components, the path to the input .csv file, and the number of decimal places.")
    print("The output file will be saved in the same location as the input file with the suffix _NMF.")
    print()
    
if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

while True:
    try:
        print()
        n_components = int(input("Enter the number of components (should be less or equal to the number of features in data): "))
        if n_components <= 0:
            raise ValueError
        break
    except ValueError:
        print()
        print("Enter a correct value")
        continue

print()
filepath = input("Enter the path to the input .csv file: ")
print()
filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_NMF.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
decimals = int(input("Specify how many significant places to round off the values after performing NMF: "))
print()
reduce_csv_nmf(filepath, n_components, output_filepath)
print()
KONIEC = input("Press Enter to finish the script: ")
print()
exit()
