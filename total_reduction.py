#total_reduction.py
import pandas as pd
import os
import sys
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA
from sklearn.decomposition import NMF
from sklearn.random_projection import GaussianRandomProjection
from MulticoreTSNE import MulticoreTSNE as TSNE
import umap
import numpy as np
import subprocess

while True:
    try:
        n_components = int(input("Enter target dimensionality: "))
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
decimals = int(input("Enter target number of decimals for value rounding: "))
print()
# PCA
def reduce_csv_pca(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the PCA model with n_components
    pca = PCA(n_components)

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

filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_PCA.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
reduce_csv_pca(filepath, n_components, output_filepath)

print(f"File saved as {output_filepath}")

# ICA

def reduce_csv_ica(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the ICA model with n_components
    ica = FastICA(n_components, whiten='arbitrary-variance', max_iter=10000)  # Set whiten to True

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

    print(f">>> Mixing matrix (unmixing matrix) shape: {mixing_matrix.shape}")
    print(f">>> Mixing matrix (unmixing matrix):\n\n{mixing_matrix}")
    print()

filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_ICA.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
reduce_csv_ica(filepath, n_components, output_filepath)
print(f"File saved as {output_filepath}")

# NMF

def reduce_csv_nmf(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the NMF model with n_components
    nmf = NMF(n_components, max_iter=10000)

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

filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_NMF.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
reduce_csv_nmf(filepath, n_components, output_filepath)
print(f"File saved as {output_filepath}")

# Random Projections

def reduce_csv_random_projection(filepath: str, n_components: int, output_filepath: str):
    # Load the data from the .csv file
    data = pd.read_csv(filepath, header=None)

    # Create the Random Projection model with n_components
    rp = GaussianRandomProjection(n_components)

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
filename = os.path.basename(filepath)  # Pobranie samej nazwy pliku bez ścieżki
output_filename = filename[:-4] + '_RP.csv'  # Usunięcie ostatnich 4 znaków (".csv") i dodanie nowego sufiksu
output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
print()
reduce_csv_random_projection(filepath, n_components, output_filepath)
print(f"File saved as {output_filepath}")

# MultiCore TSNE
print()
print("Check how to install MulticoreTSNE library at github site of the author:")
print("https://github.com/DmitryUlyanov/Multicore-TSNE/")
print()
print()
# read the data from the .csv file
data = pd.read_csv(filepath, header=None)
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

# UMAP

# Initialize UMAP model with target dimensionality
print()
print(">>> You have to specify additional parameters for reduction: ")
print()
need_help = input("Do you need addtional info about parameters n_neighbors and min_dist? (yes/no): ")
print()
if need_help == 'yes':
    subprocess.call(['python', 'mctsne_halp.py'])

n_neighbors = int(input("Enter value of n_neighbors, default (50): "))
print()
min_dist = float(input("Enter value of min_dist, default (0.5): "))

# Read in data from .csv file
data = pd.read_csv(filepath, header=None)

reducer = umap.UMAP(n_components)

# Fit and transform data using UMAP
reduced_data = reducer.fit_transform(data)

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
