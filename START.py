import subprocess
import os

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # Generate message
    print()
    print()
    print(" |--------------------------------------|")
    print(" |---------DATA HANDLING SCRIPT---------|")
    print(" |----for NMR data sets in CSV files----|")
    print(" |--------------------------------------|")
    print(" |-by Arkadiusz Leniak -----------------|")
    print(" |-arek.kein@gmail.com -----------------|")
    print(" |--------------------------------------|")
    print()
    print()
    print("Options: ")
    print()
    print(" >> 1. Check and automatically install the required modules using the pip function.")
    print()
    print(" >> 2. Merge multiple CSV files, transpose and normalize data.")
    print()
    print(" >> 3. Add Column Headers and copy columns from another CSV File.")
    print()
    print(" >> 4. Interpolate column to desired number in each row separetly.")
    print()
    print(" >> 5. Data normalization.")
    print()
    print(" >> 6. Run vector dimensionality reduction algorithms")
    print()
    print(" >> 0. Exit")

    print()
    choice = input("Choose what you want to do: ")
    print()

    if choice == '1':
        subprocess.call(['python', 'modules.py'])
    elif choice == '2':
        subprocess.call(['python', 'preparation.py'])
    elif choice == '3':
        subprocess.call(['python', 'header_and_column_insert.py'])
    elif choice == '4':
        subprocess.call(['python', 'interpolation2.py'])
    elif choice == '5':
            subprocess.call(['python', 'normalization.py'])
    elif choice == '6':
        subprocess.call(['python', 'reduction.py'])
    elif choice == '0':
        print()
        print("Exit selected. End of program.")
        print()
        break
    else:
        print()
        print("Incorrect selection. Try again.")
        print()
