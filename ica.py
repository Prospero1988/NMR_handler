import pandas as pd
from sklearn.decomposition import FastICA
import numpy as np
import sys
import os

def reduce_csv_ica(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the ICA model with n_components
    ica = FastICA(n_components=n_components, whiten='arbitrary-variance')  # Set whiten to True

    # Fit the ICA model on the data
    ica.fit(data)

    # Transform the data to the new lower-dimensional space
    reduced_data = ica.transform(data)

    # Round the reduced_data to the specified number of decimal places
    reduced_data = np.round(reduced_data, decimals)

    # Save the reduced data to a new csv file
    pd.DataFrame(reduced_data).to_csv(output_filepath, index=False, header=False)

    # Get the mixing matrix (unmixing matrix) from ICA
    mixing_matrix = ica.components_

    print()
    print(f">>> Mixing matrix (unmixing matrix) shape: {mixing_matrix.shape}")
    print(f">>> Mixing matrix (unmixing matrix):\n{mixing_matrix}")
    print()

def print_help():
    print()
    print("Script Description:")
    print("The script performs Independent Component Analysis (ICA) on a given CSV file, reducing the dimensionality of the data by extracting independent components.")
    print()
    print("Usage:")
    print("python ica.py")
    print()
    print("Options:")
    print("--help: Display help information about the script.")
    print()
    print("Instructions:")
    print("1. Run the script without any command-line arguments.")
    print("2. Follow the prompts to enter the necessary information:")
    print("   - Enter the number of components (should be less than or equal to the number of features in the data).")
    print("   - Enter the path to the input .csv file.")
    print("   - Specify the number of significant decimal places to round off the values after performing ICA.")
    print("3. The script will perform ICA on the input data, save the reduced data to a new CSV file, and display the mixing matrix (unmixing matrix) shape and values.")
    print("4. Press Enter to finish the script.")
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
output_filename = filename[:-4] + '_ICA.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
decimals = int(input("Specify how many significant places to round off the values after performing ICA: "))
print()
reduce_csv_ica(filepath, n_components, output_filepath)
print()
KONIEC = input("Press Enter to finish the script: ")
print()
exit()
