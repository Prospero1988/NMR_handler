import pandas as pd
from sklearn.random_projection import GaussianRandomProjection
import numpy as np
import os

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
