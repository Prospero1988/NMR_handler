import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import os
import sys

def reduce_csv_pca(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the PCA model with n_components
    pca = PCA(n_components=n_components)

    # Fit the PCA model on the data
    pca.fit(data)

    # Transform the data to the new lower-dimensional space
    reduced_data = pca.transform(data)

    # Round the reduced_data to 3 decimal places
    reduced_data = np.round(reduced_data, decimals)

    # Save the reduced data to a new csv file
    pd.DataFrame(reduced_data).to_csv(output_filepath, index=False, header=False)

    # explain variance ratio
    explained_var = pca.explained_variance_ratio_
    print()
    print(f">>> Explained variance ratio by each dimension: \n\n{explained_var}")
    print()

def print_help():
    print()
    print("This script performs dimensionality reduction using PCA on data stored in a CSV file.")
    print("Usage: python pca.py [--help]")
    print()
    print("Options:")
    print("  --help     Display this help message and exit.")
    print()
    print("Description:")
    print("  This script reads a CSV file containing data and reduces its dimensionality using PCA (Principal Component Analysis).")
    print("  It prompts the user to enter the file path of the input CSV file.")
    print("  The user is asked to provide the number of components to keep after dimensionality reduction.")
    print("  The script applies PCA on the data and transforms it to the lower-dimensional space.")
    print("  The reduced data is then rounded to the specified number of significant places.")
    print("  The processed data is saved to a new CSV file with '_PCA' appended to the original file name.")
    print("  Additionally, the explained variance ratio by each dimension is printed.")
    print()
    print("Example:")
    print("  python pca.py")
    print("  - This will run the script and prompt the user to enter the necessary inputs.")
    print("  python pca.py --help")
    print("  - This will display this help message and exit the script.")
    print()

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

while True:
    try:
        print()
        n_components = int(input("Enter the number of components (should be less or equal to number of features in data): "))
        if n_components <=0:
            raise ValueError
        break
    except ValueError:
        print()
        print("Enter correct value")
        continue
print()
filepath = input("Enter path to the input .csv file: ")
print()
filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_PCA.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
decimals = int(input("Specify to how many significant places to round off the values after performing PCA: "))
print()
reduce_csv_pca(filepath, n_components, output_filepath)
KONIEC = input("Press Enter to finish script: ")
print()
exit()
