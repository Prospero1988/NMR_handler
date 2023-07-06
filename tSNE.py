import pandas as pd
from fitsne import FItSNE
import numpy as np
import os
import sys
import time

def reduce_csv_tsne(filepath: str, n_components: int, output_filepath: str, decimals: int):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the t-SNE model with n_components
    fitsne = FItSNE(n_components=n_components)

    # Transform the data to the new lower-dimensional space
    reduced_data = fitsne.fit_transform(data)

    # Round the reduced_data to the specified number of decimal places
    reduced_data = np.round(reduced_data, decimals)

    # Save the reduced data to a new CSV file
    try:
        pd.DataFrame(reduced_data).to_csv(output_filepath, index=False, header=False)
        print("Output file saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving the output file: {str(e)}")

    # Explain variance ratio (not applicable for t-SNE)
    print("Explained variance ratio is not applicable for t-SNE.")


def print_help():
    print()
    print("This script performs dimensionality reduction using t-SNE on data stored in a CSV file.")
    print("Usage: python tsne.py [--help]")
    print()
    print("Options:")
    print("  --help     Display this help message and exit.")
    print()
    print("Description:")
    print("  This script reads a CSV file containing data and reduces its dimensionality using t-SNE (t-Distributed Stochastic Neighbor Embedding).")
    print("  It prompts the user to enter the file path of the input CSV file.")
    print("  The user is asked to provide the number of components to keep after dimensionality reduction.")
    print("  The script applies t-SNE on the data and transforms it to the lower-dimensional space.")
    print("  The reduced data is then rounded to the specified number of significant places.")
    print("  The processed data is saved to a new CSV file with '_tSNE' appended to the original file name.")
    print("  Please note that t-SNE does not provide explained variance ratio.")
    print()
    print("Example:")
    print("  python tsne.py")
    print("  - This will run the script and prompt the user to enter the necessary inputs.")
    print("  python tsne.py --help")
    print("  - This will display this help message and exit the script.")
    print()


if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

while True:
    try:
        print()
        n_components = int(input("Enter the number of components (should be less or equal to the number of features in the data): "))
        if n_components <= 0:
            raise ValueError
        break
    except ValueError:
        print()
        print("Enter a correct value.")
        continue

print()
filepath = input("Enter the path to the input CSV file: ")
filename = os.path.basename(filepath)
output_filename = filename[:-4] + '_tSNE.csv'
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)

print()
decimals = int(input("Specify how many decimal places to round off the values after performing t-SNE: "))
print()

reduce_csv_tsne(filepath, n_components, output_filepath, decimals)

KONIEC = input("Press Enter to finish the script: ")
print()

time.sleep(5)  # Opóźnienie przez 5 sekund
exit()