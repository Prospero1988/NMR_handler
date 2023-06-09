import pandas as pd
from sklearn.random_projection import GaussianRandomProjection
import numpy as np
import os
import sys

def reduce_csv_random_projection(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the Random Projection model with n_components
    rp = GaussianRandomProjection(n_components, max_iter=10000)

    # Fit the Random Projection model on the data and transform the data to the new lower-dimensional space
    reduced_data = rp.fit_transform(data)

    # Round the reduced_data to the specified number of decimal places
    reduced_data = np.round(reduced_data, decimals)

    # Save the reduced data to a new csv file
    pd.DataFrame(reduced_data).to_csv(output_filepath, index=False, header=False)

    print()
    print(f">>> Reduced data shape: {reduced_data.shape}")
    print(f">>> Reduced data:\n\n{reduced_data}")
    print()

def print_help():
    print()
    print("Script Description:")
    print("This script performs random projection on a given CSV file containing data.")
    print("Random projection is a dimensionality reduction technique that reduces the number of features or dimensions in the data.")
    print("The reduced data is then saved to a new CSV file.")
    print()
    print("Usage:")
    print("python rp.py [--help]")
    print()
    print("Options:")
    print("  --help    Display this help message and exit")
    print()
    print("Arguments:")
    print("  None")
    print()
    print("Example Usage:")
    print("1. Display help message:")
    print("   python rp.py --help")
    print()
    print("2. Run the script with required arguments:")
    print("   python rp.py")
    print()
    print("Upon running the script, it will prompt for the following inputs:")
    print("1. Enter the number of components (should be less or equal to the number of features in data):")
    print("   - Specify the desired number of components for random projection.")
    print()
    print("2. Enter the path to the input .csv file:")
    print("   - Provide the full path to the input CSV file containing the data.")
    print()
    print("3. Specify how many significant places to round off the values after performing Random Projection:")
    print("   - Enter the number of decimal places to round off the reduced data.")
    print()
    print("Output:")
    print("The script will generate a new CSV file with the reduced data using random projection.")
    print("The file will be saved in the same directory as the input file, with the suffix '_RP' added to the filename.")
    print("The script will also display the shape and contents of the reduced data.")
    print()
    print("Note:")
    print("- The input file should be a CSV file without a header, where each row represents a data instance.")
    print("- The output file will also not contain any headers.")
    print()
    print("Dependencies:")
    print("This script requires the following libraries to be installed: pandas, scikit-learn (sklearn), numpy.")
    print()
    print("Author:")
    print("Arkadiusz Leniak | arek.kein@gmail.com")
    print()
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
output_filename = filename[:-4] + '_RP.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
decimals = int(input("Specify how many significant places to round off the values after performing Random Projection: "))
reduce_csv_random_projection(filepath, n_components, output_filepath)
print()
print(f">>> Data saved as: {output_filepath}")
print()
KONIEC = input("Press Enter to finish the script: ")
print()
exit()
