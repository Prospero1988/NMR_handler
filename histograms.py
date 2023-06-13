import pandas as pd
import matplotlib.pyplot as plt

# Prompt for a filename

file_path = input("Enter file name of the .csv file: ")

# Load data from CSV file
df = pd.read_csv(file_path)

# Select data columns (excluding headers and the first column)
data = df.iloc[1:, 1:].values.flatten().astype(float)

# Create a histogram
plt.hist(data, bins=100)

# Configure the plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data from CSV File')

# Display the plot
plt.show()
