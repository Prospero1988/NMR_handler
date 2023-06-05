import pandas as pd
import umap
import numpy as np
import os

# Prompt user for .csv file
print()
filepath = input("Enter the name of the .csv file: ")

# Read in data from .csv file
data = pd.read_csv(filepath, header=None)

# Prompt user for target dimensionality
print()
target_dim = int(input("Enter target dimensionality: "))

# Initialize UMAP model with target dimensionality
print()
print(">>> You have to specify additional parameters for reduction: ")
print()
need_help = input("Do you need addtional info about parameters n_neighbors and min_dist? (yes/no): ")
print()
if need_help == 'yes':
    print()
    print("n_neighbors: ")
    print("     This parameter determines the number of neighbors used in ")
    print("     the local connectivity structure of the data. It controls the balance ")
    print("     between preserving local and global structure in the embedding. Larger ")
    print("     values will result in more global structure being preserved, but may also ")
    print("     lead to more smoothing of the data. Smaller values will focus more on ")
    print("     local structure but can be influenced by noise and result in less ")
    print("     meaningful embeddings.")
    print("     Start with a small value, such as 5 or 10, and gradually increase ")
    print("     it to observe the effects on the resulting embedding.")
    print("     Plot the resulting embeddings and inspect how the data points are ")
    print("     distributed. Look for clusters, separability, and preservation of ")
    print("     local and global structure.")
    print("     If the embedding appears too compact or clusters are not well-defined, ")
    print("     consider increasing the n_neighbors value.")
    print("     If the embedding is too scattered or lacks clear structure, consider ")
    print("     decreasing the n_neighbors value.")
    print()
    print("min_dist: ")
    print("     This parameter controls how tightly the embedded points ")
    print("     are packed together. It measures the minimum distance between points ")
    print("     in the low-dimensional space. Higher values encourage points to be ")
    print("     more evenly distributed, while lower values allow points to be closer ")
    print("     together.")
    print("     Start with a larger value, such as 0.5 or 0.8, to encourage more even ")
    print("     spacing of the points.")
    print("     Gradually decrease the min_dist value to bring the points closer together ")
    print("     while monitoring the effects on the embedding.")
    print("     Be cautious not to set min_dist too low, as it may result in overfitting ")
    print("     and poor generalization.")
    print("     If the embedding appears too crowded or lacks separation between clusters, ")
    print("     consider increasing the min_dist value.")
    print("     If the embedding is too spread out or lacks clear boundaries, consider ")
    print("     decreasing the min_dist value.")
    print()

n_neighbors = int(input("Enter value of n_neighbors, default (50): "))
print()
min_dist = float(input("Enter value of min_dist, default (0.5): "))

reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, n_components=target_dim)

# Fit and transform data using UMAP
reduced_data = reducer.fit_transform(data)

print()
decimals = int(input("Specify how many significant places to round off the values after performing UMAP: "))

# Round the reduced_data to the specified number of decimal places
rounded_data = np.round(reduced_data, decimals)

print()

filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_UMAP.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)

# Save reduced data to .csv file
pd.DataFrame(rounded_data).to_csv(output_filepath, header=None, index=None)

print(f">>> Data saved as: {output_filepath}")
print()
KONIEC = input("Press Enter to finish the script: ")
print()
exit()
