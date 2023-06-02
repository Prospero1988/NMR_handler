#This script searches a specified folder and removes all files in it
#hat have at least one of the keywords provided during script execution
#in their filenames.

import os

#Get the folder path
folder_path = input("Enter the path to the folder you want to work with: ")

#Get the keywords
keywords = input("Enter the keywords separated by space: ")
keywords = keywords.split()

#Variable to store the number of deleted files
deleted_files_count = 0

#Search the folder and remove files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        for keyword in keywords:
            if keyword in filename:
                os.remove(file_path)
                deleted_files_count += 1
                break # Break the loop if a keyword is found in the filename

#Display completion information
print("Task completed.")
print("Number of deleted files:", deleted_files_count)
