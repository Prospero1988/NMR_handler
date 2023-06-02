import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

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
