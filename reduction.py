# Import libraries
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess

while True:
    # Generate message
    print()
    print()
    print(" |--------------------------------------|")
    print(" |--- VECTOR DIMENSIONALITY REDUCTION --|")
    print(" |--------------------------------------|")
    print()
    print()
    print("Dimensionality reduction methods: ")
    print()
    print(" >> 1. PCA - Principal Component Analysis")
    print(" >> 2. ICA - Independent Component Analysis")
    print(" >> 3. NMF - Non-Negative Matrix Factorization")
    print(" >> 4. Random Projections")
    print(" >> 5. MultiCore t-SNE")
    print(" >> 6. UMAP")
    print(" >> 7. All methods")
    print()
    print(" >> 0. Exit")

    print()
    choice = input("Choose what you want to do: ")
    print()

    if choice == '1':
        subprocess.call(['python', 'pca.py'])
    elif choice == '2':
        subprocess.call(['python', 'ica.py'])
    elif choice == '3':
        subprocess.call(['python', 'nmf.py'])
    elif choice == '4':
        subprocess.call(['python', 'rp.py'])
    elif choice == '5':
        subprocess.call(['python', 'mctsne.py'])
    elif choice == '6':
        subprocess.call(['python', 'umap_sc.py'])
    elif choice == '7':
        subprocess.call(['python', 'total_reduction.py'])
    elif choice == '0':
        print()
        print("Exit selected. End of program.")
        print()
        break  # Przerwanie pętli while
    else:
        print()
        print("Incorrect selection. Try again.")
        print()
