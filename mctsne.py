import pandas as pd
from MulticoreTSNE import MulticoreTSNE as TSNE
import numpy as np
import os

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
reducer = TSNE(n_components, n_jobs=-1)

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
