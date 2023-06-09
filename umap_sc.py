import pandas as pd
import umap
import numpy as np
import sys 
import os

def print_help():
    print()
    print("Manual / Help Page:")
    print("------------------------------------------------------------------")
    print("This script performs dimensionality reduction using UMAP (Uniform Manifold Approximation and Projection) on a given CSV file.")
    print()
    print("Usage:")
    print("python script.py [--help]")
    print()
    print("Optional Arguments:")
    print("--help          Show this help message and exit")
    print()
    print("------------------------------------------------------------------")
    print("Description:")
    print("------------------------------------------------------------------")
    print("UMAP is a powerful dimensionality reduction technique that aims to preserve the local and global structure of high-dimensional data in a lower-dimensional representation.")
    print("This script allows you to apply UMAP on a CSV file containing the input data.")
    print()
    print("------------------------------------------------------------------")
    print("Instructions:")
    print("------------------------------------------------------------------")
    print("1. Ensure that you have installed the necessary libraries: pandas, umap-learn, and numpy.")
    print("   You can install them using pip:")
    print("   pip install pandas umap-learn numpy")
    print()
    print("2. Prepare your input CSV file:")
    print("   - The CSV file should contain the input data for dimensionality reduction.")
    print("   - Each row in the CSV file represents a data point.")
    print("   - Each column in the CSV file represents a feature of the data points.")
    print("   - The CSV file should not contain any headers.")
    print()
    print("3. Run the script:")
    print("   - Open a command prompt or terminal.")
    print("   - Navigate to the directory where the script is located.")
    print("   - Run the script using the following command:")
    print("     python script.py")
    print()
    print("4. Follow the prompts:")
    print("   - You will be prompted to enter the name of the CSV file.")
    print("   - Enter the name of the CSV file and press Enter.")
    print("   - You will be prompted to enter the target dimensionality.")
    print("   - Enter the desired target dimensionality (an integer value) and press Enter.")
    print("   - You will be prompted to provide additional information about the 'n_neighbors' and 'min_dist' parameters.")
    print("     - If you need more information, enter 'yes' and press Enter.")
    print("     - If you are already familiar with the parameters, enter 'no' and press Enter.")
    print("   - If you requested additional information, the script will display detailed explanations of the parameters.")
    print("   - After that, you will be prompted to enter the values for 'n_neighbors' and 'min_dist'.")
    print("     - You can either accept the default values or provide custom values.")
    print("     - Press Enter after entering each value.")
    print("   - The script will perform dimensionality reduction using UMAP on the input data.")
    print("   - You will be prompted to specify the number of significant places to round off the reduced values.")
    print("     - Enter the desired number of decimal places and press Enter.")
    print("   - The script will round off the reduced data to the specified number of decimal places.")
    print("   - The reduced data will be saved as a new CSV file with '_UMAP' appended to the original filename.")
    print("   - The script will display the path to the output CSV file.")
    print()

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print_help()
    sys.exit(0)

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
