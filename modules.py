import subprocess

# Define the modules you want to install
modules = [
    'matplotlib',
    'numpy',
    'pandas',
    'sklearn',
    'scipy',
    'MulticoreTSNE',
    'UMAP',

]

# Install the modules
for module in modules:
    subprocess.check_call(['pip', 'install', module])
print()
print("Modules installed successfully.")
print()
